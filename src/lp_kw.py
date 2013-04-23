#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

day_zero = (0, 0, 0)

def verify_for_equal(tmp_value, expected):
    if tmp_value != expected:
        raise RuntimeError('tmp_value = %s' % repr(tmp_value))

def part_of_day_hs(par_h, par_m, par_s):
    return datetime.time(par_h, par_m, par_s).strftime('%H:%M')

def process_hour_headers(time_tuple):
    day_part = time_tuple[:3]
    time_part = time_tuple[3:]
    verify_for_equal(day_part, day_zero)
    return part_of_day_hs(*time_part)

class TestDateQuarters(unittest.TestCase):
    def test_date_quarters(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(part_of_day_hs(2, 45, 00), '02:45')

