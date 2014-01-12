#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Rozpoznawanie zakresu dni w ramach jednego roku
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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
        self.the_first = dn_kw.roman_map[elem_ls[0]]
        elem_ls = elem_ls[1:]
        if elem_ls:
            self.the_day_first = elem_ls[0]
            elem_ls = elem_ls[1:]
        else:
            self.the_day_first = None
        return elem_ls

    def take_second(self, elem_ls):
        '''
        RomanPeriod:
        '''
        self.the_second = dn_kw.roman_map[elem_ls[0]]
        elem_ls = elem_ls[1:]
        if elem_ls:
            the_elem = elem_ls[0]
            if the_elem in dn_kw.roman_map:
                self.the_day_second = None
            else:
                self.the_day_second = the_elem
                elem_ls = elem_ls[1:]
        return elem_ls

    def take_all(self, elem_ls):
        '''
        RomanPeriod:
        '''
        elem_ls = self.take_year(elem_ls)
        elem_ls = self.take_second(elem_ls)
        elem_ls = self.take_first(elem_ls)
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

def detect_day_ranges(napis):
    result = None
    if napis[-5] == '-':
        rok = int(napis[-4:])
        reszta = napis[:-5]
        result = (rok, reszta)
    return result

def detect_month_pair(napis):
    result = (1, 1, 1, 6)
    return result

class TestDaysRanges(unittest.TestCase):
    def test_days_ranges(self):
        '''
        TestDaysRanges:
        '''
        self.assertEqual(detect_day_ranges('01-06-I-2010'), (2010, '01-06-I'))
        self.assertEqual(detect_day_ranges('01.I-06.I-2010'), (2010, '01.I-06.I'))
        self.assertEqual(detect_day_ranges('07.I-31.I-2010'), (2010, '07.I-31.I'))
        self.assertEqual(detect_day_ranges('07-I-XII-2010'), (2010, '07-I-XII'))
        self.assertEqual(detect_day_ranges('24-IV-XII-2013'), (2013, '24-IV-XII'))
        self.assertEqual(detect_day_ranges('I - III-2013'), (2013, 'I - III'))
        self.assertEqual(detect_day_ranges('I - IX-2012'), (2012, 'I - IX'))
        self.assertEqual(detect_day_ranges('I - XII-2010'), (2010, 'I - XII'))
        self.assertEqual(detect_day_ranges('I - XII-2011'), (2011, 'I - XII'))
        self.assertEqual(detect_day_ranges('I-23-IV-2013'), (2013, 'I-23-IV'))
        self.assertEqual(detect_day_ranges('I-II-2011'), (2011, 'I-II'))
        self.assertEqual(detect_day_ranges('I-III-2012'), (2012, 'I-III'))
        self.assertEqual(detect_day_ranges('I-III-2013'), (2013, 'I-III'))
        self.assertEqual(detect_day_ranges('III-XII-2011'), (2011, 'III-XII'))
        self.assertEqual(detect_day_ranges('I-IV-2012'), (2012, 'I-IV'))
        self.assertEqual(detect_day_ranges('I-IX-2012'), (2012, 'I-IX'))
        self.assertEqual(detect_day_ranges('II-XII-2010'), (2010, 'II-XII'))
        self.assertEqual(detect_day_ranges('IV - XII-2013'), (2013, 'IV - XII'))
        self.assertEqual(detect_day_ranges('I-VI-2012'), (2012, 'I-VI'))
        self.assertEqual(detect_day_ranges('IV-XII-2012'), (2012, 'IV-XII'))
        self.assertEqual(detect_day_ranges('IV-XII-2013'), (2013, 'IV-XII'))
        self.assertEqual(detect_day_ranges('I-XII-2011'), (2011, 'I-XII'))
        self.assertEqual(detect_day_ranges('I-XII-2012'), (2012, 'I-XII'))
        self.assertEqual(detect_day_ranges('I-XII-2013'), (2013, 'I-XII'))
        self.assertEqual(detect_day_ranges('VIII-XII-2011'), (2011, 'VIII-XII'))
        self.assertEqual(detect_day_ranges('VII-XII-2012'), (2012, 'VII-XII'))
        self.assertEqual(detect_day_ranges('V-XII-2012'), (2012, 'V-XII'))
        self.assertEqual(detect_day_ranges('X-XII-2012'), (2012, 'X-XII'))

    def test_days_2_ranges(self):
        '''
        TestDaysRanges:
        '''
        self.assertEqual(detect_month_pair('01-06-I'), (1, 1, 1, 6))

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
        rest = obk.take_second(['I', 5])
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
        rest = obk.take_first(['VI', 12])
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
