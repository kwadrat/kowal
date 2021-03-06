#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ez_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

KlasaSzkieletuDat = ez_kw.KlasaSzkieletuDat

class SzkieletDatDlaZuzycia(KlasaSzkieletuDat):
    def __init__(self):
        '''
        SzkieletDatDlaZuzycia:
        '''
        KlasaSzkieletuDat.__init__(self)

    def poczatki_miesiecy(self):
        '''
        SzkieletDatDlaZuzycia:
        '''
        return self.szkielet_dat

class TestSzkieletuDatDlaZuzycia(unittest.TestCase):
    def test_szkieletu_dat_dla_zuzycia(self):
        '''
        TestSzkieletuDatDlaZuzycia:
        '''
        obk = SzkieletDatDlaZuzycia()
        obk.przypisz_dla_roku_szkielet
