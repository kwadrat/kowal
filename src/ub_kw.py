#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


EYK_klcz = 'kl_zast'
EYK_wrtsc = 'nz_zast'
OBK_go = 'go' # Pole wyznaczające porządek (goto) obiektów
OBK_sc = 'sc' # Pole wyznaczające porządek (goto) skrótów
WDM_wszystkie_pola = '*'
OBK_aktywny = 'aktywny'
FLG_aktywny = 't'

class TestStalychNapisow(unittest.TestCase):
    def test_stalych_napisow(self):
        '''
        TestStalychNapisow:
        '''
        self.assertEqual(WDM_wszystkie_pola, '*')
