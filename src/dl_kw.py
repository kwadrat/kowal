#!/usr/bin/python
# -*- coding: UTF-8 -*-

import lm_kw


def dodaj_z_listy(lista_slownikow, lista_kluczy):
    suma_dzl = lm_kw.wartosc_zero_globalna
    for lokalny_slownik in lista_slownikow:
        dodatkowa_kwota = lm_kw.decimal_suma_wybranych_wpisow_slownika(lokalny_slownik, lista_kluczy)
        suma_dzl += dodatkowa_kwota
    return suma_dzl
