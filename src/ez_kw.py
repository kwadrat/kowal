#!/usr/bin/python
# -*- coding: UTF-8 -*-

import dn_kw
import dq_kw

KlasaOgolnaSzkieletuDat = dq_kw.KlasaOgolnaSzkieletuDat


class KlasaSzkieletuDat(KlasaOgolnaSzkieletuDat):
    def __init__(self):
        '''
        KlasaSzkieletuDat:
        '''
        KlasaOgolnaSzkieletuDat.__init__(self)
        self.szkielet_dat = []

    def skrajne_daty(self):
        '''
        KlasaSzkieletuDat:
        '''
        return self.szkielet_pocz, self.szkielet_kon

    def kolejne_dni_szkieletu(self):
        '''
        KlasaSzkieletuDat:
        '''
        return range(self.szkielet_pocz, self.szkielet_kon)

    def rok_poczatku(self):
        '''
        KlasaSzkieletuDat:
        '''
        return dn_kw.RokDnia(self.szkielet_pocz)
