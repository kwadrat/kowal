#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


def tq_poczatek_roku(ih_rok):
    return "'%d-01-01'" % ih_rok


def tq_koniec_roku(ih_rok):
    return "'%d-12-31'" % ih_rok


class TestYearBorders(unittest.TestCase):
    def test_year_borders(self):
        '''
        TestYearBorders:
        '''
        self.assertEqual(tq_poczatek_roku(2012), "'2012-01-01'")
        self.assertEqual(tq_koniec_roku(2012), "'2012-12-31'")
