#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fx_kw
import lc_kw
import le_kw
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
        CommonReader.__init__(self, 24, lc_kw.fq_uu_energy_qv)

    def vx_t_date(self, my_col, my_row):
        '''
        EnergyReader:
        '''
        value = self.vx_date(my_col, my_row)
        return '%04d-%02d-%02d' % value[:3]

    def prepare_time_columns(self):
        '''
        EnergyReader:
        '''
        start_col = self.vx_letter_num('B')
        data_headers = fx_kw.prepare_time_headers(start_col)
        return data_headers

    def verify_hours_headers(self, data_headers):
        '''
        EnergyReader:
        '''
        for one_column in data_headers:
            tmp_text = self.vx_num_time(one_column.col_in_sheet, 6)
            expected = one_column.header_for_hour_column
            mu_kw.verify_for_equal(tmp_text, expected)

    def detect_sheet_header(self, data_headers):
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
        self.verify_hours_headers(data_headers)
        return under_name

    def detect_data_rows(self):
        '''
        EnergyReader:
        '''
        nrows = self.sheet.nrows
        self.check_for_constant_string('A', 6, u'Data')
        self.check_for_constant_string('A', nrows - 2, u'Maksimum')
        self.check_for_constant_string('A', nrows - 1, u'Data')
        self.check_for_constant_string('A', nrows, u'Suma')
        return xrange(7, nrows - 2)

    def fetch_field(self, dfb, key_object, single_row, row_date, single_column):
        '''
        EnergyReader:
        '''
        my_hour = single_column.canonical_hour
        self.prepare_local_copy_of_row(dfb, key_object, row_date)
        value = self.vx_num_peek(single_column.col_in_sheet, single_row)
        if not le_kw.dq_entry_already_inserted(dfb, self.table_of_samples, key_object, row_date):
            value = self.vx_num_peek(single_column.col_in_sheet, single_row)
            if value:
                le_kw.dq_insert_energy_entry(dfb, self.table_of_samples, key_object, row_date, my_hour, value)

    def enter_data(self, dfb, key_object, data_headers, data_rows):
        '''
        EnergyReader:
        '''
        for single_row in data_rows:
            row_date = self.vx_t_date('A', single_row)
            for single_column in data_headers:
                self.fetch_field(dfb, key_object, single_row, row_date, single_column)

    def analyze_this_sheet(self, dfb):
        '''
        EnergyReader:
        '''
        data_headers = self.prepare_time_columns()
        under_name = self.detect_sheet_header(data_headers)
        key_object = mu_kw.locate_object_key(dfb, under_name)
        data_rows = self.detect_data_rows()
        self.enter_data(dfb, key_object, data_headers, data_rows)
