#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import oa_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KreskiWykresu(object):
    def __init__(self):
        '''
        KreskiWykresu:
        '''
        self.draw_line = []

    def append(self, krotka):
        '''
        KreskiWykresu:
        '''
        self.draw_line.append(krotka)

class TestKresekWykresu(unittest.TestCase):
    def test_kresek_wykresu(self):
        '''
        TestKresekWykresu:
        '''
        obk = KreskiWykresu()
        obk.append
