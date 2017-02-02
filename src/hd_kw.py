#!/usr/bin/python
# -*- coding: UTF-8 -*-

import md5
import unittest

'''
Testy operacji na napisach (zamiana liter na małe, obliczanie sumy MD5)
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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

def przecinkowane_pole(kolumna):
    if lm_kw.have_dec_type(kolumna):
        value_as_text = lm_kw.d2a(kolumna)
        value_as_text = kropka_przecinek(value_as_text)
    else:
        value_as_text = str(kolumna)
        if type(kolumna) is float:
            value_as_text = kropka_przecinek(value_as_text)
    return value_as_text

def comma_and_zero(txt_value):
    copy_value = txt_value
    try:
        if '.' in txt_value:
            if txt_value[-1] == '.':
                txt_value = txt_value + '0'
            while len(txt_value) >= 2 and txt_value[-1] == '0' and txt_value[-2] != '.':
                txt_value = txt_value[:-1]
            txt_value = kropka_przecinek(txt_value)
    except:
        raise RuntimeError('Failed to convert: %s' % repr(copy_value))
    return txt_value

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
        self.assertEqual(suma_kont('abc'), '900150983cd24fb0d6963f7d28e17f72')
        self.assertEqual(przecinek_kropka('0,5'), '0.5')
        self.assertEqual(kropka_przecinek('0.5'), '0,5')
        self.assertEqual(odwrotny_zwykly('\\'), '/')
        self.assertEqual(odwrotny_zwykly('1\\2'), '1/2')

    def test_pretty_txt_number(self):
        '''
        TestNapisow:
        '''
        self.assertEqual(comma_and_zero('1'), '1')
        self.assertEqual(comma_and_zero('1.'), '1,0')
        self.assertEqual(comma_and_zero('1.0'), '1,0')
        self.assertEqual(comma_and_zero('1.00'), '1,0')
        self.assertEqual(comma_and_zero('1.000'), '1,0')
        self.assertEqual(comma_and_zero('.'), ',0')

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
