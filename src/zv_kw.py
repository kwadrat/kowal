#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


class ParametrySrodowiska(object):
    def __init__(self):
        '''
        ParametrySrodowiska:
        '''
        self.ustaw_etap(0)
        self.rh_dwuwierszowosc = 0
        self.rh_nr_wiersza = 0

    def ustaw_etap(self, wartosc):
        '''
        ParametrySrodowiska:
        '''
        self.rh_nr_okresu = wartosc

    def historyczny(self):
        '''
        ParametrySrodowiska:
        '''
        return self.rh_nr_okresu

    def ustaw_dwuwierszowosc(self, wartosc):
        '''
        ParametrySrodowiska:
        '''
        self.rh_dwuwierszowosc = wartosc

    def jestem_dwuwierszowy(self):
        '''
        ParametrySrodowiska:
        '''
        return self.rh_dwuwierszowosc

    def ustaw_nr_wiersza(self, wartosc):
        '''
        ParametrySrodowiska:
        '''
        self.rh_nr_wiersza = wartosc

    def pobierz_nr_akt_wiersza(self):
        '''
        ParametrySrodowiska:
        '''
        return self.rh_nr_wiersza

    def nr_wiersza_poprz_miesiaca(self):
        '''
        ParametrySrodowiska:
        '''
        okres_hist = self.historyczny()
        if okres_hist == 0:
            wynik = self.rh_nr_wiersza - 1
        elif okres_hist == 1:
            if self.rh_nr_wiersza >= 63:
                wynik = self.rh_nr_wiersza - 2
            else:
                wynik = self.rh_nr_wiersza - 1
        elif okres_hist == 2:
            wynik = self.rh_nr_wiersza - 2
        else:
            raise RuntimeError('Nieznany okres w historii?: %s' % repr(okres_hist))
        return wynik

class TestParametrowSrodowiska(unittest.TestCase):
    def test_parametrow_srodowiska(self):
        '''
        TestParametrowSrodowiska:
        '''
        qb_dane = ParametrySrodowiska()
        qb_dane.ustaw_etap(1)
        self.assertEqual(qb_dane.historyczny(), 1)
        qb_dane.ustaw_etap(0)
        self.assertEqual(qb_dane.historyczny(), 0)
        qb_dane.ustaw_dwuwierszowosc(1)
        self.assertTrue(qb_dane.jestem_dwuwierszowy())
        qb_dane.ustaw_dwuwierszowosc(0)
        self.assertFalse(qb_dane.jestem_dwuwierszowy())
        qb_dane.ustaw_nr_wiersza(20)
        self.assertEqual(qb_dane.pobierz_nr_akt_wiersza(), 20)
