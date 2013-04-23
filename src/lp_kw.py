#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

def part_of_day_hs(par_h, par_m, par_s):
    return datetime.time(par_h, par_m, par_s).strftime('%H:%M')

class TestDateQuarters(unittest.TestCase):
    def test_date_quarters(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(part_of_day_hs(2, 45, 00), '02:45')

