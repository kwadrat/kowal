#!/usr/bin/python
# -*- coding: UTF-8 -*-

import rq_kw

ustawienia_globalne = {}
ustawienia_globalne['Tymczasowo_zamknij_Excela_na_koniec'] = 1
ustawienia_globalne['Tymczasowo_podglad_wydruku'] = 0
ustawienia_globalne['Tymczasowo_bierz_poprzedni_zestaw_faktur'] = 0
ustawienia_globalne['Chcemy_wydruk_od_razu_na_drukarke'] = 0

def ramkowy_komunikat(napis):
    ile_napisu = len(napis)
    znak = '*'
    wypelnienie = ' '
    belka = znak * (ile_napisu + 6)
    wolne = znak + wypelnienie * (ile_napisu + 4) + znak
    print belka
    print wolne
    print ''.join([
      znak, wypelnienie, wypelnienie, napis, wypelnienie, wypelnienie, znak])
    print wolne
    print belka

def informuj_o_wysylaniu_do_testowego():
    if not rq_kw.zst_wysyla_energie_na_prod:
        ramkowy_komunikat('Pracujesz w trybie testowym')
        ramkowy_komunikat('Faktury nie pojawia sie w systemie produkcyjnym')
