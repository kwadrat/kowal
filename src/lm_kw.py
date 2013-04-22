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

value_ten_const = a2d(10)

def for_storing(value):
    return 'NULL'

def have_dec_type(value):
    return isinstance(value, decimal.Decimal)

def calculate_rounding(places):
    return a2d(10) ** (- places)

class TestPointNumbers(unittest.TestCase):
    def test_point_numbers(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(a2d('1.5'), decimal.Decimal('1.5'))
        self.assertEqual(a2d(15), decimal.Decimal('15'))
        self.assertEqual(d2a(decimal.Decimal('1.5')), '1.500000')
        self.assertEqual(for_storing(None), 'NULL')
        self.assertEqual(have_dec_type(a2d('0')), 1)
        self.assertEqual(have_dec_type(0), 0)
        self.assertEqual(calculate_rounding(3), decimal.Decimal('0.001'))
