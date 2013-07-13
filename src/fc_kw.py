#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class ZwracanePola(object):
    def __init__(self):
        '''
        ZwracanePola:
        '''
        self.qs_kolejka = []

    def extend(self, lista):
        '''
        ZwracanePola:
        '''
        self.qs_kolejka.extend(lista)

    def append(self, elem):
        '''
        ZwracanePola:
        '''
        self.qs_kolejka.append(elem)

    def polaczone_przecinkami(self):
        '''
        ZwracanePola:
        '''
        return hj_kw.Poprzecinkuj(self.qs_kolejka)

class TestZwracanychPol(unittest.TestCase):
    def test_zwracanych_pol(self):
        '''
        TestZwracanychPol:
        '''
        obk = ZwracanePola()
        obk.append('a')
        self.assertEqual(obk.polaczone_przecinkami(), 'a')
        obk.extend(['b', 'c'])
        self.assertEqual(obk.polaczone_przecinkami(), 'a,b,c')
