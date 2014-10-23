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

class MojPodnajemca(object):
    def __init__(self, dane_osoby, data_pocz, data_kon):
        '''
        MojPodnajemca:
        '''
        self.dane_osoby = dane_osoby
        self.data_pocz = data_pocz
        self.data_kon = data_kon

class TestJednegoPodnajemcy(unittest.TestCase):
    def test_jednego_podnajemcy(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca('KOWALSKI JAN', '2014-02-25', None)
