#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
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

class SzkieletDatDlaFakturMiesLat(KlasaSzkieletuDat):
    def __init__(self):
        '''
        SzkieletDatDlaFakturMiesLat:
        '''
        KlasaSzkieletuDat.__init__(self)

    def mam_dat_na_dluzszy_rok(self):
        '''
        SzkieletDatDlaFakturMiesLat:
        Górne, dłuższe kreski dla poszczególnych faktur (tylko ciągłych)
        Liczba miesięcy dla ciągłych faktur miesięcznych
        '''
        return self.liczba_paskow() == rq_kw.RokDluzszy

class TestSzkieletuDatDlaFakturMiesLat(unittest.TestCase):
    def test_szkieletu_dat_dla_faktur_mies_lat(self):
        '''
        TestSzkieletuDatDlaFakturMiesLat:
        '''
        obk = SzkieletDatDlaFakturMiesLat()
