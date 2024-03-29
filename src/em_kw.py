#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import dn_kw
import ew_kw
import oh_kw
import od_kw
import es_kw

MojeSlupki = es_kw.MojeSlupki


class FakturoweRoczneSlupki(MojeSlupki):
    def __init__(self, tgk, aqr, dnw, rn_after):
        '''
        FakturoweRoczneSlupki:
        '''
        MojeSlupki.__init__(self, tgk, aqr, dnw, rn_after)

    def ustaw_skalowanie_obrazu(self):
        '''
        FakturoweRoczneSlupki:
        '''
        self.ustaw_skalowany_obraz()

    def wyznacz_etykiete(self, pocz):
        '''
        FakturoweRoczneSlupki:
        '''
        return str(dn_kw.RokDnia(pocz))


class TestFakturowychRocznychSlupkow(unittest.TestCase):
    def test_fakturowych_rocznych_slupkow(self):
        '''
        TestFakturowychRocznychSlupkow:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        aqr = ew_kw.SzkieletDatDlaFakturMiesLat()
        dzien_pocz = 13149
        dzien_kon = 13879
        szkielet_lat = dn_kw.daty_lat(dzien_pocz, dzien_kon)
        aqr.przypisz_szkielet(szkielet_lat)
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        rn_after = 2
        obk = FakturoweRoczneSlupki(tgk, aqr, dnw, rn_after)
        self.assertEqual(obk.szerokosc_dx_skali, 0)
        self.assertEqual(obk.szerokosc_slupka, 30)
        self.assertEqual(obk.wysokosc_obrazu, 150)
        self.assertEqual(obk.margines_dy_powyzej_slupka, 20)
        self.assertEqual(obk.wsp_y_na_dole_slupka, 130)
        self.assertEqual(obk.gorna_mniejsza, 140)
        self.assertEqual(obk.linii_na_dole(), 1)
        self.assertEqual(obk.chce_bez_tresci, 0)
