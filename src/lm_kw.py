#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import decimal

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def a2d(a):
    '''ASCII(kropka) -> Decimal'''
    return decimal.Decimal(a)

def d2a(a):
    '''Decimal -> ASCII(kropka)'''
    return '%f' % a

wartosc_zero_globalna = a2d('0')
value_ten_const = a2d(10)

def have_dec_type(value):
    return isinstance(value, decimal.Decimal)

def dec2flt(value):
    '''Decimal -> float'''
    if have_dec_type(value):
        value = float(d2a(value))
    return value

def for_storing(value):
    if have_dec_type(value):
        result = d2a(value)
    elif isinstance(value, float) or isinstance(value, int):
        result = str(value)
    else:
        result = 'NULL'
    return result

def calculate_rounding(places):
    return value_ten_const ** (- places)

def readjust_number(places, value):
    napis = '%.*f' % (places, value)
    rounding = calculate_rounding(places)
    return a2d(napis).quantize(rounding)

def rzeczywista_na_napis(liczba):
    '''Przerabia liczbę złotych (być może ułamkową, z groszami)
    na kwotę do pokazania użytkownikowi - bez części ułamkowej,
    jeśli ona jest zerowa.
    '''
    napis = '%.2f' % liczba
    if napis[-3:] == '.00': # Mamy pełną kwotę, bez ułamka
        return napis[:-3] # Zwróć tylko całkowitą wartość
    else:
        return napis # Zwróć pełną kwotę, łącznie z groszami

def generate_scale(max_value):
    the_last = int(max_value)
    return map(a2d, range(the_last + 1))

def roznica_dokladna(a, b):
    return d2a(a2d(b) - a2d(a))

def decimal_suma_wybranych_wpisow_slownika(slownik, klucze):
    decimal_suma_wartosci = wartosc_zero_globalna
    for klucz in klucze:
        ulotna_wartosc = slownik.pobierz_element(klucz)
        moja_wartosc = a2d(ulotna_wartosc)
        decimal_suma_wartosci += moja_wartosc
    return decimal_suma_wartosci

class TestPointNumbers(unittest.TestCase):
    def test_point_numbers(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(a2d('1.5'), decimal.Decimal('1.5'))
        self.assertEqual(a2d(15), decimal.Decimal('15'))
        self.assertEqual(d2a(decimal.Decimal('1.5')), '1.500000')
        self.assertEqual(dec2flt(decimal.Decimal('1.5')), 1.5)
        self.assertEqual(dec2flt(1.5), 1.5)
        self.assertEqual(for_storing(None), 'NULL')
        self.assertEqual(for_storing(a2d('1.25')), '1.250000')
        self.assertEqual(for_storing(1.75), '1.75')
        self.assertEqual(for_storing(2), '2')
        self.assertEqual(have_dec_type(a2d('0')), 1)
        self.assertEqual(have_dec_type(0), 0)
        self.assertEqual(calculate_rounding(3), decimal.Decimal('0.001'))
        self.assertEqual(readjust_number(3, 1.5555), decimal.Decimal('1.556'))
        self.assertEqual(rzeczywista_na_napis(589.56 * 100), '58956')
        self.assertEqual(rzeczywista_na_napis(589.56), '589.56')

    def test_generate_yscale(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(generate_scale(a2d('10.5')), map(a2d, range(11)))
        self.assertEqual(generate_scale(2.5), map(a2d, range(3)))
