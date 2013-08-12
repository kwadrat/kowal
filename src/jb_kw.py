#!/usr/bin/python
# -*- coding: UTF-8 -*-

dymek_bez_tresci = ''

class JedenOdcinekBazowy(object):
    '''Jeden odcinek bazowy, zawierający:
    - numer dnia początku okresu
    - numer dnia końca okresu
    - słownik identyfikatorów faktur (numerów l.p. faktur)
    '''
    def __init__(self, pocz, kon, slownik_qm):
        '''
        JedenOdcinekBazowy:
        '''
        self.pocz = pocz
        self.kon = kon
        self.slownik_qm = slownik_qm

    def przedzial_ks(self):
        '''
        JedenOdcinekBazowy:
        '''
        return ((self.pocz, self.kon), self.slownik_qm)

    def formatted_pkks(self):
        '''
        JedenOdcinekBazowy:
        '''
        return (self.pocz, self.kon, self.slownik_qm)

    def get_pk(self):
        '''
        JedenOdcinekBazowy:
        '''
        return (self.pocz, self.kon)

    def get_pocz(self):
        '''
        JedenOdcinekBazowy:
        '''
        return self.pocz

    def get_kon(self):
        '''
        JedenOdcinekBazowy:
        '''
        return self.kon

    def pseudoodcinek_etykiety_roku(self):
        '''
        JedenOdcinekBazowy:
        '''
        return self.pocz is None and self.kon is None

    def dymek_dla_slupka(self, tgk, chce_bez_tresci):
        '''
        JedenOdcinekBazowy:
        '''
        if self.pseudoodcinek_etykiety_roku():
            wynik = dymek_bez_tresci
        elif chce_bez_tresci:
            wynik = dymek_bez_tresci
        else:
            wynik = self.slownik_qm.polaczony_dymek()
        return wynik
