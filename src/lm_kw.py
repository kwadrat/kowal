#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import decimal

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
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

if rq_kw.Docelowo_psyco_nie_pygresql:
    wartosc_zero_z_bazy = wartosc_zero_globalna
else:
    wartosc_zero_z_bazy = 0.0

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

def rzeczywista_na_napis(liczba, rn_after=2):
    '''Przerabia liczbę złotych (być może ułamkową, z groszami)
    na kwotę do pokazania użytkownikowi - bez części ułamkowej,
    jeśli ona jest zerowa.
    '''
    if rn_after == 3:
        napis = '%.3f' % liczba
        last_cnt = -4
        pattern = '.000'
    if rn_after == 2:
        napis = '%.2f' % liczba
        last_cnt = -3
        pattern = '.00'
    if napis[last_cnt:] == pattern: # Mamy pełną kwotę, bez ułamka
        return napis[:last_cnt] # Zwróć tylko całkowitą wartość
    else:
        return napis # Zwróć pełną kwotę, łącznie z groszami

def generate_scale(max_value):
    the_last = int(max_value)
    return map(a2d, range(the_last + 1))

def roznica_dokladna(a, b):
    return d2a(a2d(b) - a2d(a))

def roznica_liczbowa(a, b):
    return a2d(b) - a2d(a)

def decimal_suma_wybranych_wpisow_slownika(slownik, klucze):
    decimal_suma_wartosci = wartosc_zero_globalna
    for klucz in klucze:
        ulotna_wartosc = slownik.pobierz_element(klucz)
        moja_wartosc = a2d(ulotna_wartosc)
        decimal_suma_wartosci += moja_wartosc
    return decimal_suma_wartosci

def adjust_for_csv(value):
    if value == '':
        result = None
    else:
        result = float(value)
    return result

class CloseToValue(object):
    def __init__(self, places):
        '''
        CloseToValue:
        '''
        self.epsilon = calculate_rounding(places)

    def rough_replacement(self, old_value, new_value):
        '''
        CloseToValue:
        '''
        if isinstance(new_value, float):
            new_value = str(new_value)
        return abs(old_value - a2d(new_value)) <= self.epsilon

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
        self.assertEqual(rzeczywista_na_napis(589.56 * 100, rn_after=3), '58956')
        self.assertEqual(rzeczywista_na_napis(589.56, rn_after=3), '589.560')
        self.assertEqual(hj_kw.remove_nones(
            [
            wartosc_zero_globalna,
            None,
            1,
            2,
            3,
            ]),
            [
            wartosc_zero_globalna,
            1,
            2,
            3,
            ],
            )

    def test_generate_yscale(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(generate_scale(a2d('10.5')), map(a2d, range(11)))
        self.assertEqual(generate_scale(2.5), map(a2d, range(3)))

    def test_zero_from_db(self):
        '''
        TestPointNumbers:
        '''
        if rq_kw.Docelowo_psyco_nie_pygresql:
            ##############################################################################
            self.assertEqual(wartosc_zero_z_bazy, wartosc_zero_globalna)
            ##############################################################################
        else:
            ##############################################################################
            self.assertEqual(wartosc_zero_z_bazy, 0.0)
            ##############################################################################

    def test_close_to_value(self):
        '''
        TestPointNumbers:
        '''
        obk = CloseToValue(places=3)
        self.assertEqual(obk.epsilon, a2d('0.001'))
        self.assertEqual(obk.rough_replacement(a2d('7.0408'), '7.041'), 1)
        self.assertEqual(obk.rough_replacement(a2d('7.041') + a2d('0.002'), '7.041'), 0)
        self.assertEqual(obk.rough_replacement(a2d('7.041') - a2d('0.002'), '7.041'), 0)
        self.assertEqual(obk.rough_replacement(a2d('7.041') + a2d('0.001'), '7.041'), 1)
        self.assertEqual(obk.rough_replacement(a2d('7.041') - a2d('0.001'), '7.041'), 1)

    def test_csv_helpers(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(adjust_for_csv('1.2'), 1.2)
        self.assertEqual(adjust_for_csv(''), None)
        self.assertEqual(roznica_dokladna('2', '2'), '0.000000')
        self.assertEqual(not roznica_liczbowa('2', '2'), 1)
