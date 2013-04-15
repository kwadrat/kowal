#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def vx_porz(litera):
    return ord(litera.upper()) - ord('A') + 1

def vx_litera(liczba):
    if 1 <= liczba <= 26:
        return chr(ord('A') + liczba - 1)
    else:
        raise RuntimeError('Poza zakresem?: %s' % repr(liczba))

class ColCalc:
    def __init__(self, my_offset):
        '''
        ColCalc:
        '''
        self.my_offset = my_offset

    def vx_porz(self, litera):
        '''
        ColCalc:
        '''
        return ord(litera.upper()) - ord('A') + self.my_offset

    def vx_litera(self, liczba):
        '''
        ColCalc:
        '''
        if self.my_offset <= liczba <= 25 + self.my_offset:
            return chr(ord('A') + liczba - self.my_offset)
        else:
            raise RuntimeError('Poza zakresem?: %s' % repr(liczba))

    def vx_lt(self, napis):
        '''
        ColCalc:
        Numer kolejny litery, aby łatwiej wpisywać adresy w Excelu
        '''
        ile = len(napis)
        if ile == 1:
            wynik = self.vx_porz(napis)
        elif ile == 2:
            wynik = (self.vx_porz(napis[0]) + 1 - self.my_offset) * 26 + self.vx_porz(napis[1])
        else:
            raise RuntimeError('Nieobslugiwany napis kolumny: %s' % repr(napis))
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
    def test_kolumn_literowych(self):
        '''
        TestKolumnLiterowych:
        '''
        self.assertEqual(vx_porz('A'), 1)
        self.assertEqual(vx_porz('Z'), 26)
        self.assertRaises(RuntimeError, vx_litera, 0)
        self.assertRaises(RuntimeError, vx_litera, 27)

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
