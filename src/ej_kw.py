#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ew_kw
import oh_kw
import od_kw
import es_kw

MojeSlupki = es_kw.MojeSlupki


class FakturoweMiesieczneSlupki(MojeSlupki):
    def __init__(self, tgk, aqr, dnw, rn_after):
        '''
        FakturoweMiesieczneSlupki:
        '''
        MojeSlupki.__init__(self, tgk, aqr, dnw, rn_after)

    def ustaw_skalowanie_obrazu(self):
        '''
        FakturoweMiesieczneSlupki:
        '''
        self.ustaw_prosty_obraz()

    def wyznacz_etykiete(self, pocz):
        '''
        FakturoweMiesieczneSlupki:
        '''
        return ''


class TestFakturowychMiesiecznychSlupkow(unittest.TestCase):
    def test_fakturowych_miesiecznych_slupkow(self):
        '''
        TestFakturowychMiesiecznychSlupkow:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        aqr = ew_kw.SzkieletDatDlaFakturMiesLat()
        aqr.przypisz_dla_roku_szkielet(2012, rok_z_rozszerzeniem=0)
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        rn_after = 2
        obk = FakturoweMiesieczneSlupki(tgk, aqr, dnw, rn_after)
        self.assertEqual(obk.szerokosc_dx_skali, 0)
        self.assertEqual(obk.szerokosc_slupka, 30)
        self.assertEqual(obk.wysokosc_obrazu, 150)
        self.assertEqual(obk.margines_dy_powyzej_slupka, 20)
        self.assertEqual(obk.wsp_y_na_dole_slupka, 130)
        self.assertEqual(obk.gorna_mniejsza, 140)
        self.assertEqual(obk.chce_bez_tresci, 0)
