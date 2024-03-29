#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lk_kw
import rq_kw
import oa_kw
import ew_kw
import oh_kw
import od_kw
import pt_kw

KlasaObrazu = pt_kw.KlasaObrazu


class WykresRaportu(KlasaObrazu):
    def __init__(self, tgk, aqr, dnw, linii):
        '''
        WykresRaportu:
        '''
        KlasaObrazu.__init__(self, tgk, aqr, dnw, lk_kw.LITERA_WYKRES)
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz
        self.szerokosc_wykresu = self.szerokosc_obrazu - 10
        self.wysokosc_linii = 12
        self.wysokosc_obrazu = linii * self.wysokosc_linii + 10

    if rq_kw.Docelowo_psyco_nie_pygresql:
        ##############################################################################
        def wylicz_dla_slupka(self, slupek, kwota):
            '''
            WykresRaportu:
            '''
            return (self.szerokosc_wykresu * slupek) / kwota
        ##############################################################################
    else:
        ##############################################################################
        def wylicz_dla_slupka(self, slupek, kwota):
            '''
            WykresRaportu:
            '''
            return float(self.szerokosc_wykresu * slupek) / kwota
        ##############################################################################


class TestWykresuRaportu(unittest.TestCase):
    def test_wykresu_raportu(self):
        '''
        TestWykresuRaportu:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        aqr = ew_kw.SzkieletDatDlaFakturMiesLat()
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        ile_linii = 3  # Liczba linii tekstu na wykresie
        obk = WykresRaportu(tgk, aqr, dnw, ile_linii)
        self.assertEqual(obk.szerokosc_obrazu, 1250)
        self.assertEqual(obk.szerokosc_wykresu, 1240)
        self.assertEqual(obk.wysokosc_obrazu, 46)
        self.assertEqual(obk.szerokosc_dx_skali, 0)
        self.assertEqual(obk.wysokosc_linii, 12)
