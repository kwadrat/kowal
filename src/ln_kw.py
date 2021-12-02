#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import hj_kw
import lm_kw


def convert_all(my_values):
    return "'{%s}'" % hj_kw.Poprzecinkuj(map(lm_kw.for_storing, my_values))


class TestConvertingVector(unittest.TestCase):
    def test_converting_vector(self):
        '''
        TestConvertingVector:
        '''
        self.assertEqual(convert_all([None] * 4), "'{NULL,NULL,NULL,NULL}'")
        self.assertEqual(convert_all([2.25, lm_kw.a2d('2.75')]), "'{2.25,2.750000}'")
