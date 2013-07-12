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

class SimpleDWN:
    def __init__(self, lp_wykresu):
        '''
        SimpleDWN:
        '''
        self.lp_miejsca = lp_wykresu

class TestProstychDanych(unittest.TestCase):
    def test_prostych_danych(self):
        '''
        TestProstychDanych:
        '''
