#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Logical operations on sets - symmetrical difference'''

import unittest


def roznica_zbiorow(zbior_a, zbior_b):
    return zbior_a - zbior_b


def rozbieznosc_zbiorow(zbior_a, zbior_b, verbose=1):
    mam_rozbieznosc = zbior_a != zbior_b
    if mam_rozbieznosc:
        if verbose:
            tmp_format = 'roznica_zbiorow(zbior_a, zbior_b)'; print 'Eval:', tmp_format, eval(tmp_format)
            tmp_format = 'roznica_zbiorow(zbior_b, zbior_a)'; print 'Eval:', tmp_format, eval(tmp_format)
    return mam_rozbieznosc


class TestOperacjiNaZbiorach(unittest.TestCase):
    def test_operacji_na_zbiorach(self):
        '''
        TestOperacjiNaZbiorach:
        '''

        self.assertEqual(roznica_zbiorow(frozenset('abc'), frozenset('ab')), frozenset('c'))
        self.assertEqual(roznica_zbiorow(frozenset('ab'), frozenset('abc')), frozenset(''))
        self.assertEqual(rozbieznosc_zbiorow(frozenset('ab'), frozenset('bc'), verbose=0), 1)
        self.assertEqual(rozbieznosc_zbiorow(frozenset('abc'), frozenset('cba')), 0)
