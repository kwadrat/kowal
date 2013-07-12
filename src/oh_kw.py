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
    def __init__(self, lp_miejsca):
        '''
        SimpleDWN:
        '''
        self.lp_miejsca = lp_miejsca

    def mam_wykres_zbiorczy(self):
        '''
        SimpleDWN:
        '''
        return 1

class TestProstychDanych(unittest.TestCase):
    def test_prostych_danych(self):
        '''
        TestProstychDanych:
        '''
        obk = SimpleDWN(0)
        self.assertTrue(obk.mam_wykres_zbiorczy())
