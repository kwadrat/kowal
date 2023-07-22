#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import hj_kw
import ek_kw
import us_kw
import li_kw
import ll_kw
import po_kw

licznik_inst_list = li_kw.LicznikInstancji('lista')

ListaLubSlownikOgolnie = ll_kw.ListaLubSlownikOgolnie


class TypowaLista(ListaLubSlownikOgolnie):
    def __init__(self, etykieta):
        '''
        TypowaLista:
        '''
        ListaLubSlownikOgolnie.__init__(self, licznik_inst_list, etykieta)
        self.poczatkowe_ustawienia()

    def poczatkowe_ustawienia(self):
        '''
        TypowaLista:
        '''
        self.poz_lista = []
        self.lista_indeksow = None

    def __repr__(self):
        '''
        TypowaLista:
        '''
        return self.wzorzec_repr('TypowaLista')

    def __eq__(self, other):
        '''
        TypowaLista:
        '''
        wynik = self.poz_lista == other.poz_lista
        if us_kw.TymczasowoWizualizacjaZestawuFaktur:
            if 1:
                tmp_format = 'self.poz_lista'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
            if 1:
                tmp_format = 'other.poz_lista'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
            if 1:
                tmp_format = 'wynik'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        return wynik

    def dla_iteracji(self):
        '''
        TypowaLista:
        '''
        if self.lista_indeksow is None:
            wynik = self.poz_lista
        else:
            wynik = []
            for i in range(len(self.poz_lista)):
                if i in self.lista_indeksow:
                    wynik.append(self.poz_lista[i])
        return wynik

    def dla_enumeracji(self):
        '''
        TypowaLista:
        '''
        licznik = 0
        wynik = []
        for element in self.dla_iteracji():
            para = (licznik, element)
            wynik.append(para)
            licznik += 1
        return wynik

    def dolacz_koncowy(self, element):
        '''
        TypowaLista:
        '''
        if us_kw.LokalnaDiagnostykaKlas:
            print('Do %s:\n%s\ndołączamy element\n%s' % (self.moja_etykieta_instancji, repr(self.poz_lista), repr(element)))
        assert self.lista_indeksow is None, 'Zakładamy, że jeszcze nie ustawiano listy indeksów, bo nie wiemy, co z tym zrobić.'
        self.poz_lista.append(element)

    def podaj_dlugosc(self):
        '''
        TypowaLista:
        '''
        if self.lista_indeksow is None:
            wynik = len(self.poz_lista)
        else:
            wynik = 0
            for i in range(len(self.poz_lista)):
                if i in self.lista_indeksow:
                    wynik += 1
        return wynik

    def mam_elementy(self):
        '''
        TypowaLista:
        '''
        return self.podaj_dlugosc()

    def wskazany_element(self, indeks):
        '''
        TypowaLista:
        '''
        if self.lista_indeksow is not None:
            indeks = self.lista_indeksow[indeks]
        wynik = self.poz_lista[indeks]
        return wynik

    def ustaw_ograniczona_wersje(self, lista_indeksow):
        '''
        TypowaLista:
        '''
        self.lista_indeksow = lista_indeksow

    def pomin_pierwszy_indeks(self):
        '''
        TypowaLista:
        '''
        if self.lista_indeksow is None:
            self.lista_indeksow = list(range(len(self.poz_lista)))
        if len(self.lista_indeksow) > 0:
            del self.lista_indeksow[0]
            if not self.lista_indeksow:
                self.poczatkowe_ustawienia()
        else:
            raise RuntimeError('Nie powinno braknąć elementów na liście.')

    def lst_roznica(self, lst_poprz, wrnt_typowy):
        '''
        TypowaLista:
        '''
        # Nie wiem jeszcze, jak obsłużyć listy o długości innej niż 1
        assert lst_poprz.podaj_dlugosc() == self.podaj_dlugosc() == 1
        poprz_slownik = lst_poprz.wskazany_element(0)
        akt_slownik = self.wskazany_element(0)
        akt_slownik.wrnt_wsp(poprz_slownik, wrnt_typowy)


def znajdz_lub_przygotuj_nowa_liste(klucz, slownik):
    return po_kw.znajdz_lub_przygotuj_nowy_element(
        klucz,
        slownik,
        lambda: TypowaLista(hj_kw.space_two(ek_kw.ETK_lista_znajdz_lub_przygotuj, klucz)),
        )


class TestTypicalList(unittest.TestCase):
    def test_typical_list(self):
        '''
        TestTypicalList:
        '''
        obj = TypowaLista('e')
        self.assertRaises(IndexError, obj.wskazany_element, 0)
        obj.dolacz_koncowy(7)
        self.assertEqual(obj.wskazany_element(0), 7)
        obj.dolacz_koncowy(8)
        self.assertEqual(obj.wskazany_element(1), 8)
        obj.ustaw_ograniczona_wersje([1])
        self.assertEqual(obj.wskazany_element(0), 8)
