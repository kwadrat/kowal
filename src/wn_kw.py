#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Słownik przedziałów czasowych
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
import lm_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def pokaz_kwote(kwota):
    '''
    Dla równego formatowania kwot z groszami
    '''
    return '%8.2f' % kwota

def bledne_duplikaty(lista):
    '''
    Lista jest posortowana, nie powinno być
    duplikatów, bo to oznacza błąd w algorytmie - funkcja wywróci
    program, jeśli znajdą się duplikaty
    '''
    if len(lista) > 1: # Tylko wtedy duplikaty mogą istnieć
        akt = lista[0]
        for nast in lista[1:]:
            if akt == nast:
                raise RuntimeError('Duplikat: %s %s' % (repr(akt), repr(lista)))
            akt = nast # Przejście na następny element

class KlasaSlownika(object):
    def __init__(self):
        '''
        KlasaSlownika:
        '''
        self.vz_slownik = {}
        self.vz_kwota = lm_kw.wartosc_zero_z_bazy
        self.umw_wartosc_s_qm = None
        self.przekroczenie_b_umw = 0

    def jh_ustaw_kwt_qm(self, vz_kwota):
        '''
        KlasaSlownika:
        '''
        self.vz_kwota = vz_kwota

    def jh_ustaw_s_qm(self, umw_wartosc_s_qm):
        '''
        KlasaSlownika:
        '''
        self.umw_wartosc_s_qm = umw_wartosc_s_qm

    def jh_keys(self):
        '''
        KlasaSlownika:
        '''
        return self.vz_slownik.keys()

    def jh__getitem__(self, key):
        '''
        KlasaSlownika:
        '''
        return self.vz_slownik[key]

    def jh__setitem__(self, key, value):
        '''
        KlasaSlownika:
        '''
        self.vz_slownik[key] = value

    def jh_values(self):
        '''
        KlasaSlownika:
        '''
        return self.vz_slownik.values()

    def jh_kv_pairs(self):
        '''
        KlasaSlownika:
        '''
        return self.vz_slownik.iteritems()

    def jh_na_poczatek_puste(self, key):
        '''
        KlasaSlownika:
        '''
        tmp_slownik = self.vz_slownik.get(key)
        if tmp_slownik is None:
            tmp_slownik = self.vz_slownik[key] = []
        return tmp_slownik

    def jh_sprawdz_powielenie(self):
        '''
        KlasaSlownika:
        '''
        for lista_b in self.vz_slownik.values():
            lista_b.sort()
            bledne_duplikaty(lista_b)

    def dymek_dla_listy_faktur(self):
        '''
        KlasaSlownika:
        '''
        lista_numerow = []
        for lista_lp_fkt in self.vz_slownik.values():
            lista_numerow.extend(lista_lp_fkt)
        lista_numerow.sort()
        if len(lista_numerow) > 1:
            tmp_pocz = 'Faktury: '
        else:
            tmp_pocz = 'Faktura: '
        return tmp_pocz + ', '.join(map(str, lista_numerow))

    def __repr__(self):
        '''
        KlasaSlownika:
        '''
        return 'KlS(%s, %s, %d, %s)' % (pokaz_kwote(self.vz_kwota), self.umw_wartosc_s_qm, self.przekroczenie_b_umw, self.vz_slownik)

    def jh_powieksz(self, slownik_qm):
        '''
        KlasaSlownika:
        '''
        klucze = slownik_qm.jh_keys()
        for klucz in klucze:
            tmp_slownik = self.jh_na_poczatek_puste(klucz)
            tmp_slownik.extend(slownik_qm.jh__getitem__(klucz))
            self.vz_kwota += slownik_qm.vz_kwota

    def jh_kwota(self):
        '''
        KlasaSlownika:
        '''
        if rq_kw.TwoPlacesMoneyVariablePlacesAmount:
            ##############################################################################
            return self.vz_kwota, miejsc
            ##############################################################################
        else:
            ##############################################################################
            return self.vz_kwota
            ##############################################################################

    def ustaw_umw(self):
        '''
        KlasaSlownika:
        '''
        if self.umw_wartosc_s_qm is not None and self.jh_kwota() > self.umw_wartosc_s_qm:
            self.przekroczenie_b_umw = 1

    def tekst_dla_przekroczenia(self):
        '''
        KlasaSlownika:
        '''
        wynik = ''
        if self.umw_wartosc_s_qm is not None:
            wynik = '%(nwln)sMoc umowna: %(emu)s%(nwln)sMoc pobrana: %(emp)s' % dict(
                emu = pokaz_kwote(self.umw_wartosc_s_qm),
                emp = pokaz_kwote(self.jh_kwota()),
                nwln = ' ',
                )
        return wynik

    def polaczony_dymek(self):
        '''
        KlasaSlownika:
        '''
        return self.dymek_dla_listy_faktur() + self.tekst_dla_przekroczenia()

    def get_max_kwota(self):
        '''
        KlasaSlownika:
        '''
        if self.umw_wartosc_s_qm is None:
            wynik = self.jh_kwota()
        else:
            wynik = max(self.jh_kwota(), self.umw_wartosc_s_qm)
        return wynik

class TestKlasySlownika(unittest.TestCase):
    def test_klasy_slownika(self):
        '''
        TestKlasyNakladki:
        '''
        obk = KlasaSlownika()
        obk.jh_values()
