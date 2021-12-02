#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lm_kw

class DecProxy(object):
    def __init__(self, dec_value):
        '''
        DecProxy:
        '''
        self.dec_value = dec_value
        self.int_multiplier = 4
        self.int_scaler = 10 ** self.int_multiplier
        self.int_value = int(self.int_scaler * self.dec_value)

class TestDecType(unittest.TestCase):
    def test_dec_type(self):
        '''
        TestDecType:
        '''
        dec_value = lm_kw.a2d('38.2902')
        obk = DecProxy(dec_value)
        self.assertEqual(obk.int_value, 382902)
        self.assertEqual(obk.int_multiplier, 4)
        self.assertEqual(obk.int_scaler, 10000)
