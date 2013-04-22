#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
import lc_kw
import le_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def new_module_for_reading_spreadsheet():
    import xlrd
    return xlrd

def new_module_for_writing_spreadsheet():
    import xlwt
    return xlwt

def check_module_dependencies_linux():
    new_module_for_reading_spreadsheet()
    new_module_for_writing_spreadsheet()

def verify_for_equal(tmp_text, expected):
    if tmp_text != expected:
        raise RuntimeError('tmp_text = %s' % repr(tmp_text))

def locate_object_key(dfb, under_name):
    key_object = le_kw.dq_object_key(dfb, under_name)
    if not key_object:
        key_object = le_kw.dq_add_new_object_key(dfb, under_name)
    ret_size = len(key_object)
    if ret_size == 1:
        key_object = key_object[0][lc_kw.fq_k_object_qv];
    else:
        raise RuntimeError('ret_size = %d' % ret_size)
    return key_object

class GatheredRows:
    def __init__(self):
        '''
        GatheredRows:
        '''
        self.internal_rows = {}

    def locate_this_row(self, key_object, row_date):
        '''
        GatheredRows:
        '''
        local_key = (key_object, row_date)
        result = self.internal_rows.get(local_key)
        return result

    def prepare_local_copy_of_row(self):
        '''
        GatheredRows:
        '''
        if (key_object, row_date) not in self.internal_rows:
            existing_rows = le_kw.dq_entry_already_inserted(dfb, self.table_of_samples, key_object, row_date)
            no_of_rows = len(existing_rows)
            if no_of_rows == 0:
                pass

class CommonReader:
    def __init__(self, cnt_per_day, table_of_samples):
        '''
        CommonReader:
        '''
        self.cnt_per_day = cnt_per_day
        self.table_of_samples = table_of_samples
        self.vx_zero = fv_kw.vx_zero
        self.day_zero = (0, 0, 0)
        self.gathered_rows = GatheredRows()
        self.internal_rows = {}

    def vx_num_peek(self, my_col, my_row):
        '''
        CommonReader:
        '''
        return self.sheet.cell_value(my_row - 1, my_col)

    def vx_letter_num(self, my_col):
        '''
        CommonReader:
        '''
        return self.vx_zero.vx_lt(my_col)

    def vx_peek(self, my_col, my_row):
        '''
        CommonReader:
        '''
        header_col = self.vx_letter_num(my_col)
        return self.vx_num_peek(header_col, my_row)

    def vx_date(self, my_col, my_row):
        '''
        CommonReader:
        '''
        value = self.vx_peek(my_col, my_row)
        return self.xlrd.xldate_as_tuple(value, self.book.datemode)

    def vx_num_time(self, my_col, my_row):
        '''
        CommonReader:
        '''
        value = self.vx_num_peek(my_col, my_row)
        time_tuple = self.xlrd.xldate_as_tuple(value, self.book.datemode)
        day_part = time_tuple[:3]
        time_part = time_tuple[3:]
        verify_for_equal(day_part, self.day_zero)
        return datetime.time(*time_part).strftime('%H:%M')

    def check_for_constant_string(self, my_col, my_row, expected):
        '''
        CommonReader:
        '''
        tmp_text = self.vx_peek(my_col, my_row)
        verify_for_equal(tmp_text, expected)

    def prepare_data_row(self, dfb, key_object, row_date):
        '''
        CommonReader:
        '''
        self.gathered_rows.prepare_local_copy_of_row(dfb, key_object, row_date, self.table_of_samples)

    def analyze_this_file(self, dfb, xlrd, single_file):
        '''
        CommonReader:
        '''
        self.xlrd = xlrd
        self.book = self.xlrd.open_workbook(single_file)
        numer_of_sheets = self.book.nsheets
        if numer_of_sheets == 1:
            self.sheet = self.book.sheet_by_name(u'Report')
            self.analyze_this_sheet(dfb)
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)
