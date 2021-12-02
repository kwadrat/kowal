#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

'''
Sprawdzenie, czy pole w bazie danych jest logicznie prawdziwe
'''

import unittest


def check_for_true(one_value):
    result = 0
    if one_value is True or one_value == 't':
        result = 1
    return result


class TestBooleanValues(unittest.TestCase):
    def test_boolean_values(self):
        '''
        TestBooleanValues:
        '''
        self.assertEqual(check_for_true('t'), 1)
        self.assertEqual(check_for_true(True), 1)
        self.assertEqual(check_for_true(False), 0)
        self.assertEqual(check_for_true('f'), 0)
