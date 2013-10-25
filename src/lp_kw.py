#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

day_zero = (0, 0, 0)
midnight_hour_wrap = {24: 0}

def verify_for_equal(tmp_value, expected):
    if tmp_value != expected:
        raise RuntimeError('tmp_value = %s' % repr(tmp_value))

def rj_na_godzine(dttm):
    return dttm.strftime('%H:%M')

def determine_quarter(qrt_number):
    result = rj_na_godzine(datetime.datetime(2013, 1, 31, 0, 0, 0) + datetime.timedelta(seconds=15*60 * qrt_number))
    return result

def change_to_full_hour(hour_number):
    return '%02d:00' % hour_number

def rj_na_date(dttm):
    return dttm.strftime('%Y-%m-%d')

def part_of_day_hs(par_h, par_m, par_s):
    return rj_na_godzine(datetime.time(par_h, par_m, par_s))

def process_hour_headers(time_tuple):
    day_part = time_tuple[:3]
    time_part = time_tuple[3:]
    verify_for_equal(day_part, day_zero)
    return part_of_day_hs(*time_part)

def process_quarter_headers(value):
    my_point = datetime.datetime(*value) - datetime.timedelta(seconds=15*60)
    my_date = rj_na_date(my_point)
    my_time = my_point.strftime('%H:%M')
    return my_date, my_time

def describe_column(column_index):
    hour_number = column_index + 1
    hour_number = midnight_hour_wrap.get(hour_number, hour_number)
    return change_to_full_hour(hour_number)

def has_date_from_dt(prm_date):
    return isinstance(prm_date, datetime.date)

def psycopg2_convert_date_format_to_text(slownik, pole):
    data = slownik[pole]
    if has_date_from_dt(data):
        slownik[slownik._index[pole]] = rj_na_date(data)

class HourMiniServer(object):
    def __init__(self, start_col, column_index):
        '''
        HourMiniServer:
        '''
        self.column_index = column_index
        self.canonical_hour = change_to_full_hour(self.column_index)
        self.col_in_sheet = start_col + self.column_index
        self.header_for_hour_column = describe_column(column_index)

    def __repr__(self):
        '''
        HourMiniServer:
        '''
        return 'HS(%s)' % self.header_for_hour_column

class HourServer(object):
    def __init__(self, start_col):
        '''
        HourServer:
        '''
        self.all_time_columns = []
        for column_index in xrange(24):
            self.all_time_columns.append(HourMiniServer(start_col, column_index))

    def verify_hours_headers(self, energy_reader):
        '''
        HourServer:
        '''
        for sample_index, one_column in enumerate(self.all_time_columns):
            tmp_text = energy_reader.vx_num_time(one_column.col_in_sheet, 6)
            expected = one_column.header_for_hour_column
            verify_for_equal(tmp_text, expected)

    def hours_for_header(self):
        '''
        HourServer:
        '''
        return map(lambda elem: elem.canonical_hour, self.all_time_columns)

class QuarterServer(object):
    def __init__(self):
        '''
        QuarterServer:
        '''
        self.quarter_translator = {}
        for i in xrange(96):
            hh_mm = determine_quarter(i)
            self.quarter_translator[hh_mm] = i

    def quarter_to_number(self, hh_mm):
        '''
        QuarterServer:
        '''
        return self.quarter_translator[hh_mm]

    def hours_for_header(self):
        '''
        QuarterServer:
        '''
        list_of_hours = self.quarter_translator.keys()
        list_of_hours.sort()
        return list_of_hours

class TestDateQuarters(unittest.TestCase):
    def test_date_quarters(self):
        '''
        TestDateQuarters:
        '''
        obk = QuarterServer()
        self.assertEqual(rj_na_godzine(datetime.time(2, 45, 00)), '02:45')
        self.assertEqual(part_of_day_hs(2, 45, 00), '02:45')
        self.assertEqual(rj_na_date(datetime.datetime(2013, 1, 31, 0, 0, 0)), '2013-01-31')
        self.assertEqual(process_quarter_headers([2013, 1, 31, 23, 59, 00]), ('2013-01-31', '23:44'))
        self.assertEqual(change_to_full_hour(7), '07:00')
        self.assertEqual(determine_quarter(0), '00:00')
        self.assertEqual(determine_quarter(1), '00:15')
        self.assertEqual(determine_quarter(95), '23:45')
        self.assertEqual(obk.quarter_to_number('00:00'), 0)
        self.assertEqual(obk.quarter_to_number('00:15'), 1)
        self.assertEqual(obk.quarter_to_number('23:45'), 95)

    def test_hour_patterns(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(describe_column(0), '01:00')
        self.assertEqual(describe_column(1), '02:00')
        self.assertEqual(describe_column(22), '23:00')
        self.assertEqual(describe_column(23), '00:00')

    def test_date_converter(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(rj_na_date(datetime.date(2012, 1, 2)), '2012-01-02')
        self.assertEqual(rj_na_date(datetime.date(2013, 3, 1)), '2013-03-01')
        self.assertEqual(has_date_from_dt(datetime.date(2013, 3, 1)), 1)
        self.assertEqual(has_date_from_dt('2013-03-01'), 0)
