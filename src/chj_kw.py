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

def tq_poczatek_roku(ih_rok):
    return "'%d-01-01'" % ih_rok

def tq_koniec_roku(ih_rok):
    return "'%d-12-31'" % ih_rok

class TestYearBorders(unittest.TestCase):
    def test_year_borders(self):
        '''
        TestYearBorders:
        '''
        self.assertEqual(tq_poczatek_roku(2012), "'2012-01-01'")
        self.assertEqual(tq_koniec_roku(2012), "'2012-12-31'")
