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

class LpFakturyRoku(object):
    def __init__(self):
        '''
        LpFakturyRoku:
        '''

    def ordinal_number(self, year):
        '''
        LpFakturyRoku:
        '''
        return 1

class TestLpFaktury(unittest.TestCase):
    def test_inserting_all(self):
        '''
        TestLpFaktury:
        '''
        obk = LpFakturyRoku()
        self.assertEqual(obk.ordinal_number(2010), 1)
