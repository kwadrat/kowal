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
