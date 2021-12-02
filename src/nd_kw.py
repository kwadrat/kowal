#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ng_kw
import gv_kw
import hj_kw
import gu_kw
import en_kw

row_offset_column_name = -1
row_offset_invoice_mark = 0
row_offset_vertical_sum = 13


class OgOpOgolnaKolumna(object):
    def __init__(self, wiersz_bazowy_miesiecy=None, kl_pion=0, kl_db_label=None, kl_miejsc=2):
        '''
        OgOpOgolnaKolumna:
        '''
        if wiersz_bazowy_miesiecy is not None:
            self.wiersz_bazowy_miesiecy = wiersz_bazowy_miesiecy
        self.qj_napisy = {}
        self.qj_szerokie1_napisy = {}
        self.qj_szerokie3_napisy = {}
        self.qj_centrowane_num_tytuly = {}
        self.qj_liczby = {}
        self.qj_napisy_12_bold = {}
        self.qj_wzory = {}
        self.kl_skladnik = None
        self.kl_suma = None
        self.kl_assigned_col = None
        self.kl_pion = kl_pion
        self.kl_db_label = kl_db_label
        self.kl_miejsc = kl_miejsc
        self.vz_transfer_flag = 0

    def assign_target_column(self, kl_assigned_col):
        '''
        OgOpOgolnaKolumna:
        '''
        self.kl_assigned_col = kl_assigned_col

    def qj_set_wide1_label(self, fvk_miesiac, tmp_value, liczba_kolumn=1, liczba_wierszy=1):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_szerokie1_napisy[fvk_miesiac] = (tmp_value, liczba_kolumn, liczba_wierszy)

    def ustaw_opis_litery(self, opis_pod_kolumna):
        '''
        OgOpOgolnaKolumna:
        '''
        if opis_pod_kolumna is not None:
            self.qj_set_wide1_label(row_offset_invoice_mark, opis_pod_kolumna)

    def ustaw_zawijany_tytul(self, sam_tekst, fvk_miesiac=row_offset_column_name, liczba_wierszy=1):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_set_wide1_label(fvk_miesiac, sam_tekst, liczba_wierszy=liczba_wierszy)

    def ustaw_wzor(self, fvk_miesiac, tekst_wzoru, kl_miejsc=None, liczba_kolumn=1, size=None, bold=None, fore_colour=None):
        '''
        OgOpOgolnaKolumna:
        '''
        if kl_miejsc is None:
            moich_miejsc = self.kl_miejsc
        else:
            moich_miejsc = kl_miejsc
        self.qj_wzory[fvk_miesiac] = (tekst_wzoru, moich_miejsc, liczba_kolumn, size, bold, fore_colour)

    def ustaw_bold_12pt_wzor(self, fvk_miesiac, tekst_wzoru):
        '''
        OgOpOgolnaKolumna:
        '''
        self.ustaw_wzor(fvk_miesiac, tekst_wzoru, size=12, bold=1)

    def ustaw_sumaryczne_bold_12pt_wzor(self, fvk_miesiac, tekst_wzoru):
        '''
        OgOpOgolnaKolumna:
        '''
        if fvk_miesiac == row_offset_vertical_sum:
            self.ustaw_bold_12pt_wzor(fvk_miesiac, tekst_wzoru)
        else:
            self.ustaw_wzor(fvk_miesiac, tekst_wzoru)

    def add_vertical_sum(self, wiersz_bazowy_miesiecy):
        '''
        OgOpOgolnaKolumna:
        '''
        if self.kl_pion:
            klm_ads = gu_kw.KolumnowyAdresator(kl_assigned_col=self.kl_assigned_col)
            tekst_wzoru = hj_kw.rcp_pion(wiersz_bazowy_miesiecy, klm_ads.get_col_letter())
            self.ustaw_bold_12pt_wzor(row_offset_vertical_sum, tekst_wzoru)

    def qj_set_direct(self, fvk_miesiac, tmp_value, liczba_kolumn=1):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_napisy[fvk_miesiac] = (tmp_value, liczba_kolumn)

    def qj_write_12_bold(self, fvk_miesiac, tmp_value):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_napisy_12_bold[fvk_miesiac] = tmp_value

    def qj_set_wide_label(self, fvk_miesiac, tmp_value, liczba_kolumn=1):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_napisy[fvk_miesiac] = (tmp_value, liczba_kolumn)

    def qj_set_wide3_label(self, fvk_miesiac, tmp_value, liczba_kolumn):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_szerokie3_napisy[fvk_miesiac] = (tmp_value, liczba_kolumn)

    def qj_set_centered_num_title(self, fvk_miesiac, tmp_value, liczba_kolumn):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_centrowane_num_tytuly[fvk_miesiac] = (tmp_value, liczba_kolumn)

    def qj_set_centered_title(self, fvk_miesiac, tmp_value, liczba_kolumn):
        '''
        OgOpOgolnaKolumna:
        '''
        the_content = en_kw.utf_to_unicode(tmp_value)
        self.qj_set_centered_num_title(fvk_miesiac, the_content, liczba_kolumn)

    def qj_set_a_flt(self, fvk_miesiac, rn_liczba):
        '''
        OgOpOgolnaKolumna:
        '''
        rn_liczba.update_after(self.kl_miejsc)
        self.qj_liczby[fvk_miesiac] = rn_liczba

    def qj_set_cent_int(self, fvk_miesiac, the_content):
        '''
        OgOpOgolnaKolumna:
        '''
        self.qj_set_centered_num_title(fvk_miesiac, the_content, 1)

    def wprowadz_jako_zwykla_sume(self, dane_dla_miesiaca):
        '''
        OgOpOgolnaKolumna:
        '''
        for fvk_miesiac, dane_jednego_miesiaca in dane_dla_miesiaca.iteritems():
            moja_suma = dane_jednego_miesiaca.wyznacz_rn_sume_faktur(self.kl_db_label)
            self.qj_set_a_flt(fvk_miesiac, moja_suma)

    def wprowadz_do_kolumny(self, fvk_miesiac, dane_faktury):
        '''
        OgOpOgolnaKolumna:
        '''
        if self.kl_db_label is not None:
            tmp_value = dane_faktury[self.kl_db_label]
            self.qj_liczby[fvk_miesiac] = gv_kw.RichNumber(tmp_value, rn_after=self.kl_miejsc)

    def podaj_adresator(self):
        '''
        OgOpOgolnaKolumna:
        '''
        klm_ads = gu_kw.KolumnowyAdresator(wiersz_bazowy_miesiecy=self.wiersz_bazowy_miesiecy, kl_assigned_col=self.kl_assigned_col)
        return klm_ads

    def pobierz_adres_wspolczynnika(self, fvk_miesiac):
        '''
        OgOpOgolnaKolumna:
        '''
        klm_ads = self.podaj_adresator()
        return klm_ads.get_ka_official_address(fvk_miesiac)

    def ustaw_umowne_wzory(self, klm_a_ads, mies_pocz, mies_kon, etykieta_mnoznika):
        '''
        OgOpOgolnaKolumna:
        '''
        for fvk_miesiac in xrange(mies_pocz, mies_kon + 1):
            etykieta_zamowionej = klm_a_ads.get_ka_official_address(fvk_miesiac)
            wzor = hj_kw.rcp_mnoz(etykieta_zamowionej, etykieta_mnoznika)
            self.ustaw_wzor(fvk_miesiac, wzor)

    def przepisz_poprzednie(self, klm_a_ads, klm_b_ads, mies_pocz, mies_kon, sfv_wiersz):
        '''
        OgOpOgolnaKolumna:
        '''
        etykieta_mnoznika = klm_b_ads.get_ka_official_address(sfv_wiersz)
        self.ustaw_umowne_wzory(klm_a_ads, mies_pocz, mies_kon, etykieta_mnoznika)

    def przepisz_kolumne_do_arkusza(self, xwg, wiersz_bazowy_miesiecy):
        '''
        OgOpOgolnaKolumna:
        '''
        nr_kol = self.kl_assigned_col
        for wiersz_przesuniecie, (tresc_napisu, liczba_kolumn) in self.qj_napisy.iteritems():
            xwg.zapisz_l_polaczone_komorki(
                wiersz_bazowy_miesiecy + wiersz_przesuniecie,
                nr_kol,
                tresc_napisu,
                style_sel=None,
                liczba_kolumn=liczba_kolumn,
                )
        for wiersz_przesuniecie, (tresc_napisu, liczba_kolumn, liczba_wierszy) in self.qj_szerokie1_napisy.iteritems():
            xwg.zapisz_zawijany_center(
                wiersz_bazowy_miesiecy + wiersz_przesuniecie,
                nr_kol,
                tresc_napisu,
                liczba_kolumn=liczba_kolumn,
                liczba_wierszy=liczba_wierszy,
                )
        for wiersz_przesuniecie, (tresc_napisu, liczba_kolumn) in self.qj_szerokie3_napisy.iteritems():
            xwg.zapisz_l_polaczone_komorki(
                wiersz_bazowy_miesiecy + wiersz_przesuniecie,
                nr_kol,
                tresc_napisu,
                style_sel=ng_kw.NVB_19_STYLE,
                liczba_kolumn=liczba_kolumn,
                )
        for wiersz_przesuniecie, rn_liczba in self.qj_liczby.iteritems():
            xwg.zapisz_rn_flt(wiersz_bazowy_miesiecy + wiersz_przesuniecie, nr_kol, rn_liczba)
        for wiersz_przesuniecie, tresc_napisu in self.qj_napisy_12_bold.iteritems():
            xwg.zapisz_bold_rozmiar_12_komorki(
                wiersz_bazowy_miesiecy + wiersz_przesuniecie,
                nr_kol,
                tresc_napisu,
                )
        for wiersz_przesuniecie, (tekst_wzoru, kl_miejsc, liczba_kolumn, size, bold, fore_colour) in self.qj_wzory.iteritems():
            xwg.zapisz_wzor(
                wiersz_bazowy_miesiecy + wiersz_przesuniecie,
                nr_kol,
                tekst_wzoru,
                kl_miejsc=kl_miejsc,
                bold=bold,
                size=size,
                liczba_kolumn=liczba_kolumn,
                fore_colour=fore_colour,
                )
        for wiersz_przesuniecie, (the_content, liczba_kolumn) in self.qj_centrowane_num_tytuly.iteritems():
            xwg.zapisz_lu_polaczone_komorki(
                wiersz_bazowy_miesiecy + wiersz_przesuniecie,
                nr_kol,
                the_content,
                style_sel=ng_kw.NVB_7_STYLE,
                liczba_kolumn=liczba_kolumn,
                )
