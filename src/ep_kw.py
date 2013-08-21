#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ex_kw
import oh_kw
import od_kw
import es_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

MojeSlupki = es_kw.MojeSlupki

class PomiaroweSlupki(MojeSlupki):
    def __init__(self, tgk, aqr, dnw):
        '''
        PomiaroweSlupki:
        '''
        MojeSlupki.__init__(self, tgk, aqr, dnw)
        self.chce_bez_tresci = 1

    def ustaw_skalowanie_obrazu(self):
        '''
        PomiaroweSlupki:
        '''
        self.ustaw_prosty_obraz()

    def wyznacz_etykiete(self, pocz):
        '''
        PomiaroweSlupki:
        '''
        return ''

class TestPomiarowychSlupkow(unittest.TestCase):
    def test_pomiarowych_slupkow(self):
        '''
        TestPomiarowychSlupkow:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        aqr = ex_kw.SzkieletDatDlaZuzycia()
        aqr.przypisz_dla_roku_szkielet(2012, rok_z_rozszerzeniem=0)
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        obk = PomiaroweSlupki(tgk, aqr, dnw)
        self.assertEqual(obk.szerokosc_dx_skali, 0)
        self.assertEqual(obk.szerokosc_slupka, 30)
        self.assertEqual(obk.wysokosc_obrazu, 150)
        self.assertEqual(obk.margines_dy_powyzej_slupka, 20)
        self.assertEqual(obk.wsp_y_na_dole_slupka, 130)
        self.assertEqual(obk.gorna_mniejsza, 140)
        self.assertEqual(obk.chce_bez_tresci, 1)
