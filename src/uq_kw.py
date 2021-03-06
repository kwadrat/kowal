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

class BagFieldSet(object):
    def __init__(self,
            pole_dla_ilosci,
            pole_dla_kwoty,
            pole_dla_mocy,
            pole_dla_energii,
            ):
        '''
        BagFieldSet:
        '''
        self.pole_dla_ilosci = pole_dla_ilosci
        self.pole_dla_kwoty = pole_dla_kwoty
        self.pole_dla_mocy = pole_dla_mocy
        self.pole_dla_energii = pole_dla_energii

class TestBagFieldData(unittest.TestCase):
    def test_bag_field_data(self):
        '''
        TestBagFieldData:
        '''
        obk = BagFieldSet(
            pole_dla_ilosci='i',
            pole_dla_kwoty='k',
            pole_dla_mocy='m',
            pole_dla_energii='e',
            )
        self.assertEqual(obk.pole_dla_ilosci, 'i')
        self.assertEqual(obk.pole_dla_kwoty, 'k')
        self.assertEqual(obk.pole_dla_mocy, 'm')
        self.assertEqual(obk.pole_dla_energii, 'e')
