#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
import jl_kw
import lw_kw
import tq_kw
import tt_kw
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
        period_server = jl_kw.HourServer()
        CommonReader.__init__(self, lw_kw.Dn_Energy, period_server)
        self.start_energy_col = self.vx_letter_num('B')

    def vx_t_date(self, lb_col, my_row):
        '''
        EnergyReader:
        '''
        value = self.vx_date(lb_col, my_row)
        return dn_kw.NapisDaty( * value[:3])

    def detect_energy_sheet_header(self):
        '''
        EnergyReader:
        '''
        self.check_for_constant_string('B', 2, u'Raport energii godzinowej dla ')
        under_name = self.vx_peek('E', 2)
        period_start = self.vx_date('E', 3)
        period_end = self.vx_date('H', 3)
        self.check_for_constant_string('M', 2, u'kWh')
        self.check_for_constant_string('B', 3, u'Za okres')
        self.check_for_constant_string('D', 3, u'od')
        self.check_for_constant_string('G', 3, u'do ')
        self.check_for_constant_string('B', 5, u'Godziny')
        self.period_server.verify_hours_headers(self, self.start_energy_col)
        return under_name

    def detect_energy_data_rows(self):
        '''
        EnergyReader:
        '''
        nrows = self.sheet.nrows
        self.check_for_constant_string('A', 6, u'Data')
        self.check_for_constant_string('A', nrows - 2, u'Maksimum')
        self.check_for_constant_string('A', nrows - 1, u'Data')
        self.check_for_constant_string('A', nrows, u'Suma')
        return xrange(7, nrows - 2)

    def fetch_energy_field(self, dfb, key_object, single_row, row_date, single_column, sample_index):
        '''
        EnergyReader:
        '''
        self.prepare_local_copy_of_row(dfb, key_object, row_date)
        col_in_sheet = self.start_energy_col + sample_index
        value = self.vx_num_peek(col_in_sheet, single_row)
        self.store_value_in_row(key_object, row_date, sample_index, value)

    def enter_energy_data(self, dfb, key_object, data_rows):
        '''
        EnergyReader:
        '''
        for single_row in data_rows:
            row_date = self.vx_t_date('A', single_row)
            for sample_index, single_column in enumerate(self.period_server.all_time_columns):
                self.fetch_energy_field(dfb, key_object, single_row, row_date, single_column, sample_index)

    def analyze_data_in_grid(self, dfb):
        '''
        EnergyReader:
        '''
        under_name = self.detect_energy_sheet_header()
        key_object = tq_kw.locate_object_key(dfb, under_name)
        data_rows = self.detect_energy_data_rows()
        self.enter_energy_data(dfb, key_object, data_rows)
        self.store_rows_in_db(dfb)

class Pseudo_Book(object):
    def __init__(self):
        '''
        Pseudo_Book:
        '''
        self.nsheets = 1
        self.datemode = None

    def sheet_by_name(self, name):
        '''
        Pseudo_Book:
        '''
        return Pseudo_Sheet()

class Pseudo_XLRD(object):
    def __init__(self):
        '''
        Pseudo_XLRD:
        '''

    def open_workbook(self, single_file):
        '''
        Pseudo_XLRD:
        '''
        return Pseudo_Book()

    def xldate_as_tuple(self, value, datemode):
        '''
        Pseudo_XLRD:
        '''
        if len(value) == 3:
            result = value + (0, 0, 0)
        else:
            result = (0, 0, 0) + value + (0,)
        return result

class Pseudo_Sheet(object):
    def __init__(self):
        '''
        Pseudo_Sheet:
        '''
        self.grid = {}

    def cell_value(self, row, col):
        '''
        Pseudo_Sheet:
        '''
        return self.grid[(row, col)]

    def cell_set_value(self, row, col, value):
        '''
        Pseudo_Sheet:
        '''
        self.grid[(row, col)] = value

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
        self.vx_poke('E', 2, None)
        self.vx_poke('E', 3, None)
        self.vx_poke('H', 3, None)
        self.vx_poke('M', 2, u'kWh')
        self.vx_poke('B', 3, u'Za okres')
        self.vx_poke('D', 3, u'od')
        self.vx_poke('G', 3, u'do ')
        self.vx_poke('B', 5, u'Godziny')

class Test_Reader_of_Energy(unittest.TestCase):
    def test_energy_1_reader(self):
        '''
        Test_Reader_of_Energy:
        '''
        obk = EnergyReader()

class Test_XLRD(unittest.TestCase):
    def test_1_xlrd(self):
        '''
        Test_XLRD:
        '''
        xlrd = Pseudo_XLRD()
        value = (1, 2)
        odp = xlrd.xldate_as_tuple(value, None)
        self.assertEqual(odp, (0, 0, 0, 1, 2, 0))

    def test_2_xlrd(self):
        '''
        Test_XLRD:
        '''
        xlrd = Pseudo_XLRD()
        value = (2014, 1, 4)
        odp = xlrd.xldate_as_tuple(value, None)
        self.assertEqual(odp, (2014, 1, 4, 0, 0, 0))
