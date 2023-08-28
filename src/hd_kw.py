#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import unittest

'''
Testy operacji na napisach (zamiana liter na małe, obliczanie sumy MD5)
'''

import lm_kw
import en_kw
import cke_kw


def pomniejsz_litery(napis):
    return napis.lower()


def suma_kont(napis):
    return hashlib.md5(napis).hexdigest()


def przecinek_kropka(a):
    return a.replace(',', '.')


def odwrotny_zwykly(napis):
    return napis.replace('\\', '/')


def przecinkowane_pole(kolumna):
    if lm_kw.have_dec_type(kolumna):
        value_as_text = lm_kw.d2a(kolumna)
        value_as_text = cke_kw.detach_zeros(value_as_text)
        value_as_text = lm_kw.kropka_przecinek(value_as_text)
    else:
        value_as_text = str(kolumna)
        if type(kolumna) is float:
            value_as_text = lm_kw.kropka_przecinek(value_as_text)
    return value_as_text


def comma_and_some_zero(txt_value, rn_after):
    before_cnt = txt_value.find('.')
    comma_zeros = ',' + rn_after * '0'
    if before_cnt >= 0:
        before_txt = txt_value[:before_cnt]
        after_txt = txt_value[before_cnt + 1:]
        comma_zeros = ',' + after_txt + (rn_after - len(after_txt)) * '0'
    else:
        before_txt = txt_value
    return before_txt + comma_zeros


class TestNapisow(unittest.TestCase):
    def test_operacji_na_napisach(self):
        '''
        TestNapisow:
        '''
        self.assertEqual(pomniejsz_litery('ABC'), 'abc')
        self.assertEqual(pomniejsz_litery('AbC'), 'abc')
        self.assertEqual(suma_kont(en_kw.str_to_bt('abc')), '900150983cd24fb0d6963f7d28e17f72')
        self.assertEqual(suma_kont(en_kw.str_to_bt('ą')), '5786eab716295401c073064c3ec82a44')
        self.assertEqual(suma_kont(en_kw.through_latin_two('ą')), 'c668534d220baf21ca3cc6df5b7ed1d5')
        self.assertEqual(suma_kont(en_kw.through_cp_for_plsh_win('ą')), 'f361e25776077789e0db8ca985bf36c5')
        self.assertEqual(przecinek_kropka('0,5'), '0.5')
        self.assertEqual(odwrotny_zwykly('\\'), '/')
        self.assertEqual(odwrotny_zwykly('1\\2'), '1/2')

    def test_pretty_txt_precision_number(self):
        '''
        TestNapisow:
        '''
        self.assertEqual(comma_and_some_zero('1.', 2), '1,00')
        self.assertEqual(comma_and_some_zero('2.', 2), '2,00')
        self.assertEqual(comma_and_some_zero('12.', 2), '12,00')
        self.assertEqual(comma_and_some_zero('1', 2), '1,00')
        self.assertEqual(comma_and_some_zero('1.2', 2), '1,20')
        self.assertEqual(comma_and_some_zero('1.3', 2), '1,30')
        self.assertEqual(comma_and_some_zero('1.34', 2), '1,34')
        self.assertEqual(comma_and_some_zero('1.', 3), '1,000')
        self.assertEqual(comma_and_some_zero('1.2', 3), '1,200')
        self.assertEqual(comma_and_some_zero('1.234', 2), '1,234')
