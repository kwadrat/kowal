#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ez_kw

KlasaSzkieletuDat = ez_kw.KlasaSzkieletuDat

class SzkieletDatDlaZuzycia(KlasaSzkieletuDat):
    def __init__(self):
        '''
        SzkieletDatDlaZuzycia:
        '''
        KlasaSzkieletuDat.__init__(self)

    def poczatki_miesiecy(self):
        '''
        SzkieletDatDlaZuzycia:
        '''
        return self.szkielet_dat

class TestSzkieletuDatDlaZuzycia(unittest.TestCase):
    def test_szkieletu_dat_dla_zuzycia(self):
        '''
        TestSzkieletuDatDlaZuzycia:
        '''
        obk = SzkieletDatDlaZuzycia()
        obk.przypisz_dla_roku_szkielet
