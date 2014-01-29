#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Rozpoznawanie zakresu dni w ramach jednego roku
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

roman_map = dict((k, v) for k, v in zip(dn_kw.tab_rzymskich, dn_kw.numery_miesiecy))

class RomanPeriod(object):
    def take_year(self, elem_ls):
        '''
        RomanPeriod:
        '''
        self.the_year = int(elem_ls[0])
        elem_ls = elem_ls[1:]
        return elem_ls

    def take_first(self, elem_ls):
        '''
        RomanPeriod:
        '''
        self.the_first = roman_map.get(elem_ls[0])
        if self.the_first is not None:
            elem_ls = elem_ls[1:]
        if elem_ls:
            self.the_day_first = int(elem_ls[0])
            elem_ls = elem_ls[1:]
        else:
            self.the_day_first = None
        return elem_ls

    def take_second(self, elem_ls):
        '''
        RomanPeriod:
        '''
        self.the_second = roman_map[elem_ls[0]]
        elem_ls = elem_ls[1:]
        if elem_ls:
            the_elem = elem_ls[0]
            if the_elem in roman_map:
                self.the_day_second = None
            else:
                self.the_day_second = int(the_elem)
                elem_ls = elem_ls[1:]
        return elem_ls

    def take_all(self, elem_ls):
        '''
        RomanPeriod:
        '''
        elem_ls = self.take_year(elem_ls)
        elem_ls = self.take_second(elem_ls)
        elem_ls = self.take_first(elem_ls)
        if self.the_first is None:
            self.the_first = self.the_second
        return elem_ls

    def __init__(self, the_date=None):
        '''
        RomanPeriod:
        '''
        if the_date is not None:
            elem_ls = the_date.replace('-', ' ')
            elem_ls = elem_ls.replace('.', ' ')
            elem_ls = elem_ls.split()
            elem_ls.reverse()
            self.the_rest = self.take_all(elem_ls)

    def get_tuple(self):
        '''
        RomanPeriod:
        '''
        return (
            self.the_year,
            self.the_first,
            self.the_day_first,
            self.the_second,
            self.the_day_second,
            )

def detect_day_ranges(napis):
    obk = RomanPeriod(napis)
    result = obk.get_tuple()
    return result

def valid_date_format(value):
    return hj_kw.zamien_na_logiczne(value)

def nazwa_rzymskiego(numer):
    return dn_kw.tab_rzymskich[numer - 1]

def RzymskiDnia(nkd):
    miesiac = dn_kw.MiesiacDnia(nkd)
    return nazwa_rzymskiego(miesiac)

def roman_range(krotka):
    return '%s-%s-%s' % (
        nazwa_rzymskiego(krotka[0]),
        nazwa_rzymskiego(krotka[1]),
        krotka[2],
        )

class TestDaysRanges(unittest.TestCase):
    def test_days_ranges(self):
        '''
        TestDaysRanges:
        '''
        self.assertEqual(detect_day_ranges('01-06-I-2010'), (2010, 1, 1, 1, 6))
        self.assertEqual(detect_day_ranges('01.I-06.I-2010'), (2010, 1, 1, 1, 6))
        self.assertEqual(detect_day_ranges('07.I-31.I-2010'), (2010, 1, 7, 1, 31))
        self.assertEqual(detect_day_ranges('07-I-XII-2010'), (2010, 1, 7, 12, None))
        self.assertEqual(detect_day_ranges('24-IV-XII-2013'), (2013, 4, 24, 12, None))
        self.assertEqual(detect_day_ranges('I - III-2013'), (2013, 1, None, 3, None))
        self.assertEqual(detect_day_ranges('I - IX-2012'), (2012, 1, None, 9, None))
        self.assertEqual(detect_day_ranges('I - XII-2010'), (2010, 1, None, 12, None))
        self.assertEqual(detect_day_ranges('I - XII-2011'), (2011, 1, None, 12, None))
        self.assertEqual(detect_day_ranges('I-23-IV-2013'), (2013, 1, None, 4, 23))
        self.assertEqual(detect_day_ranges('I-II-2011'), (2011, 1, None, 2, None))
        self.assertEqual(detect_day_ranges('I-III-2012'), (2012, 1, None, 3, None))
        self.assertEqual(detect_day_ranges('I-III-2013'), (2013, 1, None, 3, None))
        self.assertEqual(detect_day_ranges('III-XII-2011'), (2011, 3, None, 12, None))
        self.assertEqual(detect_day_ranges('I-IV-2012'), (2012, 1, None, 4, None))
        self.assertEqual(detect_day_ranges('I-IX-2012'), (2012, 1, None, 9, None))
        self.assertEqual(detect_day_ranges('II-XII-2010'), (2010, 2, None, 12, None))
        self.assertEqual(detect_day_ranges('IV - XII-2013'), (2013, 4, None, 12, None))
        self.assertEqual(detect_day_ranges('I-VI-2012'), (2012, 1, None, 6, None))
        self.assertEqual(detect_day_ranges('IV-XII-2012'), (2012, 4, None, 12, None))
        self.assertEqual(detect_day_ranges('IV-XII-2013'), (2013, 4, None, 12, None))
        self.assertEqual(detect_day_ranges('I-XII-2011'), (2011, 1, None, 12, None))
        self.assertEqual(detect_day_ranges('I-XII-2012'), (2012, 1, None, 12, None))
        self.assertEqual(detect_day_ranges('I-XII-2013'), (2013, 1, None, 12, None))
        self.assertEqual(detect_day_ranges('VIII-XII-2011'), (2011, 8, None, 12, None))
        self.assertEqual(detect_day_ranges('VII-XII-2012'), (2012, 7, None, 12, None))
        self.assertEqual(detect_day_ranges('V-XII-2012'), (2012, 5, None, 12, None))
        self.assertEqual(detect_day_ranges('X-XII-2012'), (2012, 10, None, 12, None))

    def test_days_3_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_year(['2013'])
        self.assertEqual(obk.the_year, 2013)
        self.assertEqual(rest, [])

    def test_days_4_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_second(['I'])
        self.assertEqual(obk.the_second, 1)
        self.assertEqual(rest, [])

    def test_days_5_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_second(['I', '05'])
        self.assertEqual(obk.the_second, 1)
        self.assertEqual(obk.the_day_second, 5)
        self.assertEqual(rest, [])

    def test_days_6_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_first(['XII'])
        self.assertEqual(obk.the_first, 12)
        self.assertEqual(obk.the_day_first, None)
        self.assertEqual(rest, [])

    def test_days_7_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_first(['VI', '12'])
        self.assertEqual(obk.the_first, 6)
        self.assertEqual(obk.the_day_first, 12)
        self.assertEqual(rest, [])

    def test_days_8_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_second(['IX', 'VI'])
        self.assertEqual(obk.the_second, 9)
        self.assertEqual(obk.the_day_second, None)
        self.assertEqual(rest, ['VI'])

    def test_days_9_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_all(['2012', 'XII', 'IV'])
        self.assertEqual(obk.the_year, 2012)
        self.assertEqual(obk.the_second, 12)
        self.assertEqual(obk.the_day_second, None)
        self.assertEqual(obk.the_first, 4)
        self.assertEqual(obk.the_day_first, None)
        self.assertEqual(rest, [])

    def test_days_10_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod('IV-XII-2012')
        self.assertEqual(obk.the_year, 2012)
        self.assertEqual(obk.the_second, 12)
        self.assertEqual(obk.the_day_second, None)
        self.assertEqual(obk.the_first, 4)
        self.assertEqual(obk.the_day_first, None)
        self.assertEqual(obk.the_rest, [])

    def test_days_11_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod()
        rest = obk.take_first(['02'])
        self.assertEqual(obk.the_first, None)
        self.assertEqual(obk.the_day_first, 2)
        self.assertEqual(rest, [])

    def test_days_12_ranges(self):
        '''
        TestDaysRanges:
        '''
        obk = RomanPeriod('02-06-I-2010')
        self.assertEqual(obk.the_year, 2010)
        self.assertEqual(obk.the_second, 1)
        self.assertEqual(obk.the_day_second, 6)
        self.assertEqual(obk.the_first, 1)
        self.assertEqual(obk.the_day_first, 2)
        self.assertEqual(obk.the_rest, [])
        self.assertEqual(obk.get_tuple(), (2010, 1, 2, 1, 6))

    def test_days_13_ranges(self):
        '''
        TestDaysRanges:
        '''
        self.assertEqual(valid_date_format(None), 0)
        self.assertEqual(valid_date_format('02-06-I-2010'), 1)
        self.assertEqual(valid_date_format(''), 0)

    def test_days_14_ranges(self):
        '''
        TestDaysRanges:
        '''
        self.assertEqual(roman_map['I'], 1)
        self.assertEqual(roman_map['XII'], 12)
        self.assertEqual(RzymskiDnia(15278), 'X')
        self.assertEqual(roman_range((1, 2, 2011)), 'I-II-2011')
        self.assertEqual(nazwa_rzymskiego(4), 'IV')
