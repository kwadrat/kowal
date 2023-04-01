#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ckc_kw

def uporzadkuj_etykiety(kolejnosc_etykiet):
    indeks_etykieta = [(v, k) for k, v in ckc_kw.iteritems(kolejnosc_etykiet)]
    indeks_etykieta.sort()
    return list(map(lambda para: para[1], indeks_etykieta))


def psycopg2_zamien_na_napisy(lista_slownikow):
    wersja_napisowa = []
    kolejnosc_etykiet = lista_slownikow[0]._index
    uporzadkowane_etykiety = uporzadkuj_etykiety(kolejnosc_etykiet)
    wersja_napisowa.append(uporzadkowane_etykiety)
    for jeden_wiersz in lista_slownikow:
        wersja_napisowa.append(list(map(str, jeden_wiersz)))
    return wersja_napisowa


def wyznacz_potrzebne_miejsce(same_napisy):
    return list(map(max, list(map(lambda w_kolumnie: list(map(len, w_kolumnie)), zip(*same_napisy)))))


def wydrukuj_tabelke(same_napisy, wektor_rozmiarow):
    for nr_kol, jeden_wiersz in enumerate(same_napisy):
        print('|'.join(map(lambda para: para[0].ljust(para[1]), zip(jeden_wiersz, wektor_rozmiarow))))
        if not nr_kol:
            print('+'.join(map(lambda jeden_rozmiar: '-' * jeden_rozmiar, wektor_rozmiarow)))


def sztuka_tekstowa(lista_slownikow):
    lista = []
    ile = len(lista_slownikow)
    if ile == 1:
        napis_podsumowania = '1 row'
    else:
        napis_podsumowania = '%d rows' % ile
    if ile:
        same_napisy = psycopg2_zamien_na_napisy(lista_slownikow)
        wektor_rozmiarow = wyznacz_potrzebne_miejsce(same_napisy)
        wydrukuj_tabelke(same_napisy, wektor_rozmiarow)
    lista.append('(%s)\n' % napis_podsumowania)
    return ''.join(lista)


class TestBudowyTabelki(unittest.TestCase):
    def test_budowy_tabelki(self):
        '''
        TestBudowyTabelki:
        '''
        self.assertEqual(uporzadkuj_etykiety({'a': 0, 'b': 1, 'c': 2}), ['a', 'b', 'c'])
