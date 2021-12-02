#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Moduł pozwalający wybrać między bazą produkcyjną a bazą rozwojową
'''

import unittest

import rq_kw

nazwa_prod = 'media'
nazwa_dev = 'kopia'
if rq_kw.Niebezpieczne_testowa_aplikacja_produkcyjna_baza:
    nazwa_dev = 'media'

def jaka_nazwa_bazy(system_prod_dev):
    if system_prod_dev:
        return nazwa_prod
    else:
        return nazwa_dev

class TestWyboruBazy(unittest.TestCase):
    def test_wyboru_bazy(self):
        '''
        TestWyboruBazy:
        '''
        self.assertEqual(jaka_nazwa_bazy(1), 'media')
        self.assertEqual(jaka_nazwa_bazy(0), 'kopia')
