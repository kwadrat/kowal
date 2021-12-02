#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ib_kw
import hj_kw
import rq_kw
import dn_kw
import chh_kw
import chg_kw
import sk_kw
import ei_kw
import oy_kw

Skrawek = chg_kw.Skrawek

class SkrWybranyRok(Skrawek):
    '''Wybór początkowego roku
    '''
    def __init__(self):
        '''
        SkrWybranyRok:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaCRok
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaCRok
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrWybranyRok:
        '''
        initial_year_values = chh_kw.ParowaneLataDanych
        czy_wszystkie = 1
        initial_year_values = oy_kw.rj_wstaw_surowa_kreske_jako_pierwsze(initial_year_values, czy_wszystkie)
        initial_year_values = oy_kw.rj_adjoin_all_in_one(initial_year_values)
        initial_year_values = hj_kw.tekstowe_indeksy(initial_year_values)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            result = sk_kw.ListWyboruOgolna(tgk, self.moje_pole, initial_year_values)
            ##############################################################################
        else:
            ##############################################################################
            result = sk_kw.ListWyboruOgolna(tgk, self.moje_pole, initial_year_values)
            ##############################################################################
            return result
