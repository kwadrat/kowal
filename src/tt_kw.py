#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import fv_kw
import le_kw
import lp_kw
import lq_kw
import tq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def normalize_value(before):
    if before == '':
        result = None
    else:
        result = before
    return result

CommonRdWr = tq_kw.CommonRdWr

class CommonReader(CommonRdWr):
    def __init__(self, tvk_pobor, period_server):
        '''
        CommonReader:
        '''
        CommonRdWr.__init__(self, tvk_pobor, period_server)
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
        my_sample_row.new_and_empty(self.krt_pobor.krt_wymiar)
        self.internal_rows[local_key] = my_sample_row

    def store_value_in_row(self, key_object, row_date, sample_index, value):
        '''
        CommonReader:
        '''
        local_key = (key_object, row_date)
        dst_allow = self.period_server.dst_double_hour(row_date, sample_index)
        adjusted = normalize_value(value)
        self.internal_rows[local_key].update_for_index(sample_index, adjusted, dst_allow, row_date)

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

    def vx_peek(self, lb_col, my_row):
        '''
        CommonReader:
        '''
        header_col = self.vx_letter_num(lb_col)
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

    def check_for_constant_string(
            self,
            my_col,
            my_row,
            expected,
            exp_second=None,
            ):
        '''
        CommonReader:
        '''
        tmp_text = self.vx_peek(my_col, my_row)
        if exp_second is None:
            lp_kw.verify_for_equal(tmp_text, expected)
        else:
            lp_kw.verify_for_2_equal(tmp_text, [expected, exp_second])

    def analyze_this_file(self, xlrd, single_file):
        '''
        CommonReader:
        '''
        self.xlrd = xlrd
        self.book = self.xlrd.open_workbook(single_file)
        numer_of_sheets = self.book.nsheets
        if numer_of_sheets == 1:
            self.sheet = self.book.sheet_by_name(u'Report')
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

    def store_rows_in_db(self, dfb):
        '''
        CommonReader:
        '''
        for local_key, my_sample_row in self.internal_rows.iteritems():
            my_sample_row.put_in_database(dfb, self.krt_pobor, self.table_of_samples, local_key)

    def recalculate_statistics(self, dfb):
        '''
        CommonReader:
        '''
        self.all_results = le_kw.dq_for_statistics(dfb, self.table_of_samples)
        for one_result in self.all_results:
            sample_key = one_result[lc_kw.fq_k_sample_qv]
            tmp_samples = one_result[lc_kw.fq_m_samples_qv]
            my_sample_row = lq_kw.SampleRow()
            my_sample_row.fill_from_data(sample_key, tmp_samples)
            my_sample_row.make_stats_of_samples(
                dfb, self.krt_pobor, self.table_of_samples, sample_key)

class Test_Common_Reader(unittest.TestCase):
    def test_common_reader(self):
        '''
        Test_Common_Reader:
        '''
        self.assertEqual(normalize_value(''), None)
        self.assertEqual(normalize_value(0), 0)
