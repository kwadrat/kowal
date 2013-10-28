#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import to_kw
import gv_kw
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

    def b1_coor(self, first_line):
        '''
        CommonWriter:
        '''
        m_coor = to_kw.MergedCoords(first_line, self.first_date_column)
        return m_coor

    def generate_summary(self, xwg, base_data_line, last_data_line, nmax_line, ndiff_line, first_line):
        '''
        CommonWriter:
        '''
        klm_a_ads = gu_kw.KolumnowyAdresator(base_data_line, self.first_sample_column)
        klm_b_ads = gu_kw.KolumnowyAdresator(last_data_line, self.last_sample_column)
        etk_a = klm_a_ads.get_ka_official_address()
        etk_b = klm_b_ads.get_ka_official_address()
        klm_c_ads = gu_kw.KolumnowyAdresator(nmax_line, self.nmax_start_col, col_cnt=self.liczba_max)
        row_c = nmax_line
        row_d = ndiff_line
        m_coor = self.b1_coor(first_line)
        etk_e = gu_kw.KolumnowyAdresator(*m_coor.wyznacz_dwa()).get_ka_official_address()
        for i in xrange(self.liczba_max):
            tekst_wzoru = hj_kw.rcp_maxk(etk_a, etk_b, i)
            col = self.nmax_start_col + i
            m_coor = to_kw.MergedCoords(row_c, col)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)
            etk_c = klm_c_ads.get_ka_official_address(col_delta=i)
            tekst_wzoru = 'MAX(0,%s-%s)' % (etk_c, etk_e)
            m_coor = to_kw.MergedCoords(row_d, col)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)
        etk_f, etk_g = klm_c_ads.row_start_end_labels()
        tekst_wzoru = hj_kw.rcp_emax(etk_f, etk_g)
        m_coor = to_kw.MergedCoords(row_c, self.col_for_moc_max)
        xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12, bold=1)
        tekst_wzoru = hj_kw.rcp_sred(etk_f, etk_g)
        m_coor = to_kw.MergedCoords(row_c, self.col_for_moc_max + 1)
        xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)
        tekst_wzoru = hj_kw.rcp_emin(etk_f, etk_g)
        m_coor = to_kw.MergedCoords(row_c, self.col_for_moc_max + 2)
        xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)
        etk_h, etk_i = klm_c_ads.row_start_end_labels(ndiff_line - nmax_line)
        tekst_wzoru = hj_kw.rcp_poziom(etk_h, etk_i)
        m_coor = to_kw.MergedCoords(ndiff_line, self.col_for_moc_max)
        xwg.zapisz_wzor(m_coor, tekst_wzoru, size=12)

    def generate_max_row(self, xwg, bottom_max_line, klm_ads):
        '''
        CommonWriter:
        '''
        xwg.napis_ze_wsp(bottom_max_line, self.first_date_column, napis_max, rn_colour=gv_kw.ECR_red)
        for i in klm_ads.col_iter():
            etk_a, etk_b = klm_ads.col_start_end_labels(i)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            m_coor = to_kw.MergedCoords(bottom_max_line, self.first_sample_column + i)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, rn_colour=gv_kw.ECR_red)

    def generate_max_column(self, xwg, first_line, klm_ads):
        '''
        CommonWriter:
        '''
        xwg.napis_ze_wsp(first_line, self.horiz_max_column, napis_max, rn_colour=gv_kw.ECR_red)
        for i in klm_ads.row_iter(1):
            etk_a, etk_b = klm_ads.row_start_end_labels(i)
            tekst_wzoru = hj_kw.rcp_emax(etk_a, etk_b)
            row = klm_ads.get_only_row(row_delta=i)
            m_coor = to_kw.MergedCoords(row, self.horiz_max_column)
            xwg.zapisz_wzor(m_coor, tekst_wzoru, rn_colour=gv_kw.ECR_red)

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

    def wpisz_wartosc_mocy_umownej(self, xwg, first_line, moc_umowna):
        '''
        CommonWriter:
        '''
        m_coor = self.b1_coor(first_line)
        xwg.zapisz_co_flt(m_coor, moc_umowna, kl_miejsc=0, bold=1, rn_colour=gv_kw.ECR_red)
        klm_ads = gu_kw.KolumnowyAdresator(first_line, self.first_date_column)
        tekst_wzoru = klm_ads.get_ka_official_address()
        m_coor = to_kw.MergedCoords(first_line, self.second_date_column)
        xwg.zapisz_wzor(m_coor, tekst_wzoru, kl_miejsc=0, size=None, bold=1, rn_colour=gv_kw.ECR_red)

    def generate_for_month(self, xwg, dane_bazy, nr_month, dost_wiersz, moc_umowna):
        '''
        CommonWriter:
        '''
        if 0 or nr_month < 1:
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
            self.wpisz_wartosc_mocy_umownej(xwg, first_line, moc_umowna)
            for day_nr, my_data in enumerate(dane_bazy):
                self.generate_for_a_day(xwg, all_dates, my_data, base_data_line, day_nr)
            self.generate_summary(xwg, base_data_line, last_data_line, nmax_line, ndiff_line, first_line)
            the_a_style = xwg.get_or_generate_style(size=12, middle=1)
            the_b_style = xwg.get_or_generate_style(size=12, middle=1, wrap=1)
            xwg.zapisz_polaczone_komorki(summary_label_line, self.nmax_start_col, '%d największych poborów mocy w m-cu' % self.liczba_max, style=the_a_style, liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(summary_unit_line, self.nmax_start_col, gb_kw.tytul_kilowatow_przekroczenia, style=the_a_style,  liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(diff_label_line, self.nmax_start_col, 'przekroczenia mocy (jeśli liczba ujemna to 0,00)', style=the_a_style, liczba_kolumn=self.liczba_max)
            xwg.zapisz_polaczone_komorki(diff_label_line, self.col_for_moc_max, 'Suma przekr', style=the_b_style)
            xwg.zapisz_polaczone_komorki(diff_unit_line, self.col_for_moc_max, gb_kw.tytul_kilowatow_przekroczenia, style=the_b_style)
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

    def generate_for_object(self, xwg, dane_bazy, name, uu_maper):
        '''
        CommonWriter:
        '''
        dost_wiersz = gx_kw.Wierszownik(0)
        nr_uu = uu_maper.get_my_nr(name)
        xwg.add_a_sheet(uu_maper.get_short_name(name))
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
            if uu_maper:
                moc_umowna = uu_maper.pobierz_umowna_moc(nr_uu, moj_rm)
            else:
                moc_umowna = 0
            self.generate_for_month(xwg, my_data, nr_month, dost_wiersz, moc_umowna)

    def generate_one_file(self, xwg, dfb, output_file, uu_maper):
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
            self.generate_for_object(xwg, dane_bazy, name, uu_maper)
        xwg.workbook_save(output_file)
