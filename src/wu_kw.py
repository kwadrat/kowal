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

    def przedstaw_pole_sumy(self, bfs):
        '''
        DomenowaKlasaIlosci:
        '''
        return bfs.pole_dla_ilosci

    def zawsze_moge_dodac_mr(self):
        '''
        DomenowaKlasaIlosci:
        '''
        return 1

    def moge_dodac_prog_mocy(self):
        '''
        DomenowaKlasaIlosci:
        '''
        return 0
