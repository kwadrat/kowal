#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ib_kw
import rq_kw
import chg_kw
import sk_kw
import ei_kw

Skrawek = chg_kw.Skrawek

class SkrDomena(Skrawek):
    '''Wybór domeny działania programu:
    - finansowa (w złotych)
    - towarowa (w odpowiednich jednostkach, w jakich się mierzy zakupiony towar)
    '''
    def __init__(self):
        '''
        SkrDomena:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaDomena
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaDomena
            ##############################################################################

    def skh_pr_widzialny(self, prm_prez):
        '''
        SkrDomena:
        '''
        if prm_prez in rq_kw.DP_PotrzebujeDomene:
            return True
        elif prm_prez in rq_kw.DP_NiePotrzebujeDomeny:
            return False
        else:
            raise RuntimeError('Nieznana wartosc: %s' % repr(self.wartosc))

    def skh_widzialny(self, skp_okres):
        '''
        SkrDomena:
        Informujemy, czy potrzebujemy pola z wyborem domeny
        Wartość zwracana:
        True - potrzebne jest pole z wyborem domeny
        False - nie chcemy pola z wyborem domeny
        None - to zależy od prezentacji (tabela/wykres)
        '''
        if skp_okres in rq_kw.PR_PotrzebujeDomena:
            return True
        elif skp_okres in rq_kw.PR_NiePotrzebujeDomena:
            return False
        elif skp_okres in rq_kw.PR_MozeDomena:
            # Nierozstrzygnięte, zależy także od prezentacji (tabela - potrzebne,
            # wykres - niepotrzebne)
            return None
        else:
            raise RuntimeError('Nieznana wartosc: %s' % repr(skp_okres))

    def dm_potrzebna_domena(self):
        '''
        SkrDomena:
        '''
        wynik = self.skh_widzialny(self.prm_okres.wartosc)
        if wynik is None: # Jeszcze nierozstrzygnięte, czy pokazać domenę, dla raportu 1
            if self.elem_prez:
                wynik = self.skh_pr_widzialny(self.elem_prez.wartosc)
            else:
                # Nie mamy pokazywanej prezentacji, to pokazujemy domenę w Raporcie 1
                wynik = True
        return wynik

    def zbierz_html(self, tgk, dfb):
        '''
        SkrDomena:
        '''
        if self.dm_potrzebna_domena():
            if ib_kw.AimToObjectFieldName:
                ##############################################################################
                return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneDomeny)
                ##############################################################################
            else:
                ##############################################################################
                return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneDomeny)
                ##############################################################################
        else:
            return self.wartosc_ukryta()

class TestDomena(unittest.TestCase):
    def test_1_a(self):
        '''
        TestDomena:
        '''
        moj_elem = SkrDomena()
        moj_elem.skh_okres(None)
        moj_elem.skh_prez(None)
        self.assertEqual(moj_elem.skh_widzialny(rq_kw.PR_Brak), True)
        self.assertEqual(moj_elem.skh_widzialny(rq_kw.Dt_Miesiac), True)
        self.assertEqual(moj_elem.skh_widzialny(rq_kw.Dt_Rok), True)
        self.assertEqual(moj_elem.skh_widzialny(rq_kw.Dt_RapPierwszy), None)
        self.assertEqual(moj_elem.skh_widzialny(rq_kw.Dt_RapDrugi), False)
        self.assertTrue(moj_elem.skh_pr_widzialny(rq_kw.DP_Wykres))
        self.assertTrue(moj_elem.skh_pr_widzialny(rq_kw.PoleNN))
        self.assertFalse(moj_elem.skh_pr_widzialny(rq_kw.DP_Tabela))
