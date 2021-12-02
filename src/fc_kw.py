#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import hj_kw


class ZwracanePola(object):
    def __init__(self):
        '''
        ZwracanePola:
        '''
        self.qs_kolejka = []

    def extend(self, lista):
        '''
        ZwracanePola:
        '''
        self.qs_kolejka.extend(lista)

    def append(self, elem):
        '''
        ZwracanePola:
        '''
        self.qs_kolejka.append(elem)

    def polaczone_przecinkami(self):
        '''
        ZwracanePola:
        '''
        return hj_kw.Poprzecinkuj(self.qs_kolejka)


class TestZwracanychPol(unittest.TestCase):
    def test_zwracanych_pol(self):
        '''
        TestZwracanychPol:
        '''
        obk = ZwracanePola()
        obk.append('a')
        self.assertEqual(obk.polaczone_przecinkami(), 'a')
        obk.extend(['b', 'c'])
        self.assertEqual(obk.polaczone_przecinkami(), 'a,b,c')
