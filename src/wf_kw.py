#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza faktur, obiekt jednej kolumny w tabelce faktur
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lk_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class JednaKolumnaTabelkiFaktury(object):
    def __init__(self, etykieta, tvk_nagl=None):
        '''
        JednaKolumnaTabelkiFaktury:
        '''
        self.rh_etykieta = etykieta
        self.tvk_nagl = tvk_nagl

    def zwroc_etykiete(self):
        '''
        JednaKolumnaTabelkiFaktury:
        '''
        return self.rh_etykieta

    def zwroc_naglowek(self):
        '''
        JednaKolumnaTabelkiFaktury:
        '''
        if self.tvk_nagl is None:
            wynik = self.rh_etykieta
        else:
            wynik = self.tvk_nagl
        return wynik

class TestKolumnyFaktur(unittest.TestCase):
    def test_kolumny_faktur(self):
        '''
        TestKolumnyFaktur:
        '''
        obk = JednaKolumnaTabelkiFaktury(lk_kw.EtykietaLP)
        self.assertEqual(obk.zwroc_etykiete(), lk_kw.EtykietaLP)
