#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import to_kw
import hj_kw
import gu_kw
import rq_kw
import gb_kw
import dn_kw
import le_kw
import eo_kw
import tq_kw
import gx_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

napis_max = 'MAXIMUM'

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

def unique_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field], dane_bazy)))
    object_names.sort()
    return object_names

def wyznacz_dni_robocze(all_dates):
    oficjalne = []
    liczba_dat = len(all_dates)
    if all_dates:
        one_date = all_dates[0]
        nkd = dn_kw.napis_na_numer_dnia(str(one_date))
        dzien_tygodnia = dn_kw.DzienTygodnia(nkd)
        moj_poniedzialek = -dzien_tygodnia
        while moj_poniedzialek < liczba_dat:
            moj_piatek = moj_poniedzialek + 4
            if moj_poniedzialek < 0:
                moj_pierwszy = 0
            else:
                moj_pierwszy = moj_poniedzialek
            if moj_piatek >= liczba_dat - 1:
                moj_ostatni = liczba_dat - 1
            else:
                moj_ostatni = moj_piatek
            if moj_pierwszy <= moj_ostatni:
                oficjalne.append((moj_pierwszy, moj_ostatni))
            moj_poniedzialek += 7
    return oficjalne

CommonRdWr = tq_kw.CommonRdWr

class CommonWriter(CommonRdWr):
    def __init__(self, tvk_pobor, period_server):
        '''
        CommonWriter:
        '''
        CommonRdWr.__init__(self, tvk_pobor, period_server)
        self.liczba_max = 10
        self.first_weekday_column = 0
        self.first_date_column = self.first_weekday_column + 1
        self.first_sample_column = self.first_date_column + 1
        self.last_sample_column = self.first_sample_column + self.period_server.cnt_of_samples - 1
        self.horiz_max_column = self.last_sample_column + 1
        self.horiz_max_offset = self.horiz_max_column - self.first_sample_column
        self.week_max_column = self.horiz_max_column + 1
        self.second_date_column = self.week_max_column + 1
        self.second_weekday_column = self.second_date_column + 1
        self.nmax_start_col = 2
        self.col_for_moc_max = self.nmax_start_col + self.liczba_max

    def generate_for_a_day(self, xwg, all_dates, my_data, base_data_line, day_nr):
        '''
        CommonWriter:
        '''
        row = base_data_line + day_nr
        for sample_index, my_sample in enumerate(my_data[lc_kw.fq_m_samples_qv]):
            col = self.first_sample_column + sample_index
            m_coor = to_kw.MergedCoords(row, col)
            xwg.zapisz_co_flt(m_coor, my_sample)

    def generate_hours_horizontally(self, xwg, all_hours, first_line):
        '''
        CommonWriter:
        '''
        row = first_line
        for nr, one_hour in enumerate(all_hours):
            col = self.first_sample_column + nr
            m_coor = to_kw.MergedCoords(row, col)
            xwg.napis_ze_stylem(m_coor, one_hour, middle=1)

    def generate_dates_vertically(self, xwg, all_dates, base_data_line):
        '''
        CommonWriter:
        '''
        for nr, one_date in enumerate(all_dates):
            row = base_data_line + nr
            nkd = dn_kw.napis_na_numer_dnia(str(one_date))
            weekday_name = dn_kw.nazwa_dnia_tygodnia(nkd)
            xwg.napis_ze_wsp(row, self.first_weekday_column, weekday_name)
            xwg.zapisz_date(row, self.first_date_column, one_date)
            xwg.zapisz_date(row, self.second_date_column, one_date)
            xwg.napis_ze_wsp(row, self.second_weekday_column, weekday_name)

    def generate_summary(self, xwg, base_data_line, last_data_line, nmax_line, ndiff_line):
        '''
        CommonWriter:
        '''
        klm_a_ads = gu_kw.KolumnowyAdresator(base_data_line, self.first_sample_column)
        klm_b_ads = gu_kw.KolumnowyAdresator(last_data_line, self.last_sample_column)
        etk_a = klm_a_ads.get_ka_official_address()
        etk_b = klm_b_ads.get_ka_official_address()
        klm_c_ads = gu_kw.KolumnowyAdresator(nmax_line, self.nmax_start_col)
        row_c = nmax_line
        row_d = ndiff_line
        for i in xrange(self.liczba_max):
            tekst_wzoru = hj_kw.rcp_maxk(etk_a, etk_b, i)
            col = self.nmax_start_col + i
            m_coor = to_kw.MergedCoords(row_c, col)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)
            etk_c = klm_c_ads.get_ka_official_address(col_delta=i)
            tekst_wzoru = 'MAX(0,%s)' % etk_c
            m_coor = to_kw.MergedCoords(row_d, col)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)

    def generate_max_row(self, xwg, bottom_max_line, klm_ads):
        '''
        CommonWriter:
        '''
        xwg.napis_ze_wsp(bottom_max_line, self.first_date_column, napis_max)
        for i in klm_ads.col_iter():
            etk_a, etk_b = klm_ads.col_start_end_labels(i)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            m_coor = to_kw.MergedCoords(bottom_max_line, self.first_sample_column + i)
            xwg.zapisz_wzor(m_coor, tekst_wzoru)

    def generate_max_column(self, xwg, first_line, klm_ads):
        '''
        CommonWriter:
        '''
        xwg.napis_ze_wsp(first_line, self.horiz_max_column, napis_max)
        for i in klm_ads.row_iter(1):
            etk_a, etk_b = klm_ads.row_start_end_labels(i)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            row = klm_ads.get_only_row(row_delta=i)
            m_coor = to_kw.MergedCoords(row, self.horiz_max_column)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, kl_miejsc=2, size=None, bold=None)

    def generate_week_max_column(self, xwg, first_line, klm_ads, all_dates):
        '''
        CommonWriter:
        '''
        pary_robocze = wyznacz_dni_robocze(all_dates)
        xwg.napis_ze_wsp(first_line, self.week_max_column, 'Max tyg')
        for moj_pierwszy, moj_ostatni in pary_robocze:
            etk_a, etk_b = klm_ads.col_start_end_labels(col_offset=self.horiz_max_offset, moj_pierwszy=moj_pierwszy, moj_ostatni=moj_ostatni)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            row = klm_ads.get_only_row(row_delta=moj_ostatni)
            m_coor = to_kw.MergedCoords(row, self.week_max_column)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, kl_miejsc=2, size=None, bold=None)

    def generate_for_month(self, xwg, dane_bazy, nr_month, dost_wiersz):
        '''
        CommonWriter:
        '''
        if nr_month < 1:
            all_dates = unique_sorted(dane_bazy, lc_kw.fq_m_date_qv)
            all_hours = self.period_server.hours_for_header()
            first_line = dost_wiersz.zabierz_wiersze(len(all_dates) + 9)
            base_data_line = first_line + 1
            last_data_line = base_data_line + len(all_dates) - 1
            bottom_max_line = last_data_line + 1
            summary_label_line = bottom_max_line + 1
            summary_unit_line = summary_label_line + 1
            nmax_line = summary_unit_line + 1
            diff_label_line = nmax_line + 1
            diff_unit_line = diff_label_line + 1
            ndiff_line = diff_unit_line + 1
            klm_ads = gu_kw.KolumnowyAdresator(
                wiersz_bazowy_miesiecy=base_data_line,
                kl_assigned_col=self.first_sample_column,
                col_cnt=len(all_hours),
                row_cnt=len(all_dates),
                )
            self.generate_max_row(xwg, bottom_max_line, klm_ads)
            self.generate_dates_vertically(xwg, all_dates, base_data_line)
            self.generate_hours_horizontally(xwg, all_hours, first_line)
            for day_nr, my_data in enumerate(dane_bazy):
                self.generate_for_a_day(xwg, all_dates, my_data, base_data_line, day_nr)
            self.generate_summary(xwg, base_data_line, last_data_line, nmax_line, ndiff_line)
            the_a_style = xwg.get_or_generate_style(size=12, middle=1)
            the_b_style = xwg.get_or_generate_style(size=12, middle=1, wrap=1)
            xwg.zapisz_polaczone_komorki(summary_label_line, self.nmax_start_col, '%d największych poborów mocy w m-cu' % self.liczba_max, style=the_a_style, liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(summary_unit_line, self.nmax_start_col, gb_kw.tytul_kilowatow_przekroczenia, style=the_a_style,  liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(diff_label_line, self.nmax_start_col, 'przekroczenia mocy (jeśli liczba ujemna to 0,00)', style=the_a_style, liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(diff_unit_line, self.nmax_start_col, gb_kw.tytul_kilowatow_przekroczenia, style=the_a_style,  liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(summary_label_line, self.col_for_moc_max, 'Moc max', style=the_b_style)
            xwg.zapisz_polaczone_komorki(summary_label_line, self.col_for_moc_max + 1, 'Moc śred', style=the_b_style)
            xwg.zapisz_polaczone_komorki(summary_label_line, self.col_for_moc_max + 2, 'Moc min', style=the_b_style)
            xwg.zapisz_polaczone_komorki(summary_unit_line, self.col_for_moc_max, gb_kw.tytul_kilowatow_przekroczenia, style=the_b_style)
            xwg.zapisz_polaczone_komorki(summary_unit_line, self.col_for_moc_max + 1, gb_kw.tytul_kilowatow_przekroczenia, style=the_b_style)
            xwg.zapisz_polaczone_komorki(summary_unit_line, self.col_for_moc_max + 2, gb_kw.tytul_kilowatow_przekroczenia, style=the_b_style)
            self.generate_max_column(xwg, first_line, klm_ads)
            self.generate_week_max_column(xwg, first_line, klm_ads, all_dates)

    def setup_col_widths(self, xwg):
        '''
        CommonWriter:
        '''
        for col in xrange(self.first_weekday_column, self.second_weekday_column + 1):
            xwg.sheet.col(col).best_fit = 1

    def generate_for_object(self, xwg, dane_bazy, name):
        '''
        CommonWriter:
        '''
        dost_wiersz = gx_kw.Wierszownik(0)
        xwg.add_a_sheet(dict_names[name])
        self.setup_col_widths(xwg)
        selected_data = filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy)
        all_dates = unique_sorted(selected_data, lc_kw.fq_m_date_qv)
        month_dict = {}
        for one_data in selected_data:
            moj_rm = dn_kw.rok_mies_z_napisu(str(one_data[lc_kw.fq_m_date_qv]))
            if moj_rm not in month_dict:
                month_dict[moj_rm] = []
            month_dict[moj_rm].append(one_data)
        all_months = month_dict.keys()
        all_months.sort()
        for nr_month, moj_rm in enumerate(all_months):
            my_data = month_dict[moj_rm]
            self.generate_for_month(xwg, my_data, nr_month, dost_wiersz)

    def generate_one_file(self, xwg, dfb, output_file, slownik_mocy):
        '''
        CommonWriter:
        '''
        if rq_kw.TymczasowoTylkoJeden:
            id_obiekt = 11 # eo_kw.BT_SP3, ale w tabeli uu_
            my_year = 2013
            my_month = 6
            my_start_date, my_end_date = dn_kw.daty_skrajne_miesiaca(my_year, my_month, liczba_mies=2)
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
