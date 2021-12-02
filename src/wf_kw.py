#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza faktur, obiekt jednej kolumny w tabelce faktur
'''

import unittest

import lk_kw

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
