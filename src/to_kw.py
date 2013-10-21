#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Single cell or multi-row/-column rectangle area
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class MergedCoords(object):
    def __init__(self, liczba_kolumn=1, liczba_wierszy=1):
        '''
        MergedCoords:
        '''
        self.liczba_kolumn = liczba_kolumn
        self.liczba_wierszy = liczba_wierszy

    def is_one(self):
        '''
        MergedCoords:
        '''
        return self.liczba_kolumn == 1 and self.liczba_wierszy == 1

class TestMergedCoords(unittest.TestCase):
    def test_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords()
        self.assertEqual(obk.is_one(), 1)

    def test_2_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords(liczba_kolumn=2)
        self.assertEqual(obk.is_one(), 0)

    def test_3_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords(liczba_wierszy=2)
        self.assertEqual(obk.is_one(), 0)
