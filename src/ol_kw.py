#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import hj_kw

class ObiektLiterujacy(object):
    def __init__(self, liczba_potrzebnych_liter):
        '''
        ObiektLiterujacy:
        '''
        self.liczba_potrzebnych_liter = liczba_potrzebnych_liter
        self.biezacy_indeks_litery = 0

    def chcemy_numerowac(self):
        '''
        ObiektLiterujacy:
        '''
        return self.liczba_potrzebnych_liter > 1

    def daj_koncowke_literowa(self):
        '''
        ObiektLiterujacy:
        '''
        assert self.biezacy_indeks_litery < self.liczba_potrzebnych_liter, (
          '%d < %d' % (self.biezacy_indeks_litery, self.liczba_potrzebnych_liter))
        assert self.biezacy_indeks_litery < 26 # Liczba dostępnych liter
        koncowka = '/' + hj_kw.wyznacz_litere_faktury(self.biezacy_indeks_litery)
        self.biezacy_indeks_litery += 1
        return koncowka

class TestObiektuLiterujacego(unittest.TestCase):
    def test_obiektu_literujacego(self):
        '''
        TestObiektuLiterujacego:
        '''
        obk = ObiektLiterujacy(1)
        self.assertEqual(obk.chcemy_numerowac(), 0)
        self.assertEqual(obk.daj_koncowke_literowa(), '/A')
