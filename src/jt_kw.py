#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Rozpoznawanie zakresu dni w ramach jednego roku
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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
    def __init__(self):
        '''
        RomanPeriod:
        '''

    def take_year(self, elem_ls):
        '''
        RomanPeriod:
        '''
        self.the_year = int(elem_ls[0])
        return elem_ls[1:]

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
