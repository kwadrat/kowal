#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FabrykaLicznikow(object):
    '''
    Numeracja poszczególnych faktur
    '''

    def __init__(self, wartosc_poczatkowa):
        '''
        FabrykaLicznikow:
        '''
        self.numer_pierwszego_wolnego_elementu = wartosc_poczatkowa
        self.liczba_porz_obiektu_na_obiekt = {}

    def przydziel_kolejny_numer(self, obiekt_elementu):
        '''
        FabrykaLicznikow:
        '''
        moj_numer = self.numer_pierwszego_wolnego_elementu
        self.liczba_porz_obiektu_na_obiekt[moj_numer] = obiekt_elementu
        self.numer_pierwszego_wolnego_elementu += 1  # Przygotuj się na następny element
        return moj_numer
