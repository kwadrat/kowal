#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import to_kw
import fv_kw
import rq_kw
import dn_kw
import lr_kw
import le_kw
import lp_kw
import dd_kw
import lq_kw
import eo_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

dict_names = {
    'GIMNAZJUM_NR_7_RYBNIK_SZTOLNIOWA': 'G-7',
    'SZKOLA_PODST_NR_11_RYBNIK_HIBNERA': 'SP-11',
    'SZKOLA_PODSTAWOWA_NR_13_CHWALOWICE': 'SP-13',
    'SZKOLA_PODSTAWOWA_NR_20_RYBNIK_ZIOLOWA': 'SP-20',
    'SZKOLA_PODSTAWOWA_NR_28_RYBNIK_SZEWCZYKA': 'SP-28',
    'SZKOLA_PODST_NR_3_RYBNIK_WOLNA': 'SP-3',
    'SZKOLA_PODSTAWOWA_NR_37_RYBNIK': 'SP-37',
    'ZESPOL_SZKOL_EKON_USLUG_RYBNIK': 'ZSE-U',
    'ZESPOL_SZKOL_TECHNICZNYCH_RYBNIK_KOSCIUSZKI': 'ZST',
    'ZESPOL_SZKOLNO_PRZEDSZK_WIELOPOLE': 'ZSz-P W.',
    'SZKOLA_MUZYCZNA_RYBNIK': 'PSM',
    'LICEUM_OGOLNOKSZT_NR_1_RYBNIK': 'ZS-1',
    'II_LO_RYBNIK_MIKOLOWSKA': 'ZS-2',
    'IV_LICEUM_OGOLNOKSZTALCACE_W_RYBNIKU': 'IV-LO',
    'SZKOLA_PODSTAWOWA_NR34_RYBNIK_REYMONTA': 'SP-34',
    'SZKOLA_PODSTAWOWA_NR_35_RYBNIK_SLASKA': 'SP-35',
    'URZAD_MIASTA_RYBNIK_SEK1': 'UM-S1',
    'URZAD_MIASTA_RYBNIK_SEK2': 'UM-S2',
    'URZAD_MIASTA_RYBNIK_ZAMKOWA': 'UM-Z',
    'ZESPOL_SZKOL_RYBNIK_SWIERKLANSKA': 'ZSB',
    }

def generate_dates_vertically(xwg, all_dates):
    col = 0
    xwg.sheet.col(0).best_fit = 1
    for nr, one_date in enumerate(all_dates):
        row = nr + 1
        xwg.zapisz_date(row, col, one_date)

def generate_hours_horizontally(xwg, all_hours):
    for nr, one_hour in enumerate(all_hours):
        row = 0
        col = nr + 1
        m_coor = to_kw.MergedCoords(row, col)
        xwg.write_single(m_coor, one_hour)

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

def normalize_value(before):
    if before == '':
        result = None
    else:
        result = before
    return result

class CommonRdWr(object):
    def __init__(self, tvk_pobor):
        '''
        CommonRdWr:
        '''
        self.krt_pobor = dd_kw.CechaEnergii(tvk_pobor)
        self.table_of_samples = self.krt_pobor.krt_table

    def set_pd_server(self, period_server):
        '''
        CommonRdWr:
        '''
        self.period_server = period_server

class CommonReader(CommonRdWr):
    def __init__(self, tvk_pobor):
        '''
        CommonReader:
        '''
        CommonRdWr.__init__(self, tvk_pobor)
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
        adjusted = normalize_value(value)
        self.internal_rows[local_key].update_for_index(sample_index, adjusted)

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
            my_sample_row.put_in_database(dfb, self.krt_pobor, self.table_of_samples, local_key)

    def generate_one_file(self, xwg, dfb, output_file):
        '''
        CommonReader:
        '''
        if rq_kw.TymczasowoTylkoJeden:
            id_obiekt = 11 # eo_kw.BT_SP3, ale w tabeli uu_
            my_year = 2013
            my_month = 6
            my_start_date, my_end_date = dn_kw.daty_skrajne_miesiaca(my_year, my_month, liczba_mies=1)
        else:
            id_obiekt = None
            my_start_date, my_end_date = None, None
        dane_bazy = le_kw.dq_load_from_db(
            dfb,
            self.table_of_samples,
            id_obiekt=id_obiekt,
            my_start_date=my_start_date,
            my_end_date=my_end_date,
            )
        object_names = unique_sorted(dane_bazy, lc_kw.fq_account_qv)
        xwg.workbook_create()
        for nr, name in enumerate(object_names):
            xwg.add_a_sheet(dict_names[name])
            selected_data = filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy)
            all_dates = unique_sorted(selected_data, lc_kw.fq_m_date_qv)
            all_hours = self.period_server.hours_for_header()
            generate_dates_vertically(xwg, all_dates)
            generate_hours_horizontally(xwg, all_hours)
            for my_data in selected_data:
                for sample_index, my_sample in enumerate(my_data[lc_kw.fq_m_samples_qv]):
                    row = all_dates.index(my_data[lc_kw.fq_m_date_qv]) + 1
                    col = sample_index + 1
                    m_coor = to_kw.MergedCoords(row, col)
                    xwg.zapisz_co_flt(m_coor, my_sample)
        xwg.workbook_save(output_file)

    def recalculate_statistics(self, dfb):
        '''
        CommonReader:
        '''
        obk = lr_kw.GeneratorUU(self.table_of_samples)
        db_statement = obk.samples_for_recalculating()
        self.all_results = dfb.query_dct(db_statement)
        for one_result in self.all_results:
            sample_key = one_result[lc_kw.fq_k_sample_qv]
            tmp_samples = one_result[lc_kw.fq_m_samples_qv]
            my_sample_row = lq_kw.SampleRow()
            my_sample_row.fill_from_data(sample_key, tmp_samples)
            my_sample_row.make_stats_of_samples(
                dfb, self.krt_pobor, self.table_of_samples, sample_key)

class CommonWriter(CommonRdWr):
    def __init__(self, tvk_pobor):
        '''
        CommonWriter:
        '''
        CommonRdWr.__init__(self, tvk_pobor)

    def generate_one_file(self, xwg, dfb, output_file):
        '''
        CommonWriter:
        '''
        if rq_kw.TymczasowoTylkoJeden:
            id_obiekt = 11 # eo_kw.BT_SP3, ale w tabeli uu_
            my_year = 2013
            my_month = 6
            my_start_date, my_end_date = dn_kw.daty_skrajne_miesiaca(my_year, my_month, liczba_mies=1)
        else:
            id_obiekt = None
            my_start_date, my_end_date = None, None
        dane_bazy = le_kw.dq_load_from_db(
            dfb,
            self.table_of_samples,
            id_obiekt=id_obiekt,
            my_start_date=my_start_date,
            my_end_date=my_end_date,
            )
        object_names = unique_sorted(dane_bazy, lc_kw.fq_account_qv)
        xwg.workbook_create()
        for nr, name in enumerate(object_names):
            xwg.add_a_sheet(dict_names[name])
            selected_data = filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy)
            all_dates = unique_sorted(selected_data, lc_kw.fq_m_date_qv)
            all_hours = self.period_server.hours_for_header()
            generate_dates_vertically(xwg, all_dates)
            generate_hours_horizontally(xwg, all_hours)
            for my_data in selected_data:
                for sample_index, my_sample in enumerate(my_data[lc_kw.fq_m_samples_qv]):
                    row = all_dates.index(my_data[lc_kw.fq_m_date_qv]) + 1
                    col = sample_index + 1
                    m_coor = to_kw.MergedCoords(row, col)
                    xwg.zapisz_co_flt(m_coor, my_sample)
        xwg.workbook_save(output_file)

class Test_Common_Reader(unittest.TestCase):
    def test_common_reader(self):
        '''
        Test_Common_Reader:
        '''
        self.assertEqual(normalize_value(''), None)
        self.assertEqual(normalize_value(0), 0)
