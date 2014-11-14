#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ut_kw
import dz_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class TxtXlrd(object):
    def __init__(self):
        '''
        TxtXlrd:
        '''

    def xldate_as_tuple(self, value, datemode):
        '''
        TxtXlrd:
        '''
        result = None
        date_full = dz_kw.extract_csv_full(value)
        if date_full is not None:
            result = tuple(date_full + [0])
        else:
            date_ymr = dz_kw.extract_csv_day(value)
            if date_ymr is not None:
                result = tuple(date_ymr + [0, 0, 0])
            else:
                hour_minute = dz_kw.extract_csv_hour(value)
                if hour_minute is not None:
                    result = tuple([0, 0, 0] + hour_minute + [0])
        return result

    def open_workbook(self, single_file):
        '''
        TxtXlrd:
        '''
        return ut_kw.TxtBook(single_file)

class TestXlrdInText(unittest.TestCase):
    def test_xlrd_in_text(self):
        '''
        TestXlrdInText:
        '''
        obk = TxtXlrd()
        value = '1:00'
        odp = obk.xldate_as_tuple(value, None)
        self.assertEqual(odp, (0, 0, 0, 1, 0, 0))
        value = '2:00'
        odp = obk.xldate_as_tuple(value, None)
        self.assertEqual(odp, (0, 0, 0, 2, 0, 0))
        value = '2014-06-01'
        odp = obk.xldate_as_tuple(value, None)
        self.assertEqual(odp, (2014, 6, 1, 0, 0, 0))
        value = '6/30/2014 23:45'
        odp = obk.xldate_as_tuple(value, None)
        self.assertEqual(odp, (2014, 6, 30, 23, 45, 0))
