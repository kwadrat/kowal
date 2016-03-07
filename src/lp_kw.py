#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import en_kw
import ciy_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

day_zero = (0, 0, 0)
midnight_hour_wrap = {24: 0}
midnight_quarter_wrap = {96: 0}

def verify_for_equal(tmp_value, expected):
    if tmp_value != expected:
        raise RuntimeError('tmp_value = %s expected = %s' % (repr(tmp_value), repr(expected)))

def verify_for_u8_equal(tmp_value, expected):
    tmp_value = en_kw.upgrade_to_unicode(tmp_value)
    verify_for_equal(tmp_value, expected)

def verify_for_2_equal(tmp_value, ls_expected):
    if tmp_value not in ls_expected:
        raise RuntimeError('tmp_value = %s' % repr(tmp_value))

def prepare_s_date(year, month, day, hour, minute, second):
    return datetime.datetime(year, month, day, hour, minute, second)

def rj_na_godzine(dttm):
    return dttm.strftime('%H:%M')

def determine_quarter(qrt_number):
    result = (rj_na_godzine(prepare_s_date(2013, 1, 31, 0, 0, 0) + datetime.timedelta(seconds=15 * 60 * qrt_number)))
    return result

def determine_hour(hour_number):
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
    my_point = prepare_s_date(*value) - datetime.timedelta(seconds=15*60)
    my_date = rj_na_date(my_point)
    my_time = my_point.strftime('%H:%M')
    return my_date, my_time

def describe_hour_column(column_index):
    one_number = column_index + 1
    one_number = midnight_hour_wrap.get(one_number, one_number)
    return determine_hour(one_number)

def describe_quarter_column(column_index):
    one_number = column_index + 1
    one_number = midnight_quarter_wrap.get(one_number, one_number)
    return determine_quarter(one_number)

def has_date_from_dt(prm_date):
    return isinstance(prm_date, datetime.date)

def psycopg2_convert_date_format_to_text(slownik, pole):
    data = slownik[pole]
    if has_date_from_dt(data):
        slownik[slownik._index[pole]] = rj_na_date(data)

def build_date(rok, miesiac, dzien):
    return datetime.date(rok, miesiac, dzien)

def heating_period(my_point):
    year = my_point.year
    if my_point.month <= 8:
        year -= 1
    return year

def watering_period(my_point):
    year = my_point.year
    return year

def heating_label(year):
    return '%d/%d' % (year, year + 1)

def watering_label(year):
    return '%d' % (year,)

def detect_invariant_time(times_of_counters, default_value):
    mono_cnt = {}
    for dttm, one_cnt in times_of_counters:
        times_for_cnt = mono_cnt.get(one_cnt)
        if not times_for_cnt:
            times_for_cnt = mono_cnt[one_cnt] = []
        time_value = rj_na_godzine(dttm)
        times_for_cnt.append(time_value)
    for one_cnt in mono_cnt:
        mono_cnt[one_cnt] = ciy_kw.invariable_time(mono_cnt[one_cnt], default_value)
    return mono_cnt

def convert_keys(integer_keys):
    string_keys = {}
    for one_key, one_value in integer_keys.iteritems():
        string_keys[str(one_key)] = one_value
    result = str(string_keys)
    return result

class TestDateQuarters(unittest.TestCase):
    def test_date_quarters(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(rj_na_godzine(datetime.time(2, 45, 00)), '02:45')
        self.assertEqual(part_of_day_hs(2, 45, 00), '02:45')
        self.assertEqual(rj_na_date(prepare_s_date(2013, 1, 31, 0, 0, 0)), '2013-01-31')
        self.assertEqual(process_quarter_headers([2013, 1, 31, 23, 59, 00]), ('2013-01-31', '23:44'))
        self.assertEqual(determine_hour(7), '07:00')
        self.assertEqual(determine_quarter(0), '00:00')
        self.assertEqual(determine_quarter(1), '00:15')
        self.assertEqual(determine_quarter(95), '23:45')

    def test_hour_patterns(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(describe_hour_column(0), '01:00')
        self.assertEqual(describe_hour_column(1), '02:00')
        self.assertEqual(describe_hour_column(22), '23:00')
        self.assertEqual(describe_hour_column(23), '00:00')

    def test_date_converter(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(rj_na_date(datetime.date(2012, 1, 2)), '2012-01-02')
        self.assertEqual(rj_na_date(datetime.date(2013, 3, 1)), '2013-03-01')
        self.assertEqual(has_date_from_dt(datetime.date(2013, 3, 1)), 1)
        self.assertEqual(has_date_from_dt('2013-03-01'), 0)
        self.assertEqual(build_date(2012, 1, 2), datetime.date(2012, 1, 2))
        self.assertEqual(heating_period(build_date(2012, 8, 2)), 2011)
        self.assertEqual(heating_period(build_date(2012, 9, 2)), 2012)
        self.assertEqual(watering_period(build_date(2011, 1, 1)), 2011)
        self.assertEqual(watering_period(build_date(2012, 12, 31)), 2012)
        self.assertEqual(heating_label(2011), '2011/2012')
        self.assertEqual(heating_label(2012), '2012/2013')
        self.assertEqual(watering_label(2011), '2011')
        self.assertEqual(watering_label(2012), '2012')

    def test_time_headers(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(describe_quarter_column(0), '00:15')
        self.assertEqual(describe_quarter_column(94), '23:45')
        self.assertEqual(describe_quarter_column(95), '00:00')

    def test_time_from_db(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(detect_invariant_time([
            [datetime.time(7, 30), 959],
            [datetime.time(7, 30), 959],
            ], None), {
            959: '07:30',
            })
        self.assertEqual(detect_invariant_time([
            [datetime.time(7, 30), 959],
            [datetime.time(7, 30), 959],
            [datetime.time(8, 0), 381],
            [datetime.time(8, 0), 381],
            [datetime.time(7, 30), 386],
            [datetime.time(8, 0), 386],
            ], None), {
            959: '07:30',
            381: '08:00',
            386: None,
            })

    def test_freezing_keys(self):
        '''
        TestDateQuarters:
        '''
        self.assertEqual(convert_keys({}), '{}')
        self.assertEqual(convert_keys({959: '07:30', 381: '08:00'}), "{'959': '07:30', '381': '08:00'}")
