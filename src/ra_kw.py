#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ib_kw
import rq_kw
import chh_kw
import chg_kw
import sk_kw
import ei_kw

Skrawek = chg_kw.Skrawek


class SkrARok(Skrawek):
    '''Wybór początkowego roku
    '''
    def __init__(self):
        '''
        SkrARok:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaARok
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaARok
            ##############################################################################

    def skh_widzialny(self, skp_okres):
        '''
        SkrARok:
        '''
        if skp_okres in rq_kw.PR_PotrzebujeARok:
            return True
        elif skp_okres in rq_kw.PR_NiePotrzebujeARok:
            return False
        else:
            raise RuntimeError('Nieznana wartosc: %s' % repr(skp_okres))

    def zbierz_html(self, tgk, dfb):
        '''
        SkrARok:
        '''
        if self.skh_widzialny(self.prm_okres.wartosc):
            if ib_kw.AimToObjectFieldName:
                ##############################################################################
                result = sk_kw.ListWyboruOgolna(tgk, self.moje_pole, chh_kw.MozliweLataDlaARok)
                ##############################################################################
            else:
                ##############################################################################
                result = sk_kw.ListWyboruOgolna(tgk, self.moje_pole, chh_kw.MozliweLataDlaARok)
                ##############################################################################
                return result
        else:
            return self.wartosc_ukryta()


class TestARok(unittest.TestCase):
    def test_1_a(self):
        '''
        TestARok:
        '''
        moj_elem = SkrARok()
        moj_elem.skh_okres(None)
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.PR_Brak))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Miesiac))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Rok))
        self.assertTrue(moj_elem.skh_widzialny(rq_kw.Dt_RapPierwszy))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_RapDrugi))
