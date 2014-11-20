#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import rq_kw
import sk_kw
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

Skrawek = sk_kw.Skrawek

class SkrPrezentacja(Skrawek):
    '''Wybór sposobu prezentacji wyników: tabela, tabela/wykres, wykres
    To pole jest wyświetlane tylko dla R1 i R2, dla lat i roku
    jest to pole niewidoczne i jego wartość nie jest istotna
    '''

    def __init__(self):
        '''
        SkrPrezentacja:
        '''
        Skrawek.__init__(self)
        self.moje_pole = ei_kw.NazwaPrezentacja

    def skh_widzialny(self, skp_okres):
        '''
        SkrPrezentacja:
        Informujemy, czy potrzebujemy pola z wyborem prezentacji (tabela/wykres).
        Potrzebne to jest dla R1 i R2, dla pozostałych - na
        razie prezentacja nie będzie używana.
        Wartość zwracana:
        True - potrzebne jest pole z wyborem prezentacji
        False - nie chcemy pola z wyborem prezentacji
        '''
        if skp_okres in rq_kw.PR_PotrzebujePrezent:
            return True
        elif skp_okres in rq_kw.PR_NiePotrzebujePrezent:
            return False
        else:
            raise RuntimeError('Nieznana wartosc: %s' % repr(skp_okres))

    def analiza_parametrow(self, tgk, dfb):
        '''
        SkrPrezentacja:
        '''
        self.wartosc = tgk.qparam.get(self.moje_pole, None)
        if self.wartosc == None:
            # Domyślnie pokazujmy same tabelki
            self.wartosc = rq_kw.DP_Tabela
        if self.skh_widzialny(self.prm_okres.wartosc):
            return self.wartosc != None
        else:
            return True

    def zbierz_html(self, tgk, dfb):
        '''
        SkrPrezentacja:
        '''
        if self.skh_widzialny(self.prm_okres.wartosc):
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DanePrezentacji)
        else:
            return self.wartosc_ukryta()

class TestPrezentacja(unittest.TestCase):
    def test_1_a(self):
        '''
        TestPrezentacja:
        '''
        moj_elem = SkrPrezentacja()
        moj_elem.skh_okres(None)
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.PR_Brak))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Miesiac))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Rok))
        self.assertTrue(moj_elem.skh_widzialny(rq_kw.Dt_RapPierwszy))
        self.assertTrue(moj_elem.skh_widzialny(rq_kw.Dt_RapDrugi))
