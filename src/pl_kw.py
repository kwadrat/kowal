#!/usr/bin/python
# -*- coding: UTF-8 -*-

import po_kw

PozycjeOgolne = po_kw.PozycjeOgolne

class PozycjeLicznikowe(PozycjeOgolne):
    def __init__(self, etykieta, slownik_poczatkowy=None):
        '''
        PozycjeLicznikowe:
        '''
        PozycjeOgolne.__init__(self, etykieta, slownik_poczatkowy)

    def __repr__(self):
        '''
        PozycjeLicznikowe:
        '''
        return self.wzorzec_repr('PozycjeLicznikowe')

    def podaj_ciag(self):
        '''
        PozycjeLicznikowe:
        '''
        return self.klucze_chronologicznie()

    def zwroc_drugiego(self, klucz):
        '''
        PozycjeLicznikowe:
        '''
        return self.pobierz_element(klucz)
