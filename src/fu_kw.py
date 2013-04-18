#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
import fx_kw
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

class DataReader(CommonReader):
    def __init__(self):
        '''
        DataReader:
        '''
        CommonReader.__init__(self)

    def vx_t_date(self, my_col, my_row):
        '''
        DataReader:
        '''
        value = self.vx_date(my_col, my_row)
        return '%04d-%02d-%02d' % value[:3]

    def vx_num_time(self, my_col, my_row):
        '''
        DataReader:
        '''
        value = self.vx_num_peek(my_col, my_row)
        time_tuple = self.xlrd.xldate_as_tuple(value, self.book.datemode)
        day_part = time_tuple[:3]
        time_part = time_tuple[3:]
        mu_kw.verify_for_equal(day_part, self.day_zero)
        return datetime.time(*time_part).strftime('%H:%M')

    def check_for_constant_string(self, my_col, my_row, expected):
        '''
        DataReader:
        '''
        tmp_text = self.vx_peek(my_col, my_row)
        mu_kw.verify_for_equal(tmp_text, expected)

    def prepare_time_columns(self):
        '''
        DataReader:
        '''
        start_col = self.vx_letter_num('B')
        data_headers = fx_kw.prepare_time_headers(start_col)
        return data_headers

    def verify_hours_headers(self, data_headers):
        '''
        DataReader:
        '''
        for one_column in data_headers:
            tmp_text = self.vx_num_time(one_column.col_in_sheet, 6)
            expected = one_column.header_for_hour_column
            mu_kw.verify_for_equal(tmp_text, expected)

    def detect_sheet_header(self, data_headers):
        '''
        DataReader:
        '''
        self.check_for_constant_string('B', 2, u'Raport energii godzinowej dla ')
        under_name = self.vx_peek('E', 2)
        tmp_format = 'under_name'; print 'Eval:', tmp_format, eval(tmp_format)
        period_start = self.vx_date('E', 3)
        tmp_format = 'period_start'; print 'Eval:', tmp_format, eval(tmp_format)
        period_end = self.vx_date('H', 3)
        tmp_format = 'period_end'; print 'Eval:', tmp_format, eval(tmp_format)
        self.check_for_constant_string('M', 2, u'kWh')
        self.check_for_constant_string('B', 3, u'Za okres')
        self.check_for_constant_string('D', 3, u'od')
        self.check_for_constant_string('G', 3, u'do ')
        self.check_for_constant_string('B', 5, u'Godziny')
        self.verify_hours_headers(data_headers)
        return under_name

    def detect_data_rows(self):
        '''
        DataReader:
        '''
        nrows = self.sheet.nrows
        self.check_for_constant_string('A', 6, u'Data')
        self.check_for_constant_string('A', nrows - 2, u'Maksimum')
        self.check_for_constant_string('A', nrows - 1, u'Data')
        self.check_for_constant_string('A', nrows, u'Suma')
        return xrange(7, nrows - 2)

    def fetch_field(self, dfb, key_object, single_row, row_date, single_column):
        '''
        DataReader:
        '''
        my_hour = single_column.canonical_hour
        if not mu_kw.entry_already_inserted(dfb, 'uu_energy', key_object, row_date, my_hour):
            value = self.vx_num_peek(single_column.col_in_sheet, single_row)
            mu_kw.insert_energy_entry(dfb, 'uu_energy', key_object, row_date, my_hour, value)

    def enter_data(self, dfb, key_object, data_headers, data_rows):
        '''
        DataReader:
        '''
        for single_row in data_rows:
            row_date = self.vx_t_date('A', single_row)
            for single_column in data_headers:
                self.fetch_field(dfb, key_object, single_row, row_date, single_column)

    def analyze_this_sheet(self, dfb):
        '''
        DataReader:
        '''
        data_headers = self.prepare_time_columns()
        under_name = self.detect_sheet_header(data_headers)
        key_object = mu_kw.locate_object_key(dfb, under_name)
        data_rows = self.detect_data_rows()
        self.enter_data(dfb, key_object, data_headers, data_rows)
        print data_rows

    def analyze_this_file(self, dfb, xlrd, single_file):
        '''
        DataReader:
        '''
        self.xlrd = xlrd
        self.book = self.xlrd.open_workbook(single_file)
        numer_of_sheets = self.book.nsheets
        if numer_of_sheets == 1:
            self.sheet = self.book.sheet_by_name(u'Report')
            self.analyze_this_sheet(dfb)
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

def analyze_excel_files(dfb, filenames):
    xlrd = mu_kw.new_module_for_reading_spreadsheet()
    for single_file in filenames:
        obk = DataReader()
        obk.analyze_this_file(dfb, xlrd, single_file)
