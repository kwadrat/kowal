#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
import lc_kw
import le_kw
import lp_kw
import lq_kw
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

def unique_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field], dane_bazy)))
    object_names.sort()
    return object_names

def unique_a_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field][:5], dane_bazy)))
    object_names.sort()
    return object_names

class CommonReader:
    def __init__(self, cnt_per_day, table_of_samples):
        '''
        CommonReader:
        '''
        self.cnt_per_day = cnt_per_day
        self.table_of_samples = table_of_samples
        self.vx_zero = fv_kw.vx_zero
        self.internal_rows = {}

    def locate_this_row(self, key_object, row_date):
        '''
        CommonReader:
        '''
        local_key = (key_object, row_date)
        result = self.internal_rows.get(local_key)
        return result

    def prepare_new_empty_row(self, key_object, row_date):
        '''
        CommonReader:
        '''
        local_key = (key_object, row_date)
        my_sample_row = lq_kw.SampleRow()
        my_sample_row.new_and_empty(self.cnt_per_day)
        self.internal_rows[local_key] = my_sample_row

    def store_value_in_row(self, key_object, row_date, sample_index, value):
        '''
        CommonReader:
        '''
        local_key = (key_object, row_date)
        self.internal_rows[local_key].update_for_index(sample_index, value)

    def fetch_data_from_database(self, key_object, row_date, sample_data):
        '''
        CommonReader:
        '''
        local_key = (key_object, row_date)
        sample_key, tmp_object, tmp_date, tmp_samples = sample_data
        tmp_date = lp_kw.rj_na_date(tmp_date)
        lp_kw.verify_for_equal(tmp_object, key_object)
        lp_kw.verify_for_equal(tmp_date, row_date)
        my_sample_row = lq_kw.SampleRow()
        my_sample_row.fill_from_data(sample_key, tmp_samples)
        self.internal_rows[local_key] = my_sample_row

    def prepare_local_copy_of_row(self, dfb, key_object, row_date):
        '''
        CommonReader:
        '''
        if not self.locate_this_row(key_object, row_date):
            existing_rows = le_kw.dq_entry_already_inserted(dfb, self.table_of_samples, key_object, row_date)
            no_of_rows = len(existing_rows)
            if no_of_rows == 0:
                self.prepare_new_empty_row(key_object, row_date)
            elif no_of_rows == 1:
                self.fetch_data_from_database(key_object, row_date, existing_rows[0])
            else:
                raise RuntimeError('no_of_rows = %s' % repr(no_of_rows))

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
        return lp_kw.process_hour_headers(time_tuple)

    def check_for_constant_string(self, my_col, my_row, expected):
        '''
        CommonReader:
        '''
        tmp_text = self.vx_peek(my_col, my_row)
        lp_kw.verify_for_equal(tmp_text, expected)

    def analyze_this_file(self, dfb, xlrd, single_file):
        '''
        CommonReader:
        '''
        self.xlrd = xlrd
        self.book = self.xlrd.open_workbook(single_file)
        numer_of_sheets = self.book.nsheets
        if numer_of_sheets == 1:
            self.sheet = self.book.sheet_by_name(u'Report')
            self.analyze_data_in_grid(dfb)
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

    def store_rows_in_db(self, dfb):
        '''
        CommonReader:
        '''
        for local_key, my_sample_row in self.internal_rows.iteritems():
            (key_object, row_date) = local_key
            sample_key = my_sample_row.get_row_key()
            all_samples = my_sample_row.get_row_of_samples()
            if sample_key:
                le_kw.dq_update_vector_of_samples(dfb, self.table_of_samples, sample_key, key_object, row_date, all_samples)
            else:
                le_kw.dq_insert_vector_of_samples(dfb, self.table_of_samples, key_object, row_date, all_samples)
