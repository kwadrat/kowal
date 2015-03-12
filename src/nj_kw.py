#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Wspólne elementy klas dla eksportu faktur energii elektrycznej oraz gazu W-5
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import jt_kw
import ir_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def wylicz_kl_pocz(qj_ta_kolumna, qj_liczba_lat):
    return 2 + qj_ta_kolumna * (qj_liczba_lat + 1)

CObjectNaming = ir_kw.CObjectNaming

class DaneWspolneObiektu(CObjectNaming):
    def __init__(self):
        '''
        DaneWspolneObiektu:
        '''
        CObjectNaming.__init__(self)
        self.dane_dla_roku = {}

    def wartosc_z_obiektu(self, fvk_rok, fvk_miesiac, qj_ta_kolumna):
        '''
        DaneWspolneObiektu:
        '''
        if fvk_rok in self.dane_dla_roku:
            wynik = self.dane_dla_roku[fvk_rok].wartosc_z_roku(fvk_miesiac, qj_ta_kolumna)
        else:
            wynik = 0
        return wynik

    def wpisz_nazwy_miesiecy(self, xwg, wiersz_pocz):
        '''
        DaneWspolneObiektu:
        '''
        xwg.tytul_miesiac(wiersz_pocz, liczba_wierszy=1)
        for nr_mies in jt_kw.numery_miesiecy:
            xwg.zapisz_nazwe_miesiaca(wiersz_pocz + nr_mies, nr_mies)

    def wpisz_nazwe_grupy_kolumn(self, xwg, wiersz_pocz, qj_ta_kolumna, kol_pocz):
        '''
        DaneWspolneObiektu:
        '''
        xwg.zapisz_l_polaczone_komorki(
            wiersz_pocz - 1,
            kol_pocz,
            self.qj_nazwy[qj_ta_kolumna],
            style_sel=None,
            )

    def wpisz_nazwy_lat(self, xwg, wiersz_pocz, kol_pocz, wszystkie_lata):
        '''
        DaneWspolneObiektu:
        '''
        for przes, etykieta in wszystkie_lata.enum_pairs():
            xwg.zapisz_flt(wiersz_pocz, kol_pocz + przes, etykieta, kl_miejsc=2)

    def przygotuj_moce_w_obiekcie(self, xwg, wiersz_pocz, qj_ta_kolumna, qj_liczba_lat, wszystkie_lata):
        '''
        DaneWspolneObiektu:
        '''
        kol_pocz = wylicz_kl_pocz(qj_ta_kolumna, qj_liczba_lat)
        self.wpisz_nazwe_grupy_kolumn(xwg, wiersz_pocz, qj_ta_kolumna, kol_pocz)
        self.wpisz_nazwy_lat(xwg, wiersz_pocz, kol_pocz, wszystkie_lata)
        self.wpisz_dane_do_tabelki(xwg, wiersz_pocz, kol_pocz, wszystkie_lata, qj_ta_kolumna)

    def obiektowy_a_arkusz(self, xwg, qj_liczba_lat, wszystkie_lata, qj_wszystkie):
        '''
        DaneWspolneObiektu:
        '''
        xwg.add_a_sheet(self.nazwa_dla_arkusza())
        xwg.zapisz_l_polaczone_komorki(
            0,
            0,
            self.nazwa_tego_obiektu,
            style_sel=None,
            )
        wiersz_pocz = 3
        self.wpisz_nazwy_miesiecy(xwg, wiersz_pocz)
        for qj_ta_kolumna in qj_wszystkie:
            self.przygotuj_moce_w_obiekcie(xwg, wiersz_pocz, qj_ta_kolumna, qj_liczba_lat, wszystkie_lata)

    def wpisz_dane_do_tabelki(self, xwg, wiersz_pocz, kol_pocz, wszystkie_lata, qj_ta_kolumna):
        '''
        DaneWspolneObiektu:
        '''
        for nr_kol_roku, fvk_rok in wszystkie_lata.enum_pairs():
            for fvk_miesiac in jt_kw.numery_miesiecy:
                wartosc_do_wpisania = self.wartosc_z_obiektu(fvk_rok, fvk_miesiac, qj_ta_kolumna)
                xwg.zapisz_flt(wiersz_pocz + fvk_miesiac, kol_pocz + nr_kol_roku, wartosc_do_wpisania, kl_miejsc=2)
