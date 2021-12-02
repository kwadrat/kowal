#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


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
