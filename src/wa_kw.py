#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ib_kw
import rq_kw
import chg_kw
import sk_kw
import ei_kw

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
        self.assertEqual(moj_elem.wartosc, None)
