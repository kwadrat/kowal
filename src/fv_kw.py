#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def vx_porz(litera):
    return ord(litera.upper()) - ord('A') + 1

def vx_litera(liczba):
    if 1 <= liczba <= 26:
        return chr(ord('A') + liczba - 1)
    else:
        raise RuntimeError('Poza zakresem?: %s' % repr(liczba))

def vx_lt(napis):
    '''
    Numer kolejny litery, aby łatwiej wpisywać adresy w Excelu
    '''
    ile = len(napis)
    if ile == 1:
        wynik = vx_porz(napis)
    elif ile == 2:
        wynik = vx_porz(napis[0]) * 26 + vx_porz(napis[1])
    else:
        raise RuntimeError('Nieobslugiwany napis kolumny: %s' % repr(napis))
    return wynik

def vx_rev_lt(liczba):
    if liczba > 26:
        a, b = divmod(liczba - 1, 26)
        wynik = vx_rev_lt(a) + vx_litera(b + 1)
    else:
        wynik = vx_litera(liczba)
    return wynik
