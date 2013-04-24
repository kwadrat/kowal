#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lp_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class HourServer:
    def __init__(self, start_col, column_index):
        '''
        HourServer:
        '''
        self.column_index = column_index
        self.canonical_hour = lp_kw.change_to_full_hour(self.column_index)
        self.col_in_sheet = start_col + self.column_index
        self.header_for_hour_column = lp_kw.describe_column(column_index)

    def __repr__(self):
        '''
        HourServer:
        '''
        return 'HS(%s)' % self.header_for_hour_column

def prepare_time_headers(start_col):
    all_time_columns = []
    for column_index in xrange(24):
        all_time_columns.append(HourServer(start_col, column_index))
    return all_time_columns

class TestHourPatterns(unittest.TestCase):
    pass
