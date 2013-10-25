#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import to_kw
import rq_kw
import dn_kw
import le_kw
import eo_kw
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

def unique_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field], dane_bazy)))
    object_names.sort()
    return object_names

CommonRdWr = tq_kw.CommonRdWr

class CommonWriter(CommonRdWr):
    def __init__(self, tvk_pobor, period_server):
        '''
        CommonWriter:
        '''
        CommonRdWr.__init__(self, tvk_pobor, period_server)
        self.first_weekday_column = 0
        self.first_date_column = self.first_weekday_column + 1
        self.first_sample_column = self.first_date_column + 1

    def generate_for_a_day(self, xwg, all_dates, my_data):
        '''
        CommonWriter:
        '''
        row = all_dates.index(my_data[lc_kw.fq_m_date_qv]) + 1
        for sample_index, my_sample in enumerate(my_data[lc_kw.fq_m_samples_qv]):
            col = sample_index + 1
            m_coor = to_kw.MergedCoords(row, col)
            xwg.zapisz_co_flt(m_coor, my_sample)

    def generate_hours_horizontally(self, xwg, all_hours):
        '''
        CommonWriter:
        '''
        for nr, one_hour in enumerate(all_hours):
            row = 0
            col = nr + 1
            m_coor = to_kw.MergedCoords(row, col)
            xwg.write_single(m_coor, one_hour)

    def generate_for_object(self, xwg, dane_bazy, name):
        '''
        CommonWriter:
        '''
        xwg.add_a_sheet(dict_names[name])
        selected_data = filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy)
        all_dates = unique_sorted(selected_data, lc_kw.fq_m_date_qv)
        all_hours = self.period_server.hours_for_header()
        generate_dates_vertically(xwg, all_dates)
        self.generate_hours_horizontally(xwg, all_hours)
        for my_data in selected_data:
            self.generate_for_a_day(xwg, all_dates, my_data)

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
            self.generate_for_object(xwg, dane_bazy, name)
        xwg.workbook_save(output_file)
