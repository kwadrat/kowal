#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import oa_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KreskiWykresu(object):
    def __init__(self):
        '''
        KreskiWykresu:
        '''
        self.collected_lines = []

    def append(self, krotka):
        '''
        KreskiWykresu:
        '''
        self.collected_lines.append(krotka)

    def line_with_default_color(self, dimensions):
        '''
        KreskiWykresu:
        '''
        krotka = (dimensions, oa_kw.Kolor_Kresek)
        self.append(krotka)

    def tick_on_vertical_axis(self, end_x, end_y):
        '''
        KreskiWykresu:
        '''
        self.line_with_default_color((end_x - oa_kw.DlugoscKresekMiesiecy, end_y, end_x, end_y))

    def narysuj_na_obrazku(self, draw):
        '''
        KreskiWykresu:
        '''
        for polozenie, kolor in self.collected_lines:
            draw.line(polozenie, kolor)

class TestKresekWykresu(unittest.TestCase):
    def test_kresek_wykresu(self):
        '''
        TestKresekWykresu:
        '''
        obk = KreskiWykresu()
        obk.append
        obk.narysuj_na_obrazku
        obk.line_with_default_color
        obk.tick_on_vertical_axis
