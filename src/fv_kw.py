#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class ColCalc(object):
    def __init__(self, my_offset):
        '''
        ColCalc:
        '''
        self.my_offset = my_offset

    def vx_porz(self, litera):
        '''
        ColCalc:
        '''
        return hj_kw.letter_to_number(litera) + self.my_offset

    def vx_litera(self, liczba):
        '''
        ColCalc:
        '''
        if self.my_offset <= liczba <= 25 + self.my_offset:
            return hj_kw.wyznacz_litere_faktury(liczba - self.my_offset)
        else:
            raise RuntimeError('Poza zakresem?: %s' % repr(liczba))

    def vx_lt(self, lb_col):
        '''
        ColCalc:
        Numer kolejny litery, aby łatwiej wpisywać adresy w Excelu
        '''
        ile = len(lb_col)
        if ile == 1:
            wynik = self.vx_porz(lb_col)
        elif ile == 2:
            wynik = (self.vx_porz(lb_col[0]) + 1 - self.my_offset) * 26 + self.vx_porz(lb_col[1])
        else:
            raise RuntimeError('Nieobslugiwany napis kolumny: %s' % repr(lb_col))
        return wynik

    def vx_rev_lt(self, liczba):
        '''
        ColCalc:
        '''
        if liczba > 25 + self.my_offset:
            major, minor = divmod(liczba - self.my_offset, 26)
            wynik = self.vx_rev_lt(major - 1 + self.my_offset) + self.vx_litera(minor + self.my_offset)
        else:
            wynik = self.vx_litera(liczba)
        return wynik

vx_zero = ColCalc(0)
vx_one = ColCalc(1)

class TestKolumnLiterowych(unittest.TestCase):
    def test_with_offset_zero(self):
        '''
        TestKolumnLiterowych:
        '''
        self.assertEqual(vx_zero.vx_porz('A'), 0)
        self.assertEqual(vx_zero.vx_porz('Z'), 25)
        self.assertEqual(vx_zero.vx_lt('A'), 0)
        self.assertEqual(vx_zero.vx_lt('Z'), 25)
        self.assertEqual(vx_zero.vx_lt('AA'), 26)
        self.assertEqual(vx_zero.vx_lt('AB'), 27)
        self.assertEqual(vx_zero.vx_lt('BA'), 52)
        self.assertRaises(RuntimeError, vx_zero.vx_lt, 'AAA')
        self.assertEqual(vx_zero.vx_rev_lt(0), 'A')
        self.assertEqual(vx_zero.vx_rev_lt(25), 'Z')
        self.assertEqual(vx_zero.vx_rev_lt(26), 'AA')
        self.assertEqual(vx_zero.vx_rev_lt(701), 'ZZ')
        self.assertRaises(RuntimeError, vx_zero.vx_litera, -1)
        self.assertRaises(RuntimeError, vx_zero.vx_litera, 26)

    def test_with_offset_one(self):
        '''
        TestKolumnLiterowych:
        '''
        self.assertEqual(vx_one.vx_porz('A'), 1)
        self.assertEqual(vx_one.vx_porz('Z'), 26)
        self.assertEqual(vx_one.vx_lt('A'), 1)
        self.assertEqual(vx_one.vx_lt('Z'), 26)
        self.assertEqual(vx_one.vx_lt('AA'), 27)
        self.assertEqual(vx_one.vx_lt('AB'), 28)
        self.assertEqual(vx_one.vx_lt('BA'), 53)
        self.assertRaises(RuntimeError, vx_one.vx_lt, 'AAA')
        self.assertEqual(vx_one.vx_rev_lt(1), 'A')
        self.assertEqual(vx_one.vx_rev_lt(26), 'Z')
        self.assertEqual(vx_one.vx_rev_lt(27), 'AA')
        self.assertEqual(vx_one.vx_rev_lt(702), 'ZZ')
        self.assertRaises(RuntimeError, vx_one.vx_litera, 0)
        self.assertRaises(RuntimeError, vx_one.vx_litera, 27)
