#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Single cell or multi-row/-column rectangle area
'''

import unittest


class MergedCoords(object):
    def update_cols(self, liczba_kolumn):
        '''
        MergedCoords:
        '''
        self.liczba_kolumn = liczba_kolumn

    def update_rows(self, liczba_wierszy):
        '''
        MergedCoords:
        '''
        self.liczba_wierszy = liczba_wierszy

    def __init__(self, akt_wiersz=None, akt_kolumna=None, liczba_kolumn=1, liczba_wierszy=1):
        '''
        MergedCoords:
        '''
        self.akt_wiersz = akt_wiersz
        self.akt_kolumna = akt_kolumna
        self.update_cols(liczba_kolumn)
        self.update_rows(liczba_wierszy)

    def is_one(self):
        '''
        MergedCoords:
        '''
        return self.liczba_kolumn == 1 and self.liczba_wierszy == 1

    def wyznacz_cztery(self):
        '''
        MergedCoords:
        '''
        r1 = self.akt_wiersz
        r2 = r1 + self.liczba_wierszy - 1
        c1 = self.akt_kolumna
        c2 = c1 + self.liczba_kolumn - 1
        return r1, r2, c1, c2

    def wyznacz_dwa(self):
        '''
        MergedCoords:
        '''
        r1 = self.akt_wiersz
        c1 = self.akt_kolumna
        return r1, c1


class TestMergedCoords(unittest.TestCase):
    def test_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords()
        self.assertEqual(obk.is_one(), 1)
        obk.update_rows(2)
        self.assertEqual(obk.is_one(), 0)

    def test_2_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords(liczba_kolumn=2)
        self.assertEqual(obk.is_one(), 0)
        obk.update_cols(1)
        self.assertEqual(obk.is_one(), 1)

    def test_3_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords(liczba_wierszy=2)
        self.assertEqual(obk.is_one(), 0)

    def test_4_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords(1, 2, 3)
        self.assertEqual(obk.wyznacz_cztery(), (1, 1, 2, 4))
        obk = MergedCoords(1, 2, liczba_wierszy=3)
        self.assertEqual(obk.wyznacz_cztery(), (1, 3, 2, 2))
        self.assertEqual(obk.wyznacz_dwa(), (1, 2))
