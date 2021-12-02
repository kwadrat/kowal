#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Przydziela wiersze w arkuszu kalkulacyjnym poszczególnym tabelom
'''

import unittest


class Wierszownik(object):
    def __init__(self, wiersz_do_dyspozycji):
        '''
        Wierszownik:
        '''
        self.wiersz_do_dyspozycji = wiersz_do_dyspozycji

    def zabierz_wiersze(self, ile_do_wziecia):
        '''
        Wierszownik:
        '''
        current_value = self.wiersz_do_dyspozycji
        self.wiersz_do_dyspozycji += ile_do_wziecia
        return current_value


class TestPrzydzialuWierszy(unittest.TestCase):
    def test_przydzialu_wierszy(self):
        '''
        TestPrzydzialuWierszy:
        '''
        obk = Wierszownik(20)
        self.assertEqual(obk.wiersz_do_dyspozycji, 20)
        self.assertEqual(obk.zabierz_wiersze(10), 20)
        self.assertEqual(obk.wiersz_do_dyspozycji, 30)
