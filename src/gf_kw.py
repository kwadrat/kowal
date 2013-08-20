#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
import dd_kw
import ey_kw
import oh_kw
import od_kw
import gc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

PoboroweOgolneSlupki = gc_kw.PoboroweOgolneSlupki

class PoboroweMiesieczneSlupki(PoboroweOgolneSlupki):
    def __init__(self, tgk, aqr, dnw):
        '''
        PoboroweMiesieczneSlupki:
        '''
        PoboroweOgolneSlupki.__init__(self, tgk, aqr, dnw, lw_kw.PDS_Dni)

class TestPoborowychMiesiecznychSlupkow(unittest.TestCase):
    def test_poborowych_miesiecznych_slupkow(self):
        '''
        TestPoborowychMiesiecznychSlupkow:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dn_Energy)
        aqr = ey_kw.SzkieletDatDlaPoborow(krt_pobor)
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        obk = PoboroweMiesieczneSlupki(tgk, aqr, dnw)
        self.assertEqual(obk.dolny_podpis, 'dni')
