#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

KlasaOgolnaSzkieletuDat = dq_kw.KlasaOgolnaSzkieletuDat

class SzkieletDziennyDlaPoborow(KlasaOgolnaSzkieletuDat):
    def __init__(self, krt_pobor):
        '''
        SzkieletDziennyDlaPoborow:
        '''
        KlasaOgolnaSzkieletuDat.__init__(self)

class TestDziennegoSzkieletu(unittest.TestCase):
    def test_energii_szkieletowego_datownika(self):
        '''
        TestDziennegoSzkieletu:
        '''
