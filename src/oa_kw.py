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

# Każdy dzień będzie jako 2 punkty - wtedy 365 dni w roku
# zmieści się w poziomie na ekranie 1024x768
sk_pelny_obraz = 1250

class TestRozmiaruObrazu(unittest.TestCase):
    def test_rozmiaru_obrazu(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(sk_pelny_obraz, 1250)
