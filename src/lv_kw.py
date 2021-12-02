#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ib_kw
import lw_kw
import chg_kw
import sk_kw
import ei_kw

Skrawek = chg_kw.Skrawek

class SkrPobor(Skrawek):
    '''Wybór poboru:
       - energii
       - mocy
    '''

    def __init__(self, fs_prefix=None):
        '''
        SkrPobor:
        '''
        Skrawek.__init__(self, fs_prefix)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaPobor
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaPobor
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrPobor:
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, lw_kw.DanePoboru)
            ##############################################################################
        else:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, lw_kw.DanePoboru)
            ##############################################################################
