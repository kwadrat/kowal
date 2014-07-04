#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ust_iw_kw
import li_kw
import llso_iw_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

licznik_inst_list = li_kw.LicznikInstancji('lista')

ListaLubSlownikOgolnie = llso_iw_kw.ListaLubSlownikOgolnie

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
        if ust_iw_kw.TymczasowoWizualizacjaZestawuFaktur:
            tmp_format = 'self.poz_lista'; print tmp_format, eval(tmp_format)
            tmp_format = 'other.poz_lista'; print tmp_format, eval(tmp_format)
            tmp_format = 'wynik'; print tmp_format, eval(tmp_format)
        return wynik

    def dla_iteracji(self):
        '''
        TypowaLista:
        '''
        if self.lista_indeksow is None:
            wynik = self.poz_lista
        else:
            wynik = []
            for i in xrange(len(self.poz_lista)):
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
        if ust_iw_kw.LokalnaDiagnostykaKlas:
            print 'Do %s:\n%s\ndołączamy element\n%s' % (self.moja_etykieta_instancji, repr(self.poz_lista), repr(element))
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
            for i in xrange(len(self.poz_lista)):
                if i in self.lista_indeksow:
                    wynik += 1
        return wynik

    def mam_elementy(self):
        '''
        TypowaLista:
        '''
        return self.podaj_dlugosc();

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
            self.lista_indeksow = range(len(self.poz_lista))
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
