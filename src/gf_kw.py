#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import gc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

PoboroweOgolneSlupki = gc_kw.PoboroweOgolneSlupki

class PoboroweMiesieczneSlupki(PoboroweOgolneSlupki):
    def __init__(self, tgk, aqr, dnw):
        '''
        PoboroweMiesieczneSlupki:
        '''
        PoboroweOgolneSlupki.__init__(self, tgk, aqr, dnw)

class TestPoborowychMiesiecznychSlupkow(unittest.TestCase):
    def test_poborowych_miesiecznych_slupkow(self):
        '''
        TestPoborowychMiesiecznychSlupkow:
        '''
