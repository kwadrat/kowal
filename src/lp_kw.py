#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

day_zero = (0, 0, 0)
midnight_hour_wrap = {24: 0}

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

def describe_column(column_index):
    hour_number = column_index + 1
    hour_number = midnight_hour_wrap.get(hour_number, hour_number)
    return change_to_full_hour(hour_number)

class HourServer:
    def __init__(self, start_col, column_index):
        '''
        HourServer:
        '''
        self.column_index = column_index
        self.canonical_hour = change_to_full_hour(self.column_index)
        self.col_in_sheet = start_col + self.column_index
        self.header_for_hour_column = describe_column(column_index)

    def __repr__(self):
        '''
        HourServer:
        '''
        return 'HS(%s)' % self.header_for_hour_column

class TestDateQuarters(unittest.TestCase):
    def test_date_quarters(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(part_of_day_hs(2, 45, 00), '02:45')
        self.assertEqual(process_quarter_headers([2013, 1, 31, 23, 59, 00]), ('2013.01.31', '23:44'))
        self.assertEqual(change_to_full_hour(7), '07:00')

    def test_hour_patterns(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(describe_column(0), '01:00')
        self.assertEqual(describe_column(1), '02:00')
        self.assertEqual(describe_column(22), '23:00')
        self.assertEqual(describe_column(23), '00:00')
