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

def for_storing(value):
    return 'NULL'

def have_dec_type(value):
    return isinstance(value, decimal.Decimal)

class TestPointNumbers(unittest.TestCase):
    def test_point_numbers(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(a2d('1.5'), decimal.Decimal('1.5'))
        self.assertEqual(d2a(decimal.Decimal('1.5')), '1.500000')
        self.assertEqual(for_storing(None), 'NULL')
        self.assertEqual(have_dec_type(a2d('0')), 1)
        self.assertEqual(have_dec_type(0), 0)
