#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ib_kw
import rq_kw
import chg_kw
import sk_kw
import ei_kw

Skrawek = chg_kw.Skrawek


class SkrOkres(Skrawek):
    '''Wybór okresu:
       - w latach (całe lata pokazujemy na wykresie)
       - rok (tylko konkretny rok)
       - Raport 1
       - Raport 2
    '''

    def __init__(self):
        '''
        SkrOkres:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaOkres
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaOkres
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrOkres:
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneOkresu)
            ##############################################################################
        else:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneOkresu)
            ##############################################################################
