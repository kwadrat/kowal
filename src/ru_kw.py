#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ib_kw
import dn_kw
import chg_kw
import ei_kw
import ro_kw

Skrawek = chg_kw.Skrawek


class SkrZuzRok(Skrawek):
    '''Wybór roku dla analizy zużyć.
    '''

    def __init__(self):
        '''
        SkrZuzRok:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaRok
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaRok
            ##############################################################################

    def analiza_parametrow(self, tgk, dfb):
        '''
        SkrZuzRok:
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.wartosc = tgk.qparam.get(self.moje_pole, None)
            ##############################################################################
        else:
            ##############################################################################
            self.wartosc = tgk.qparam.get(self.moje_pole, None)
            ##############################################################################
        if self.wartosc == None:
            # Domyślnie pokazujemy aktualny rok
            self.wartosc = dn_kw.RokTeraz()
        return self.wartosc != None

    def zbierz_html(self, tgk, dfb):
        '''
        SkrZuzRok:
        '''
        return ro_kw.ListaWyboruRoku(tgk)


class TestZuzRok(unittest.TestCase):
    def test_1_a(self):
        '''
        TestZuzRok:
        '''
        moj_elem = SkrZuzRok()
