#!/usr/bin/python
# -*- coding: UTF-8 -*-


class MojPisak(object):

    '''
    Zbiera informacje o wartościach maksymalnych w raportach 1 i 2, aby
    ładnie przeskalować wszystkie wykresy słupkowe.
    '''
    def __init__(self, szrp):
        '''
        MojPisak:
        '''
        self.szrp = szrp
        self.lista_linii_pisaka = []

    def liczba_linii(self):
        '''
        MojPisak:
        '''
        return len(self.lista_linii_pisaka)

    def pobierz_liste_linii(self):
        '''
        MojPisak:
        '''
        return self.lista_linii_pisaka

    def pobierz_linie_numer(self, nr):
        '''
        MojPisak:
        '''
        return self.lista_linii_pisaka[nr]

    def dodaj_wpis(self, element):
        '''
        MojPisak:
        '''
        self.lista_linii_pisaka.append(element)
        self.szrp.kolejna_linia(element)
