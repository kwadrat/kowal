#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import decimal

def a2d(a):
    '''ASCII(kropka) -> Decimal'''
    return decimal.Decimal(a)

class TestPointNumbers(unittest.TestCase):
    def test_point_numbers(self):
        '''
        TestPointNumbers:
        '''
        self.assertEqual(a2d('1.5'), decimal.Decimal('1.5'))
