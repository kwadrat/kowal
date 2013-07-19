#!/usr/bin/python
# -*- coding: UTF-8 -*-

class DomenowaKlasaIlosci(object):
    def wyznacz_mi_pola(self, grupa_kolumn):
        '''
        DomenowaKlasaIlosci:
        '''
        return grupa_kolumn.rh_kolumny + grupa_kolumn.kol_ilsc

    def zmien_ilosc_dla_brylantu(self, bnh):
        '''
        DomenowaKlasaIlosci:
        '''
        bnh.ustaw_ilosc()

    def teksty_domeny(self, tmp_wkrs, jedn_mocy):
        '''
        DomenowaKlasaIlosci:
        '''
        return tmp_wkrs.pole_jedn, 'ilość'

    def przedstaw_pole_sumy(self, pole_dla_ilosci, pole_dla_kwoty, pole_dla_mocy):
        '''
        DomenowaKlasaIlosci:
        '''
        return pole_dla_ilosci

    def zawsze_moge_dodac_mr(self):
        '''
        DomenowaKlasaIlosci:
        '''
        return 1
