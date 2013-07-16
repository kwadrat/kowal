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
        lp_wykresu = 0
        dwk = oh_kw.SimpleDNW(lp_wykresu)
        obk = PomiaroweSlupki(tgk, aqr, dwk)
        self.assertEqual(obk.szerokosc_dx_skali, 0)
        self.assertEqual(obk.szerokosc_slupka, 30)
        self.assertEqual(obk.wysokosc_obrazu, 150)
        self.assertEqual(obk.margines_dy_slupka, 20)
