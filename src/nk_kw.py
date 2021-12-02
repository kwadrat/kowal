#!/usr/bin/python
# -*- coding: UTF-8 -*-


class DaneWspolneDlaRoku(object):
    def __init__(self):
        '''
        DaneWspolneDlaRoku:
        '''
        self.dane_dla_miesiaca = {}

    def wartosc_z_roku(self, fvk_miesiac, qj_ta_kolumna):
        '''
        DaneWspolneDlaRoku:
        '''
        if fvk_miesiac in self.dane_dla_miesiaca:
            wynik = self.dane_dla_miesiaca[fvk_miesiac].wartosc_z_miesiaca(qj_ta_kolumna)
        else:
            wynik = 0
        return wynik
