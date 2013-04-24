#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

day_zero = (0, 0, 0)

def verify_for_equal(tmp_value, expected):
    if tmp_value != expected:
        raise RuntimeError('tmp_value = %s' % repr(tmp_value))

def change_to_full_hour(hour_number):
    return '%02d:00' % hour_number

def part_of_day_hs(par_h, par_m, par_s):
    return datetime.time(par_h, par_m, par_s).strftime('%H:%M')

def process_hour_headers(time_tuple):
    day_part = time_tuple[:3]
    time_part = time_tuple[3:]
    verify_for_equal(day_part, day_zero)
    return part_of_day_hs(*time_part)

def process_quarter_headers(value):
    my_point = datetime.datetime(*value) - datetime.timedelta(seconds=15*60)
    my_date = my_point.strftime('%Y.%m.%d')
    my_time = my_point.strftime('%H:%M')
    return my_date, my_time

class TestDateQuarters(unittest.TestCase):
    def test_date_quarters(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(part_of_day_hs(2, 45, 00), '02:45')
        self.assertEqual(process_quarter_headers([2013, 1, 31, 23, 59, 00]), ('2013.01.31', '23:44'))
