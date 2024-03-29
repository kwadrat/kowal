#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lc_kw

PrawaDostepuPliku = 0o777
CHC_NO = 0
CHC_YES = 1
LITERA_SLUPEK = 's'
LITERA_PASEK = 'p'
LITERA_WYKRES = 'w'
KLD_CIEMNY = 0
KLD_JASNY = 1
EtykietaLP = 'L.p.'  # Liczba porządkowa
rjb_sam_slsh = '/'
RDZ_Audyt = rjb_sam_slsh + lc_kw.fq_kaud_qv
RDZ_Inwentaryzacja = rjb_sam_slsh + lc_kw.fq_kinw_qv
RDZ_Zdjecia = rjb_sam_slsh + lc_kw.fq_kzdj_qv
RDZ_Oswietlenie = '/kosw'
LTR_GLR_STAMP = 'stamp'
LTR_GLR_SMALL = 'small'
CHC_PIC_NON = 0  # to nie zdjęcie
CHC_PIC_ORYG = 1  # oryginał zdjęcia
CHC_PIC_STAMP = 2  # miniaturka zdjęcia
CHC_PIC_SMALL = 3  # zdjęcie standardowe
# Rozmiary dla pomniejszanych obrazków
LTR_GLR_X_SMALL = 1024  # Format 4/3
LTR_GLR_X_STAMP = 150  # Mniej więcej format 4/3
CHC_FL = 0  # ścieżka pliku
CHC_UR = 1  # ścieżka URL
KEY_ROZMIAR = 'rozmiar'
KEY_DODANY_PRZEZ = 'dodany_przez'
KEY_ZAZNACZ = 'zaznacz'
LTR_CHBOX_ID_WPISU = 'p_zaznacz_to_'
LTR_CHBOX_SUFFIX_PLIK = 'moj_plik'
LTR_CHBOX_SUFFIX_KATALOG = 'moj_katalog'
LTR_FORM_EDYCJA_NAZWY = 'p_zmieniam_nazwe_'
LTR_PRAWO_DO_EDYCJI = 'prawo_do_edycji'
LTR_DLA_ZAZNACZONYCH = 'dla_zaznaczonych'
LTR_ZAZN_NIC = 'zazn_nic'
LTR_ZAZN_ZMIEN = 'zazn_zmien'
LTR_ZAZN_USUN = 'zazn_usun'
LTR_JESZCZE_CHCEMY_GLOWNY_KATALOG = 1
LTR_FORM_BIEZACY_KATALOG = 'nazwa_biezacego1'
LTR_FORM_BIEZACY_ID_KATALOG = 'id_biez'
LTR_FORM_PLIK_DO_ZALADOWANIA = 'nazwa_pliku1'
LTR_FORM_NAZWA_NOWEGO_KATALOGU = 'nazwa_katalogu1'
LTR_KLUCZ_WLACZONY = '1'  # Do kasowania danych
LTR_KLUCZ_ZABLOKOWANY = '0'  # Do kasowania danych

wyznacz_wielkosc = {
    CHC_PIC_ORYG: lc_kw.fq_oryg_qv,
    CHC_PIC_STAMP: LTR_GLR_STAMP,
    CHC_PIC_SMALL: LTR_GLR_SMALL,
    }

wyznacz_opis_akcji = {
    LTR_ZAZN_NIC: 'Nic nie rób',
    LTR_ZAZN_ZMIEN: 'Zmień nazwę',
    LTR_ZAZN_USUN: 'Usuń',
    }


def formatuj_pelne_in(adresat):
    return '%(imie)s %(nazwisko)s' % adresat


def ladny_rozmiar(ile, exp=3):
    if ile < 2 * 1024 or exp <= 0:
        return "%d B" % ile
    elif ile < 2 * 1024 * 1024 or exp == 1:
        return "%d KB" % (ile // 1024)
    elif ile < 2 * 1024 * 1024 * 1024 or exp == 2:
        return "%d MB" % (ile // 1024 // 1024)
    else:
        return "%d GB" % (ile // 1024 // 1024 // 1024)


class TestSomeConstants(unittest.TestCase):
    def test_opisow_akcji(self):
        '''
        TestSomeConstants:
        '''
        self.assertEqual(wyznacz_opis_akcji[LTR_ZAZN_NIC], 'Nic nie rób')
        self.assertEqual(wyznacz_opis_akcji[LTR_ZAZN_ZMIEN], 'Zmień nazwę')
        self.assertEqual(wyznacz_opis_akcji[LTR_ZAZN_USUN], 'Usuń')

    def test_some_constants(self):
        '''
        TestSomeConstants:
        '''
        self.assertEqual(wyznacz_wielkosc[CHC_PIC_ORYG], lc_kw.fq_oryg_qv)
        self.assertEqual(wyznacz_wielkosc[CHC_PIC_STAMP], LTR_GLR_STAMP)
        self.assertEqual(wyznacz_wielkosc[CHC_PIC_SMALL], LTR_GLR_SMALL)
        self.assertEqual(rjb_sam_slsh, '/')
        self.assertEqual(RDZ_Audyt, '/kaud')
        self.assertEqual(RDZ_Inwentaryzacja, '/kinw')
        self.assertEqual(RDZ_Zdjecia, '/kzdj')
        self.assertEqual(RDZ_Oswietlenie, '/kosw')
        self.assertEqual(formatuj_pelne_in({
            lc_kw.fq_imie_qv: 'Imię',
            lc_kw.fq_nazwisko_qv: 'Nazwisko',
            }), 'Imię Nazwisko')
        self.assertEqual(LTR_GLR_X_SMALL, 1024)
        self.assertEqual(LTR_GLR_X_STAMP, 150)
        self.assertEqual(ladny_rozmiar(2047), '2047 B')
        self.assertEqual(ladny_rozmiar(2097151), '2047 KB')
        self.assertEqual(ladny_rozmiar(2097151, exp=0), '2097151 B')
        self.assertEqual(ladny_rozmiar(2097152, exp=0), '2097152 B')
        self.assertEqual(ladny_rozmiar(2097152, exp=1), '2048 KB')
        self.assertEqual(ladny_rozmiar(2097152), '2 MB')
        self.assertEqual(ladny_rozmiar(2147483647), '2047 MB')
        self.assertEqual(ladny_rozmiar(2147483648), '2 GB')
        self.assertEqual(ladny_rozmiar(2147483648, exp=2), '2048 MB')
