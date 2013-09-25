#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Nazwy jednostek
'''

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

# Kilowatogodzin
Jedn_kWh = 'kWh'
Jedn_kWtow = 'kW'
Jedn_zlotowki = 'zł'

def nawiasy_kwadratowe(jednostka):
    return '[%s]' % jednostka

Jedn_k_zlotowki = nawiasy_kwadratowe(Jedn_zlotowki)

class TestUnitNames(unittest.TestCase):
    def test_unit_names(self):
        '''
        TestUnitNames:
        '''
        self.assertEqual(Jedn_kWh, 'kWh')
        self.assertEqual(Jedn_kWtow, 'kW')
        self.assertEqual(Jedn_zlotowki, 'zł')
        self.assertEqual(Jedn_k_zlotowki, '[zł]')
