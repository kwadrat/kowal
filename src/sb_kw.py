#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
MSIE 7.1 przesyła pełne ścieżki pliku, należy ją przyciąć używając funkcji
z modułu ntpath używanego zwykle w Windows
'''

import ntpath
import unittest


def only_filename(maybe_full_name):
    if '\\' in maybe_full_name:
        wynik = ntpath.basename(maybe_full_name)
    else:
        wynik = maybe_full_name
    return wynik


class TestFunkcjiObcinajacejSciezke(unittest.TestCase):
    def test_msie_7_gave_full_path(self):
        '''
        TestFunkcjiObcinajacejSciezke:
        '''
        self.assertEqual(only_filename('a.txt'), 'a.txt')
        self.assertEqual(only_filename(r'C:\kurs\C-11_prezentacja.ppt'), 'C-11_prezentacja.ppt')
