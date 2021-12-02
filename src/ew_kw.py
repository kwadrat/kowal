#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import rq_kw
import ez_kw

KlasaSzkieletuDat = ez_kw.KlasaSzkieletuDat


class SzkieletDatDlaFakturMiesLat(KlasaSzkieletuDat):
    def __init__(self):
        '''
        SzkieletDatDlaFakturMiesLat:
        '''
        KlasaSzkieletuDat.__init__(self)

    def mam_dat_na_dluzszy_rok(self):
        '''
        SzkieletDatDlaFakturMiesLat:
        Górne, dłuższe kreski dla poszczególnych faktur (tylko ciągłych)
        Liczba miesięcy dla ciągłych faktur miesięcznych
        '''
        return self.liczba_paskow() == rq_kw.RokDluzszy


class TestSzkieletuDatDlaFakturMiesLat(unittest.TestCase):
    def test_szkieletu_dat_dla_faktur_mies_lat(self):
        '''
        TestSzkieletuDatDlaFakturMiesLat:
        '''
        obk = SzkieletDatDlaFakturMiesLat()
        obk.przypisz_dla_roku_szkielet(2012, rok_z_rozszerzeniem=0)
        self.assertEqual(obk.szkielet_pocz, 15340)
        self.assertEqual(obk.szkielet_kon, 15706)
