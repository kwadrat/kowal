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

class BuildingIndicator(object):
    def __init__(self, lokalny_the_building):
        '''
        BuildingIndicator:
        '''
        self.lokalny_the_building = lokalny_the_building
        self.lokalny_mam_realny_obiekt = self.lokalny_the_building is not None

    def zrob_z_pustego_budynku_zero(self):
        '''
        BuildingIndicator:
        '''
        if self.lokalny_mam_realny_obiekt:
            wartosc = self.lokalny_the_building
        else:
            wartosc = 0
        return wartosc

class TestOpisuBudynku(unittest.TestCase):
    def test_opisu_a_budynku(self):
        '''
        TestOpisuBudynku:
        '''
        lokalny_the_building = None
        obk = BuildingIndicator(lokalny_the_building)
        self.assertEqual(obk.lokalny_the_building, None)
        self.assertEqual(obk.lokalny_mam_realny_obiekt, 0)
        self.assertEqual(obk.zrob_z_pustego_budynku_zero(), 0)

    def test_opisu_b_budynku(self):
        '''
        TestOpisuBudynku:
        '''
        lokalny_the_building = 4
        obk = BuildingIndicator(lokalny_the_building)
        self.assertEqual(obk.lokalny_the_building, 4)
        self.assertEqual(obk.lokalny_mam_realny_obiekt, 1)
        self.assertEqual(obk.zrob_z_pustego_budynku_zero(), 4)
