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

def prepare_time_headers(start_col):
    all_time_columns = []
    for column_index in xrange(24):
        all_time_columns.append(lp_kw.HourServer(start_col, column_index))
    return all_time_columns

class TestHourPatterns(unittest.TestCase):
    pass
