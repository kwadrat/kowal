#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
import dd_kw
import dq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

KlasaOgolnaSzkieletuDat = dq_kw.KlasaOgolnaSzkieletuDat

class SzkieletDatDlaPoborow(KlasaOgolnaSzkieletuDat):
    def __init__(self, krt_pobor):
        '''
        SzkieletDatDlaPoborow:
        '''
        KlasaOgolnaSzkieletuDat.__init__(self)
        wymiar_czasowy = krt_pobor.krt_wymiar
        self.przypisz_szkielet(dq_kw.generator_szkieletu(wymiar_czasowy))
        self.wymiar_czasowy = wymiar_czasowy

    def to_pelna_godzina(self, akt):
        '''
        SzkieletDatDlaPoborow:
        '''
        return self.wymiar_czasowy == 24 or akt % 8 == 0

    def tekst_pelnej_godziny(self, akt):
        '''
        SzkieletDatDlaPoborow:
        '''
        if self.wymiar_czasowy == 24:
            result = akt
        else:
            result = akt / 4
        return str(result / 2)

class TestSzkieletowegoDatownika(unittest.TestCase):
    def test_energii_szkieletowego_datownika(self):
        '''
        TestSzkieletowegoDatownika:
        '''
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dn_Energy)
        obk = SzkieletDatDlaPoborow(krt_pobor)
        self.assertEqual(obk.szkielet_dat, dq_kw.generator_szkieletu(24))

    def test_mocy_szkieletowego_datownika(self):
        '''
        TestSzkieletowegoDatownika:
        '''
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dn_Power)
        obk = SzkieletDatDlaPoborow(krt_pobor)
        self.assertEqual(obk.szkielet_dat, dq_kw.generator_szkieletu(96))
