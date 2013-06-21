#!/usr/bin/python
# -*- coding: UTF-8 -*-

import md5
import unittest

'''
Testy operacji na napisach (zamiana liter na małe, obliczanie sumy MD5)
'''

def pomniejsz_litery(napis):
    return napis.lower()

def suma_kont(napis):
    return md5.md5(napis).hexdigest()

def przecinek_kropka(a):
    return a.replace(',', '.')

def kropka_przecinek(a):
    return a.replace('.', ',')

def odwrotny_zwykly(napis):
    return napis.replace('\\', '/')

class TestNapisow(unittest.TestCase):
    def test_operacji_na_napisach(self):
        '''
        TestNapisow:
        '''
        self.assertEqual(pomniejsz_litery('ABC'), 'abc')
        self.assertEqual(pomniejsz_litery('AbC'), 'abc')
        self.assertEqual(suma_kont('abc'), '900150983cd24fb0d6963f7d28e17f72')
        self.assertEqual(przecinek_kropka('0,5'), '0.5')
        self.assertEqual(kropka_przecinek('0.5'), '0,5')
        self.assertEqual(odwrotny_zwykly('\\'), '/')
        self.assertEqual(odwrotny_zwykly('1\\2'), '1/2')
