#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import to_kw
import gu_kw
import lm_kw
import gb_kw
import jj_kw
import ja_kw
import lw_kw
import gx_kw
import jc_kw
import nc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

CommonWriter = nc_kw.CommonWriter

class PowerWriter(CommonWriter):
    def __init__(self):
        '''
        PowerWriter:
        '''
        period_server = jj_kw.QuarterServer()
        CommonWriter.__init__(self, lw_kw.Dn_Power, period_server)

    def generate_for_a_day(self, xwg, my_data, base_data_line, day_nr, moc_um_dec):
        '''
        PowerWriter:
        '''
        row = base_data_line + day_nr
        nkd = jc_kw.nr_of_day(my_data[lc_kw.fq_m_date_qv])
        jestem_weekend = jc_kw.wyznacz_weekend(nkd)
        samples_in_order = my_data[lc_kw.fq_m_samples_qv][:]
        samples_in_order.sort()
        ten_treshold = samples_in_order[-10]
        for sample_index, my_sample in enumerate(my_data[lc_kw.fq_m_samples_qv]):
            col = self.first_sample_column + sample_index
            m_coor = to_kw.MergedCoords(row, col)
            dc_b_style = jc_kw.obtain_cell_color(moc_um_dec, ten_treshold, jestem_weekend, my_sample)
            xwg.zapisz_co_flt(m_coor, my_sample, **dc_b_style)

    def generate_for_month(self, xwg, dane_bazy, nr_month, dost_wiersz, moc_umowna):
        '''
        PowerWriter:
        '''
        if nc_kw.month_enabled(nr_month):
            all_dates = nc_kw.unique_sorted(dane_bazy, lc_kw.fq_m_date_qv)
            all_hours = self.period_server.time_for_header
            first_line = dost_wiersz.zabierz_wiersze(len(all_dates) + 11)
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
            if moc_umowna is None:
                moc_um_dec = lm_kw.wartosc_zero_globalna
            else:
                moc_um_dec = lm_kw.a2d(lm_kw.rzeczywista_na_napis(moc_umowna))
            month_aggr = ja_kw.MonthSummary()
            for day_nr, my_data in enumerate(dane_bazy):
                self.generate_for_a_day(xwg, my_data, base_data_line, day_nr, moc_um_dec)
                month_aggr.add_day_samples(my_data)
            month_aggr.prepare_top_values(self.liczba_max)
            self.generate_summary(xwg, nmax_line, ndiff_line, first_line, month_aggr)
            xwg.zapisz_l_polaczone_komorki(summary_label_line, self.nmax_start_col, '%d największych poborów mocy w m-cu' % self.liczba_max, style_sel=ng_kw.NVB_16_STYLE, liczba_kolumn=self.liczba_max)
            xwg.zapisz_l_polaczone_komorki(summary_unit_line, self.nmax_start_col, gb_kw.tytul_kilowatow_przekroczenia, style_sel=ng_kw.NVB_16_STYLE, liczba_kolumn=self.liczba_max)
            xwg.zapisz_l_polaczone_komorki(diff_label_line, self.nmax_start_col, 'przekroczenia mocy (jeśli liczba ujemna to 0,00)', style_sel=ng_kw.NVB_16_STYLE, liczba_kolumn=self.liczba_max)
            xwg.zapisz_l_polaczone_komorki(diff_label_line, self.col_for_moc_max, 'Suma przekr', style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(diff_unit_line, self.col_for_moc_max, gb_kw.tytul_kilowatow_przekroczenia, style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(diff_unit_line, self.nmax_start_col, gb_kw.tytul_kilowatow_przekroczenia, style_sel=ng_kw.NVB_16_STYLE, liczba_kolumn=self.liczba_max)
            xwg.zapisz_l_polaczone_komorki(summary_label_line, self.col_for_moc_max, 'Moc max', style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(summary_label_line, self.col_for_moc_max + 1, 'Moc śred', style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(summary_label_line, self.col_for_moc_max + 2, 'Moc min', style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(summary_unit_line, self.col_for_moc_max, gb_kw.tytul_kilowatow_przekroczenia, style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(summary_unit_line, self.col_for_moc_max + 1, gb_kw.tytul_kilowatow_przekroczenia, style_sel=ng_kw.NVB_17_STYLE)
            xwg.zapisz_l_polaczone_komorki(summary_unit_line, self.col_for_moc_max + 2, gb_kw.tytul_kilowatow_przekroczenia, style_sel=ng_kw.NVB_17_STYLE)
            self.generate_max_column(xwg, first_line, klm_ads)
            self.generate_week_max_column(xwg, first_line, klm_ads, all_dates)

    def generate_for_object(self, xwg, dane_bazy, name, uu_maper):
        '''
        PowerWriter:
        '''
        dost_wiersz = gx_kw.Wierszownik(0)
        nr_uu = uu_maper.get_my_nr(name)
        xwg.add_a_sheet(uu_maper.get_short_name(name))
        self.setup_col_widths(xwg)
        selected_data = nc_kw.dla_podanej_nazwy(dane_bazy, name)
        month_dict, all_months = nc_kw.wyznacz_slownik_miesiaca(selected_data)
        for nr_month, moj_rm in enumerate(all_months):
            my_data = month_dict[moj_rm]
            if uu_maper:
                moc_umowna = uu_maper.pobierz_umowna_moc(nr_uu, moj_rm)
            else:
                moc_umowna = 0
            self.generate_for_month(xwg, my_data, nr_month, dost_wiersz, moc_umowna)

class TestWritingPower(unittest.TestCase):
    def test_writing_power(self):
        '''
        TestWritingPower:
        '''
        obk = PowerWriter()
        self.assertEqual(obk.first_weekday_column, 0)
        self.assertEqual(obk.first_date_column, 1)
        self.assertEqual(obk.first_sample_column, 2)
        self.assertEqual(obk.last_sample_column, 97)
        self.assertEqual(obk.horiz_max_column, 98)
        self.assertEqual(obk.horiz_max_offset, 96)
        self.assertEqual(obk.week_max_column, 99)
        self.assertEqual(obk.second_date_column, 100)
        self.assertEqual(obk.second_weekday_column, 101)
