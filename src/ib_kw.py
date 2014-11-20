#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Nazwa pola: nazwa właściwa, przedrostek
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

class FieldDesc(object):
    def __init__(self, moje_pole, fs_prefix):
        '''
        FieldDesc:
        '''
        self.moje_pole = moje_pole
        self.fs_prefix = fs_prefix
        if self.fs_prefix is None:
            self.official_name = self.moje_pole
        else:
            self.official_name = self.fs_prefix + self.moje_pole

class TestMojegoPola(unittest.TestCase):
    def test_mojego_pola(self):
        '''
        TestMojegoPola:
        '''
        obk = FieldDesc('pole', 'przed_')
        self.assertEqual(obk.moje_pole, 'pole')
        self.assertEqual(obk.fs_prefix, 'przed_')
        self.assertEqual(obk.official_name, 'przed_pole')

    def test_bez_przedrostka(self):
        '''
        TestMojegoPola:
        '''
        obk = FieldDesc('proste', None)
        self.assertEqual(obk.moje_pole, 'proste')
        self.assertEqual(obk.fs_prefix, None)
        self.assertEqual(obk.official_name, 'proste')
