#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lk_kw
import rq_kw
import oa_kw
import ew_kw
import oh_kw
import od_kw
import pt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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

class TestWykresuRaportu(unittest.TestCase):
    def test_wykresu_raportu(self):
        '''
        TestWykresuRaportu:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        aqr = ew_kw.SzkieletDatDlaFakturMiesLat()
        lp_wykresu = 0
        dwk = oh_kw.SimpleDWN(lp_wykresu)
        ile_linii = 3 # Liczba linii tekstu na wykresie
        obk = WykresRaportu(tgk, aqr, dwk, ile_linii)
        self.assertEqual(obk.szerokosc_obrazu, 1250)
        self.assertEqual(obk.szerokosc_wykresu, 1240)
        self.assertEqual(obk.wysokosc_obrazu, 46)
        self.assertEqual(obk.szerokosc_dx_skali, 0)
        self.assertEqual(obk.wysokosc_linii, 12)
