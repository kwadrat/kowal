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

def vx_lt(napis):
    '''
    Numer kolejny litery, aby łatwiej wpisywać adresy w Excelu
    '''
    ile = len(napis)
    if ile == 1:
        wynik = vx_porz(napis)
    elif ile == 2:
        wynik = vx_porz(napis[0]) * 26 + vx_porz(napis[1])
    else:
        raise RuntimeError('Nieobslugiwany napis kolumny: %s' % repr(napis))
    return wynik

def vx_rev_lt(liczba):
    if liczba > 26:
        a, b = divmod(liczba - 1, 26)
        wynik = vx_rev_lt(a) + vx_litera(b + 1)
    else:
        wynik = vx_litera(liczba)
    return wynik

class TestKolumnLiterowych(unittest.TestCase):
    def test_kolumn_literowych(self):
        '''
        TestKolumnLiterowych:
        '''
        self.assertEqual(vx_porz('A'), 1)
        self.assertEqual(vx_porz('Z'), 26)
        self.assertEqual(vx_lt('A'), 1)
        self.assertEqual(vx_lt('Z'), 26)
        self.assertEqual(vx_lt('AA'), 27)
        self.assertEqual(vx_lt('AB'), 28)
        self.assertEqual(vx_lt('BA'), 53)
        self.assertRaises(RuntimeError, vx_lt, 'AAA')
        self.assertEqual(vx_rev_lt(1), 'A')
        self.assertEqual(vx_rev_lt(26), 'Z')
        self.assertEqual(vx_rev_lt(27), 'AA')
        self.assertEqual(vx_rev_lt(702), 'ZZ')
        self.assertRaises(RuntimeError, vx_litera, 0)
        self.assertRaises(RuntimeError, vx_litera, 27)
