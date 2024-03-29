#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import ciw_kw
import chj_kw
import ng_kw
import nf_kw
import lc_kw
import sf_kw
import gv_kw
import hj_kw
import gu_kw
import dn_kw
import le_kw
import la_kw
import tq_kw
import jc_kw

napis_max = 'MAXIMUM'


def info_brak_danych(output_file, id_obiekt, my_start_date, my_end_date):
    dane = []
    dane.append('Brak danych dla parametrów:\r\n')
    dane.append('basename: %s\r\n' % repr(os.path.basename(output_file)))
    dane.append('id_obiekt: %s\r\n' % repr(id_obiekt))
    dane.append('my_start_date: %s\r\n' % repr(my_start_date))
    dane.append('my_end_date: %s\r\n' % repr(my_end_date))
    full_text = ''.join(dane)
    sf_kw.zapisz_plik(output_file, full_text)


def unique_sorted(dane_bazy, field):
    object_names = list(set(ciw_kw.dict_ls_key_mapper(field, dane_bazy)))
    object_names.sort()
    return object_names


def dla_podanej_nazwy(dane_bazy, name):
    return list(filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy))


def wyznacz_slownik_miesiaca(selected_data):
    month_dict = {}
    for one_data in selected_data:
        moj_rm = dn_kw.rok_mies_z_napisu(str(one_data[lc_kw.fq_m_date_qv]))
        if moj_rm not in month_dict:
            month_dict[moj_rm] = []
        month_dict[moj_rm].append(one_data)
    all_months = list(month_dict.keys())
    all_months.sort()
    return month_dict, all_months


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


def weekend_style(jestem_weekend):
    if jestem_weekend:
        dc_style = dict(
            italic=1,
            fore_colour=gv_kw.ECR_light_turquoise,
            )
    else:
        dc_style = {}
    return dc_style


def weekend_b_style(jestem_weekend):
    if jestem_weekend:
        dc_style = dict(
            fore_colour=gv_kw.ECR_light_turquoise,
            )
    else:
        dc_style = {}
    return dc_style


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

    def generate_hours_horizontally(self, xwg, all_hours, first_line):
        '''
        CommonWriter:
        '''
        row = first_line
        for nr, one_hour in enumerate(all_hours):
            col = self.first_sample_column + nr
            xwg.zapisz_l_polaczone_komorki(
                row,
                col,
                one_hour,
                style_sel=ng_kw.NVB_2_STYLE,
                )

    def generate_dates_vertically(self, xwg, all_dates, base_data_line):
        '''
        CommonWriter:
        '''
        for nr, one_date in enumerate(all_dates):
            row = base_data_line + nr
            nkd = jc_kw.nr_of_day(one_date)
            jestem_weekend = jc_kw.wyznacz_weekend(nkd)
            dc_style = weekend_style(jestem_weekend)
            dc_b_style = weekend_b_style(jestem_weekend)
            weekday_name = dn_kw.nazwa_dnia_tygodnia(nkd)
            xwg.napis_ze_wsp(row, self.first_weekday_column, weekday_name, **dc_style)
            xwg.zapisz_date(row, self.first_date_column, one_date, **dc_b_style)
            xwg.zapisz_date(row, self.second_date_column, one_date, **dc_b_style)
            xwg.napis_ze_wsp(row, self.second_weekday_column, weekday_name, **dc_style)

    def generate_summary(self, xwg, nmax_line, ndiff_line, first_line, month_aggr):
        '''
        CommonWriter:
        '''
        klm_c_ads = gu_kw.KolumnowyAdresator(nmax_line, self.nmax_start_col, col_cnt=self.liczba_max)
        row_c = nmax_line
        row_d = ndiff_line
        row_e = row_d + 1
        row_f = row_e + 1
        etk_e = gu_kw.KolumnowyAdresator(first_line, self.first_date_column).get_ka_official_address()
        for i in range(self.liczba_max):
            hour_est = month_aggr.ordered_limited[i]
            col = self.nmax_start_col + i
            my_value = hour_est.one_sample
            xwg.zapisz_flt(row_c, col, my_value, kl_miejsc=2, size=12, borders=nf_kw.brd_1_obk)
            etk_c = klm_c_ads.get_ka_official_address(col_delta=i)
            tekst_wzoru = hj_kw.rcp_diff_max(etk_c, etk_e)
            xwg.zapisz_wzor(row_d, col, tekst_wzoru, kl_miejsc=2, size=12, borders=nf_kw.brd_1_obk)
            ##############################################################################
            one_date = hour_est.one_date
            xwg.zapisz_date(row_e, col, one_date)
            ##############################################################################
            my_hhmm = hour_est.get_hhmm()
            xwg.napis_ze_wsp(row_f, col, my_hhmm, middle=1)
            ##############################################################################
        etk_f, etk_g = klm_c_ads.row_start_end_labels()
        tekst_wzoru = hj_kw.rcp_emax(etk_f, etk_g)
        xwg.zapisz_wzor(row_c, self.col_for_moc_max, tekst_wzoru, kl_miejsc=2, bold=1, size=12, borders=nf_kw.brd_1_obk)
        tekst_wzoru = hj_kw.rcp_sred(etk_f, etk_g)
        xwg.zapisz_wzor(row_c, self.col_for_moc_max + 1, tekst_wzoru, kl_miejsc=2, size=12, borders=nf_kw.brd_1_obk)
        tekst_wzoru = hj_kw.rcp_emin(etk_f, etk_g)
        xwg.zapisz_wzor(row_c, self.col_for_moc_max + 2, tekst_wzoru, kl_miejsc=2, size=12, borders=nf_kw.brd_1_obk)
        etk_h, etk_i = klm_c_ads.row_start_end_labels(ndiff_line - nmax_line)
        tekst_wzoru = hj_kw.rcp_poziom(etk_h, etk_i)
        xwg.zapisz_wzor(ndiff_line, self.col_for_moc_max, tekst_wzoru, kl_miejsc=2, size=12, borders=nf_kw.brd_1_obk)

    def generate_max_row(self, xwg, bottom_max_line, klm_ads):
        '''
        CommonWriter:
        '''
        xwg.napis_ze_wsp(bottom_max_line, self.first_date_column, napis_max, rn_colour=gv_kw.ECR_red)
        for i in klm_ads.col_iter():
            etk_a, etk_b = klm_ads.col_start_end_labels(i)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            xwg.zapisz_wzor(bottom_max_line, self.first_sample_column + i, tekst_wzoru, kl_miejsc=2, rn_colour=gv_kw.ECR_red)

    def generate_max_column(self, xwg, first_line, klm_ads):
        '''
        CommonWriter:
        '''
        xwg.napis_ze_wsp(first_line, self.horiz_max_column, napis_max, rn_colour=gv_kw.ECR_red)
        for i in klm_ads.row_iter(1):
            etk_a, etk_b = klm_ads.row_start_end_labels(i)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            row = klm_ads.get_only_row(row_delta=i)
            xwg.zapisz_wzor(row, self.horiz_max_column, tekst_wzoru, kl_miejsc=2, rn_colour=gv_kw.ECR_red)

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
            xwg.zapisz_wzor(row, self.week_max_column, tekst_wzoru, kl_miejsc=2, bold=None, size=None)

    def wpisz_wartosc_mocy_umownej(self, xwg, first_line, moc_umowna):
        '''
        CommonWriter:
        '''
        xwg.zapisz_flt(first_line, self.first_date_column, moc_umowna, kl_miejsc=0, rn_colour=gv_kw.ECR_red, bold=1)
        klm_ads = gu_kw.KolumnowyAdresator(first_line, self.first_date_column)
        tekst_wzoru = klm_ads.get_ka_official_address()
        xwg.zapisz_wzor(first_line, self.second_date_column, tekst_wzoru, kl_miejsc=0, rn_colour=gv_kw.ECR_red, bold=1, size=None)

    def setup_col_widths(self, xwg):
        '''
        CommonWriter:
        '''
        for col in range(self.first_weekday_column, self.second_weekday_column + 1):
            xwg.sheet.col(col).best_fit = 1

    def write_real_data(self, output_file, uu_maper, dane_bazy):
        '''
        CommonWriter:
        '''
        object_names = unique_sorted(dane_bazy, lc_kw.fq_account_qv)
        xwg = la_kw.workbook_a_create()
        for nr, name in enumerate(object_names):
            self.generate_for_object(xwg, dane_bazy, name, uu_maper)
        xwg.workbook_save(output_file)

    def generate_one_file(self, dfb, output_file, uu_maper, choosen_year, id_obiekt=None):
        '''
        CommonWriter:
        '''
        if choosen_year is None:
            my_start_date = None
            my_end_date = None
        else:
            my_start_date = chj_kw.tq_poczatek_roku(choosen_year)
            my_end_date = chj_kw.tq_poczatek_roku(choosen_year + 1)
        dane_bazy = le_kw.dq_load_from_db(
            dfb,
            self.table_of_samples,
            id_obiekt=id_obiekt,
            my_start_date=my_start_date,
            my_end_date=my_end_date,
            )
        if dane_bazy:
            self.write_real_data(output_file, uu_maper, dane_bazy)
        else:
            info_brak_danych(output_file, id_obiekt, my_start_date, my_end_date)
