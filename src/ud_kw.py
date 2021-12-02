#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


class LpFakturyRoku(object):
    def __init__(self):
        '''
        LpFakturyRoku:
        '''
        self.current_year = None

    def ordinal_number(self, year):
        '''
        LpFakturyRoku:
        '''
        if self.current_year is None or self.current_year != year:
            self.current_year = year
            self.counter = 0
        self.counter += 1
        return self.counter

class TestLpFaktury(unittest.TestCase):
    def test_inserting_all(self):
        '''
        TestLpFaktury:
        '''
        obk = LpFakturyRoku()
        self.assertEqual(obk.ordinal_number(2010), 1)
        self.assertEqual(obk.ordinal_number(2010), 2)
        self.assertEqual(obk.ordinal_number(2011), 1)
