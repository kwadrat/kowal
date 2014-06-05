#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
import dn_kw
import sk_ht_kw
import ei_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def ListaWyboruRoku(tgk):
    return sk_ht_kw.ListWyboruOgolna(tgk, ei_kw.NazwaRok, dn_kw.MozliweLataZuzyc)

Skrawek = sk_ht_kw.Skrawek

class SkrRok(Skrawek):
    '''Wybór roku, który przetwarzamy. Tego pola może nie być, jeśli analizujemy
    cały zakres, na przestrzeni wszystkich lat.
    '''

    def __init__(self):
        '''
        SkrRok:
        '''
        Skrawek.__init__(self)
        self.moje_pole = ei_kw.NazwaRok

    def analiza_parametrow(self, tgk, dfb):
        '''
        SkrRok:
        '''
        self.wartosc = tgk.qparam.get(self.moje_pole, None)
        if self.skh_widzialny(self.prm_okres.wartosc):
            if self.wartosc == None:
                # Domyślnie pokazujemy aktualny rok
                self.wartosc = dn_kw.RokTeraz()
        else:
            return True # Rok nie jest potrzebny, zwracamy cokolwiek różnego od None
        return self.wartosc != None

    def skh_widzialny(self, skp_okres):
        '''
        SkrRok:
        Informuje, czy potrzebujemy pole z wyborem roku - potrzebujemy,
        jeśli w polu okresu nic nie wybrano lub wybrano skalę miesięcy w roku
        Wartość zwracana:
        True - potrzebne jest pole z wyborem roku
        False - nie chcemy pola z wyborem roku
        '''
        if skp_okres in rq_kw.PR_PotrzebujeRoku:
            return True
        elif skp_okres in rq_kw.PR_NiePotrzebujeRoku:
            return False
        else:
            raise RuntimeError('Nieznana wartosc: %s' % repr(skp_okres))

    def zbierz_html(self, tgk, dfb):
        '''
        SkrRok:
        '''
        # Zwracamy pole wyboru roku tylko wtedy, gdy jest to wymagane w polu
        # wyboru okresu
        if self.skh_widzialny(self.prm_okres.wartosc):
            return ListaWyboruRoku(tgk)
        else:
            return self.wartosc_ukryta()

class TestRok(unittest.TestCase):
    def test_1_a(self):
        '''
        SkrRok:
        '''
        moj_elem = SkrRok()
        moj_elem.skh_okres(None)
        self.assertTrue(moj_elem.skh_widzialny(rq_kw.Dt_Miesiac))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Rok))
        self.assertTrue(moj_elem.skh_widzialny(rq_kw.PR_Brak))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dn_RapPierwszy))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dn_RapDrugi))
