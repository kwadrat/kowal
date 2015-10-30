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

class PredefinedEnergyCoefficient(object):
    def __init__(self, moc_optymalna, moc_przylaczeniowa, taryfa):
        '''
        PredefinedEnergyCoefficient:
        '''
        self.moc_optymalna = moc_optymalna
        self.moc_przylaczeniowa = moc_przylaczeniowa
        self.taryfa = taryfa

class TestEnergyCoefficients(unittest.TestCase):
    def test_energy_coefficients(self):
        '''
        TestEnergyCoefficients:
        '''
        obk = PredefinedEnergyCoefficient(42.0, 160.0, 'C21')
        self.assertEqual(obk.moc_optymalna, 42.0)
        self.assertEqual(obk.moc_przylaczeniowa, 160.0)
        self.assertEqual(obk.taryfa, 'C21')
