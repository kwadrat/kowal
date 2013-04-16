#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

midnight_hour_wrap = {24: 0}

def describe_column(column_index):
    hour_number = column_index + 1
    hour_number = midnight_hour_wrap.get(hour_number, hour_number)
    return '%02d:00' % hour_number

class HourServer:
    def __init__(self, column_index):
        '''
        HourServer:
        '''
        self.column_index = column_index

def prepare_time_headers():
    all_time_columns = []
    for column_index in xrange(24):
        all_time_columns.append(HourServer(column_index))
    return all_time_columns

class TestHourPatterns(unittest.TestCase):
    def test_hour_patterns(self):
        '''
        TestHourPatterns:
        '''
        self.assertEqual(describe_column(0), '01:00')
        self.assertEqual(describe_column(1), '02:00')
        self.assertEqual(describe_column(22), '23:00')
        self.assertEqual(describe_column(23), '00:00')
