#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import uu_kw
import lm_kw
import dn_kw
import lp_kw
import jl_kw
import lw_kw
import tq_kw
import tt_kw
import jq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

CommonReader = tt_kw.CommonReader

class EnergyReader(CommonReader):
    def __init__(self):
        '''
        EnergyReader:
        '''
        self.is_csv = 0 # Dla pliku XLS
        self.tel_delta = 1 # Jest jedna pusta linia na początku XLS
        self.extra_dst_column = 0
        period_server = jl_kw.HourServer()
        CommonReader.__init__(self, lw_kw.Dm_Energy, period_server)
        self.start_energy_col = self.vx_letter_num('B')

    def delta_for_csv(self):
        '''
        EnergyReader:
        '''
        self.is_csv = 1 # Dla pliku CSV/TXT
        self.tel_delta = 0 # Nie ma pustych linii na początku

    def set_dst_column(self):
        '''
        EnergyReader:
        '''
        self.extra_dst_column = 1

    def vx_t_date(self, lb_col, my_row):
        '''
        EnergyReader:
        '''
        value = self.vx_date(lb_col, my_row)
        return dn_kw.NapisDaty( * value[:3])

    def verify_hours_headers(self):
        '''
        EnergyReader:
        '''
        for sample_index, one_column in enumerate(self.period_server.all_time_columns):
            tmp_text = self.vx_num_time(
                self.start_energy_col +
                sample_index +
                self.extra_dst_column, 5 + self.tel_delta)
            expected = one_column.header_for_hour_column
            if (
                    tmp_text == '02:00' and
                    expected == '03:00' and
                    sample_index == 2):
                self.set_dst_column()
                continue
            lp_kw.verify_for_equal(tmp_text, expected)

    def vx_delta_peek(self, lb_col, my_row):
        '''
        EnergyReader:
        '''
        return self.vx_peek(
            lb_col, my_row, col_delta=self.extra_dst_column)

    def vx_delta_date(self, lb_col, my_row):
        '''
        EnergyReader:
        '''
        return self.vx_date(
            lb_col, my_row, col_delta=self.extra_dst_column)

    def check_for_delta_string(
            self,
            lb_col,
            my_row,
            expected,
            exp_second=None,
            col_delta=0,
            ):
        '''
        EnergyReader:
        '''
        self.check_for_constant_string(
            lb_col, my_row, expected, exp_second=exp_second,
            col_delta=self.extra_dst_column)

    def detect_energy_sheet_header(self):
        '''
        EnergyReader:
        '''
        self.check_for_constant_string('B', 1 + self.tel_delta, u'Raport energii godzinowej dla ')
        self.verify_hours_headers()
        self.check_for_delta_string('M', 1 + self.tel_delta, u'kWh')
        self.check_for_constant_string('B', 2 + self.tel_delta, u'Za okres')
        self.check_for_delta_string('D', 2 + self.tel_delta, u'od')
        self.check_for_delta_string('G', 2 + self.tel_delta, u'do ')
        self.check_for_constant_string('B', 4 + self.tel_delta, u'Godziny')
        under_name = self.vx_delta_peek('E', 1 + self.tel_delta)
        period_start = self.vx_delta_date('E', 2 + self.tel_delta)
        period_end = self.vx_delta_date('H', 2 + self.tel_delta)
        return under_name

    def detect_energy_data_rows(self):
        '''
        EnergyReader:
        '''
        nrows = self.sheet.nrows
        self.check_for_constant_string('A', 5 + self.tel_delta, u'Data')
        self.check_for_constant_string('A', nrows - 2, u'Maksimum')
        self.check_for_constant_string('A', nrows - 1, u'Data')
        self.check_for_constant_string('A', nrows, u'Suma')
        return uu_kw.vx_wiersze(6 + self.tel_delta, nrows - 3)

    def simple_energy_read(self, single_row, sample_index):
        '''
        EnergyReader:
        '''
        col_in_sheet = self.start_energy_col + sample_index
        value = self.vx_num_peek(col_in_sheet, single_row)
        return value

    def energy_using_dst(self, single_row, sample_index, autumn_dst_date):
        '''
        EnergyReader:
        '''
        if self.extra_dst_column:
            if autumn_dst_date and sample_index == 1:
                value = self.simple_energy_read(single_row, sample_index)
                value += self.simple_energy_read(single_row, sample_index + 1)
            else:
                if sample_index == 1:
                    empty_value = self.simple_energy_read(single_row, sample_index + 1)
                    lp_kw.verify_for_equal(empty_value, '')
                if sample_index > 1:
                    col_delta = 1
                else:
                    col_delta = 0
                value = self.simple_energy_read(single_row, sample_index + col_delta)
        else:
            value = self.simple_energy_read(single_row, sample_index)
        return value

    def fetch_energy_field(self, key_object, single_row, row_date, autumn_dst_date, sample_index):
        '''
        EnergyReader:
        '''
        value = self.energy_using_dst(single_row, sample_index, autumn_dst_date)
        if self.is_csv:
            value = lm_kw.adjust_for_csv(value)

        self.store_hour_value_in_row(key_object, row_date, sample_index, value)

    def enter_energy_data(self, dfb, key_object, data_rows):
        '''
        EnergyReader:
        '''
        for single_row in data_rows:
            row_date = self.vx_t_date('A', single_row)
            autumn_dst_date = dn_kw.autumn_dst_day(row_date)
            self.prepare_local_copy_of_row(dfb, key_object, row_date)
            for sample_index in xrange(24):
                self.fetch_energy_field(key_object, single_row, row_date, autumn_dst_date, sample_index)

    def analyze_data_in_grid(self, dfb):
        '''
        EnergyReader:
        '''
        under_name = self.detect_energy_sheet_header()
        key_object = tq_kw.locate_object_key(dfb, under_name)
        data_rows = self.detect_energy_data_rows()
        self.enter_energy_data(dfb, key_object, data_rows)
        self.store_rows_in_db(dfb)

class AugmentedEnReader(EnergyReader):
    def vx_num_poke(self, my_col, my_row, my_value):
        '''
        AugmentedEnReader:
        '''
        self.sheet.cell_set_value(my_row - 1, my_col, my_value)

    def vx_poke(self, lb_col, my_row, my_value):
        '''
        AugmentedEnReader:
        '''
        my_col = self.vx_letter_num(lb_col)
        self.vx_num_poke(my_col, my_row, my_value)

    def __init__(self):
        '''
        AugmentedEnReader:
        '''
        EnergyReader.__init__(self)

    def fill_a_case(self):
        '''
        AugmentedEnReader:
        '''
        self.vx_poke('B', 2, u'Raport energii godzinowej dla ')
        self.vx_poke('M', 2, u'kWh')
        self.vx_poke('B', 3, u'Za okres')
        self.vx_poke('D', 3, u'od')
        self.vx_poke('G', 3, u'do ')
        self.vx_poke('B', 5, u'Godziny')
        self.vx_poke('E', 2, None)
        self.vx_poke('E', 3, (2013, 12, 1))
        self.vx_poke('H', 3, (2014, 1, 1))
        self.vx_poke('B', 6, (1, 0))
        self.vx_poke('C', 6, (2, 0))
        self.vx_poke('D', 6, (3, 0))
        self.vx_poke('E', 6, (4, 0))
        self.vx_poke('F', 6, (5, 0))
        self.vx_poke('G', 6, (6, 0))
        self.vx_poke('H', 6, (7, 0))
        self.vx_poke('I', 6, (8, 0))
        self.vx_poke('J', 6, (9, 0))
        self.vx_poke('K', 6, (10, 0))
        self.vx_poke('L', 6, (11, 0))
        self.vx_poke('M', 6, (12, 0))
        self.vx_poke('N', 6, (13, 0))
        self.vx_poke('O', 6, (14, 0))
        self.vx_poke('P', 6, (15, 0))
        self.vx_poke('Q', 6, (16, 0))
        self.vx_poke('R', 6, (17, 0))
        self.vx_poke('S', 6, (18, 0))
        self.vx_poke('T', 6, (19, 0))
        self.vx_poke('U', 6, (20, 0))
        self.vx_poke('V', 6, (21, 0))
        self.vx_poke('W', 6, (22, 0))
        self.vx_poke('X', 6, (23, 0))
        self.vx_poke('Y', 6, (0, 0))

    def fill_b_case(self):
        '''
        AugmentedEnReader:
        '''
        self.vx_poke('B', 2, u'Raport energii godzinowej dla ')
        self.vx_poke('N', 2, u'kWh')
        self.vx_poke('B', 3, u'Za okres')
        self.vx_poke('E', 3, u'od')
        self.vx_poke('H', 3, u'do ')
        self.vx_poke('B', 5, u'Godziny')
        self.vx_poke('F', 2, None)
        self.vx_poke('F', 3, (2013, 12, 1))
        self.vx_poke('I', 3, (2014, 1, 1))
        self.vx_poke('B', 6, (1, 0))
        self.vx_poke('C', 6, (2, 0))
        self.vx_poke('D', 6, (2, 0))
        self.vx_poke('E', 6, (3, 0))
        self.vx_poke('F', 6, (4, 0))
        self.vx_poke('G', 6, (5, 0))
        self.vx_poke('H', 6, (6, 0))
        self.vx_poke('I', 6, (7, 0))
        self.vx_poke('J', 6, (8, 0))
        self.vx_poke('K', 6, (9, 0))
        self.vx_poke('L', 6, (10, 0))
        self.vx_poke('M', 6, (11, 0))
        self.vx_poke('N', 6, (12, 0))
        self.vx_poke('O', 6, (13, 0))
        self.vx_poke('P', 6, (14, 0))
        self.vx_poke('Q', 6, (15, 0))
        self.vx_poke('R', 6, (16, 0))
        self.vx_poke('S', 6, (17, 0))
        self.vx_poke('T', 6, (18, 0))
        self.vx_poke('U', 6, (19, 0))
        self.vx_poke('V', 6, (20, 0))
        self.vx_poke('W', 6, (21, 0))
        self.vx_poke('X', 6, (22, 0))
        self.vx_poke('Y', 6, (23, 0))
        self.vx_poke('Z', 6, (0, 0))

class Test_Reader_of_Energy(unittest.TestCase):
    def test_energy_1_reader(self):
        '''
        Test_Reader_of_Energy:
        '''
        obk = AugmentedEnReader()
        xlrd = jq_kw.Pseudo_XLRD()
        single_file = None
        obk.analyze_this_file(xlrd, single_file)
        obk.fill_a_case()
        under_name = obk.detect_energy_sheet_header()

    def test_energy_2_reader(self):
        '''
        Test_Reader_of_Energy:
        '''
        obk = AugmentedEnReader()
        xlrd = jq_kw.Pseudo_XLRD()
        single_file = None
        obk.analyze_this_file(xlrd, single_file)
        wzor = 'abc'
        obk.vx_poke('N', 2, wzor)
        self.assertEqual(obk.vx_peek('N', 2), wzor)
        self.assertEqual(obk.vx_peek('M', 2, col_delta=1), wzor)

    def test_energy_3_reader(self):
        '''
        Test_Reader_of_Energy:
        '''
        obk = AugmentedEnReader()
        xlrd = jq_kw.Pseudo_XLRD()
        single_file = None
        obk.analyze_this_file(xlrd, single_file)
        obk.fill_b_case()
        under_name = obk.detect_energy_sheet_header()

    def test_energy_4_reader(self):
        '''
        Test_Reader_of_Energy:
        '''
        obk = EnergyReader()
        self.assertEqual(obk.extra_dst_column, 0)
        obk.set_dst_column()
        self.assertEqual(obk.extra_dst_column, 1)

    def test_energy_4_reader(self):
        '''
        Test_Reader_of_Energy:
        '''
        obk = EnergyReader()
        self.assertEqual(obk.is_csv, 0)
        self.assertEqual(obk.tel_delta, 1)
        obk.delta_for_csv()
        self.assertEqual(obk.is_csv, 1)
        self.assertEqual(obk.tel_delta, 0)
