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

def detect_my_days(slownik_wpisow):
    all_days = list(reduce(lambda x, y: x | y, map(lambda x: frozenset(x.keys()), slownik_wpisow.values())))
    all_days.sort()
    return all_days

class TestPrzetwarzaniaDni(unittest.TestCase):
    def test_przetwarzania_dni(self):
        '''
        TestPrzetwarzaniaDni:
        '''
        slownik_wpisow = {
            '2013-01': {1: 0, 9: 0, 11: 0, 28: 0, 29: 0, 30: 0, 31: 0},
            '2013-02': {1: 0, 9: 0, 12: 0, 28: 0},
            '2013-03': {1: 0, 9: 0, 13: 0, 28: 0, 29: 0, 30: 0, 31: 1},
            '2013-04': {1: 0, 9: 0, 10: 0, 28: 0, 29: 0, 30: 0},
            }
        self.assertEqual(detect_my_days(slownik_wpisow), [1, 9, 10, 11, 12, 13, 28, 29, 30, 31])
