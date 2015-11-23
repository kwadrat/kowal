#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import rq_kw
import chg_kw
import sk_kw
import ei_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

Skrawek = chg_kw.Skrawek

class SkrAktWsz(Skrawek):
    '''Wybór aktywnych (ważnych) obiektów lub wszystkich (łącznie z testowymi)
    '''

    def __init__(self):
        '''
        SkrAktWsz:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaAktWsz
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaAktWsz
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrAktWsz:
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneAktWsz)
            ##############################################################################
        else:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneAktWsz)
            ##############################################################################

class TestAktWsz(unittest.TestCase):
    def test_1_a(self):
        '''
        TestAktWsz:
        '''
        moj_elem = SkrAktWsz()
