#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dv_kw
import rq_kw
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

MozliweLataZuzyc = map(str, dn_kw.ListaLatZuzyc)
MozliweLataDlaARok = [rq_kw.PoleWszystko] + MozliweLataZuzyc
MozliweLataDlaBRok = MozliweLataZuzyc
MozliweLataDlaWybranyRok = MozliweLataZuzyc + [rq_kw.PoleWszystko]

def DataBledna(napis):
    '''
    Wartość zwracana:
    pusty napis - data nie była błędna (czyli była poprawna)
    napis o niezerowej długości - wystąpił jakiś błąd
    '''
    bledna = '' # Załóż, że data nie jest poprawna
    kawalki = napis.split('-')
    ile_kawalkow = len(kawalki)
    if ile_kawalkow == 3:
        rok, miesiac, dzien = kawalki
        if rok in dn_kw.MozliweLataFaktur:
            if miesiac in dn_kw.LegalneMiesiace:
                rok = int(rok)
                miesiac = int(miesiac)
                liczba_legalnych_dni = dn_kw.DniWMiesiacu[miesiac - 1]
                # W lutym dodamy jeden dzień, jeśli rok jest przestępny
                if miesiac == 2:
                    liczba_legalnych_dni += chi_kw.rok_przestepny(rok)
                if dzien in dn_kw.LegalneDni[:liczba_legalnych_dni]:
                    pass # Mamy datę bez zastrzeżeń
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
        self.assertEqual(DataBledna('1'),
            'Liczba kawałków oddzielanych myślnikiem: 1')
        self.assertEqual(DataBledna('1800-01-01'),
            'Rok poza obsługiwanym zakresem: "1800"')
        self.assertEqual(DataBledna('2014-13-01'),
            'Miesiąc poza obsługiwanym zakresem: "13"')
        self.assertEqual(DataBledna('2014-03-32'),
            'Dzień poza obsługiwanym zakresem: "32"')
