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

def describe_column():
    return '01:00'

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
        self.assertEqual(describe_column(), '01:00')

