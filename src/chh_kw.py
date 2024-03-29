#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import dv_kw
import rq_kw
import chi_kw
import dn_kw

LegalneMiesiace = (
    '01', '02', '03', '04', '05', '06',
    '07', '08', '09', '10', '11', '12',
    )

DniWMiesiacu = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,)

LegalneDni = (
    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
    '25', '26', '27', '28', '29', '30', '31',
    )

RokObecnyStaly = dn_kw.RokDzisiaj()
ListaLatZuzyc = list(range(RokObecnyStaly, rq_kw.RokPocz2 - 1, -1))
MozliweLataZuzyc = list(map(str, ListaLatZuzyc))
MozliweLataFaktur = list(map(str, range(RokObecnyStaly + 1, rq_kw.RokPocz2 - 1, -1)))
MozliweLataDlaARok = [rq_kw.PoleWszystko] + MozliweLataZuzyc
MozliweLataDlaBRok = MozliweLataZuzyc


def tupled_year(year):
    return (year, str(year))


ParowaneLataDanych = list(map(tupled_year, ListaLatZuzyc))


def DataBledna(napis):
    '''
    Wartość zwracana:
    pusty napis - data nie była błędna (czyli była poprawna)
    napis o niezerowej długości - wystąpił jakiś błąd
    '''
    bledna = ''  # Załóż, że data nie jest poprawna
    kawalki = napis.split('-')
    ile_kawalkow = len(kawalki)
    if ile_kawalkow == 3:
        rok, miesiac, dzien = kawalki
        if rok in MozliweLataFaktur:
            if miesiac in LegalneMiesiace:
                rok = int(rok)
                miesiac = int(miesiac)
                liczba_legalnych_dni = DniWMiesiacu[miesiac - 1]
                # W lutym dodamy jeden dzień, jeśli rok jest przestępny
                if miesiac == 2:
                    liczba_legalnych_dni += chi_kw.rok_przestepny(rok)
                if dzien in LegalneDni[:liczba_legalnych_dni]:
                    pass  # Mamy datę bez zastrzeżeń
                else:
                    bledna = 'Dzień poza obsługiwanym zakresem: "%s"' % dzien
            else:
                bledna = 'Miesiąc poza obsługiwanym zakresem: "%s"' % miesiac
        else:
            bledna = 'Rok poza obsługiwanym zakresem: "%s"' % rok
    else:
        bledna = 'Liczba kawałków oddzielanych myślnikiem: %d' % ile_kawalkow
    return bledna


class TestMisspelledDate(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual

    def test_misspelled_date(self):
        '''
        TestMisspelledDate:
        '''
        self.assertEqual(
            DataBledna('1'),
            'Liczba kawałków oddzielanych myślnikiem: 1')
        self.assertEqual(
            DataBledna('1800-01-01'),
            'Rok poza obsługiwanym zakresem: "1800"')
        self.assertEqual(
            DataBledna('2014-13-01'),
            'Miesiąc poza obsługiwanym zakresem: "13"')
        self.assertEqual(
            DataBledna('2014-03-32'),
            'Dzień poza obsługiwanym zakresem: "32"')

    def test_converting_year(self):
        '''
        TestMisspelledDate:
        '''
        self.assertEqual(tupled_year(2014), (2014, '2014'))
        self.assertEqual(tupled_year(2013), (2013, '2013'))
