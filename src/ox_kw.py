#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import jt_kw
import lw_kw
import dd_kw
import dq_kw

KlasaOgolnaSzkieletuDat = dq_kw.KlasaOgolnaSzkieletuDat


class SzkieletMiesiecznyDlaPoborow(KlasaOgolnaSzkieletuDat):
    def __init__(self, krt_pobor):
        '''
        SzkieletMiesiecznyDlaPoborow:
        '''
        KlasaOgolnaSzkieletuDat.__init__(self)
        self.przypisz_szkielet(dq_kw.generator_szkieletu(12))

    def to_pelna_godzina(self, akt):
        '''
        SzkieletMiesiecznyDlaPoborow:
        '''
        return 1

    def tekst_pelnej_godziny(self, akt):
        '''
        SzkieletMiesiecznyDlaPoborow:
        '''
        return jt_kw.nazwa_rzymskiego(1 + akt / 2)


class TestMiesiecznegoSzkieletu(unittest.TestCase):
    def test_energii_szkieletowego_miesiecznie_datownika(self):
        '''
        TestMiesiecznegoSzkieletu:
        '''
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dm_Energy)
        obk = SzkieletMiesiecznyDlaPoborow(krt_pobor)
        self.assertEqual(obk.tekst_pelnej_godziny(10), 'VI')
