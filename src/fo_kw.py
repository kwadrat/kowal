#!/usr/bin/python
# -*- coding: UTF-8 -*-


class SpecGrupyWykFak(object):
    '''
    Dane współdzielone przez grupę wykresów lub grupę faktur
    Paczka zwracana jako:
    - wykaz liczników, dla których pokazujemy wykresy
    - wykaz faktur dla danego licznika
    '''
    def __init__(self, tfi_medium, lista_slownikow):
        '''
        SpecGrupyWykFak:
        '''
        self.tfi_medium = tfi_medium
        self.lista_wewn = lista_slownikow

    def podaj_twoja_liste(self):
        '''
        SpecGrupyWykFak:
        '''
        return self.lista_wewn

    def dolacz_na_koncu(self, dodatkowy):
        '''
        SpecGrupyWykFak:
        '''
        druga_lista = dodatkowy.podaj_twoja_liste()
        self.lista_wewn.extend(druga_lista)

    def akt_dlugosc(self):
        '''
        SpecGrupyWykFak:
        '''
        return len(self.lista_wewn)
