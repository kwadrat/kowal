#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
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

def generator_szkieletu(liczba_przedzialow):
    return range(0, 2 * liczba_przedzialow + 1, 2)

KlasaOgolnaSzkieletuDat = dq_kw.KlasaOgolnaSzkieletuDat

class SzkieletDatDlaPoborow(KlasaOgolnaSzkieletuDat):
    def __init__(self, tvk_pobor):
        '''
        SzkieletDatDlaPoborow:
        '''
        KlasaOgolnaSzkieletuDat.__init__(self)
        wymiar_czasowy = {
            lw_kw.Dn_Energy: 24,
            lw_kw.Dn_Power: 96,
            }[tvk_pobor]
        self.tvk_pobor = tvk_pobor
        self.przypisz_szkielet(generator_szkieletu(wymiar_czasowy))
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
        self.assertEqual(generator_szkieletu(1), [0, 2])
        self.assertEqual(generator_szkieletu(3), [0, 2, 4, 6])
        obk = SzkieletDatDlaPoborow(lw_kw.Dn_Energy)
        self.assertEqual(obk.szkielet_dat, generator_szkieletu(24))

    def test_mocy_szkieletowego_datownika(self):
        '''
        TestSzkieletowegoDatownika:
        '''
        obk = SzkieletDatDlaPoborow(lw_kw.Dn_Power)
        self.assertEqual(obk.szkielet_dat, generator_szkieletu(96))
