#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import decimal

def a2d(a):
    '''ASCII(kropka) -> Decimal'''
    return decimal.Decimal(a)

def d2a(a):
    '''Decimal -> ASCII(kropka)'''
    return '%f' % a

def dec2flt(a):
    '''Decimal -> float'''
    return float(d2a(a))

value_ten_const = a2d(10)

def have_dec_type(value):
    return isinstance(value, decimal.Decimal)

def for_storing(value):
    if have_dec_type(value):
        result = d2a(value)
    elif isinstance(value, float):
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

class TestPointNumbers(unittest.TestCase):
    def test_point_numbers(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(a2d('1.5'), decimal.Decimal('1.5'))
        self.assertEqual(a2d(15), decimal.Decimal('15'))
        self.assertEqual(d2a(decimal.Decimal('1.5')), '1.500000')
        self.assertEqual(dec2flt(decimal.Decimal('1.5')), 1.5)
        self.assertEqual(for_storing(None), 'NULL')
        self.assertEqual(for_storing(a2d('1.25')), '1.250000')
        self.assertEqual(for_storing(1.75), '1.75')
        self.assertEqual(have_dec_type(a2d('0')), 1)
        self.assertEqual(have_dec_type(0), 0)
        self.assertEqual(calculate_rounding(3), decimal.Decimal('0.001'))
        self.assertEqual(readjust_number(3, 1.5555), decimal.Decimal('1.556'))
