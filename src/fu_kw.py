#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
import lp_kw
import lw_kw
import tq_kw
import mu_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

CommonReader = mu_kw.CommonReader

class EnergyReader(CommonReader):
    def __init__(self):
        '''
        EnergyReader:
        '''
        CommonReader.__init__(self, lw_kw.Dn_Energy)
        start_col = self.vx_letter_num('B')
        period_server = lp_kw.HourServer(start_col)
        self.set_pd_server(period_server)

    def vx_t_date(self, my_col, my_row):
        '''
        EnergyReader:
        '''
        value = self.vx_date(my_col, my_row)
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
        self.period_server.verify_hours_headers(self)
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

    def fetch_energy_field(self, dfb, key_object, single_row, row_date, single_column):
        '''
        EnergyReader:
        '''
        self.prepare_local_copy_of_row(dfb, key_object, row_date)
        value = self.vx_num_peek(single_column.col_in_sheet, single_row)
        hour_number = single_column.column_index
        self.store_value_in_row(key_object, row_date, hour_number, value)

    def enter_energy_data(self, dfb, key_object, data_rows):
        '''
        EnergyReader:
        '''
        for single_row in data_rows:
            row_date = self.vx_t_date('A', single_row)
            for single_column in self.period_server.all_time_columns:
                self.fetch_energy_field(dfb, key_object, single_row, row_date, single_column)

    def analyze_data_in_grid(self, dfb):
        '''
        EnergyReader:
        '''
        under_name = self.detect_energy_sheet_header()
        key_object = tq_kw.locate_object_key(dfb, under_name)
        data_rows = self.detect_energy_data_rows()
        self.enter_energy_data(dfb, key_object, data_rows)
        self.store_rows_in_db(dfb)

CommonWriter = mu_kw.CommonWriter

class EnergyWriter(CommonWriter):
    def __init__(self):
        '''
        EnergyWriter:
        '''
        CommonWriter.__init__(self, lw_kw.Dn_Energy)
        start_col = 0
        period_server = lp_kw.HourServer(start_col)
        self.set_pd_server(period_server)
