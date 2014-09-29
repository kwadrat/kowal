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

def vx_wiersze(pocz, kon, krok=1):
    return list(xrange(pocz, kon + 1, krok))

class TestZakresuOdDo(unittest.TestCase):
    def test_zakresu_od_do(self):
        '''
        TestZakresuOdDo:
        '''
        self.assertEqual(vx_wiersze(2, 4), [2,3,4])
        self.assertEqual(vx_wiersze(2, 8, 2), [2,4,6,8])
