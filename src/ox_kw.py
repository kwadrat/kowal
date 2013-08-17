#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
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
        return dn_kw.nazwa_rzymskiego(1 + akt / 2)

class TestMiesiecznegoSzkieletu(unittest.TestCase):
    def test_energii_szkieletowego_miesiecznie_datownika(self):
        '''
        TestMiesiecznegoSzkieletu:
        '''
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dn_Energy)
        obk = SzkieletMiesiecznyDlaPoborow(krt_pobor)
        self.assertEqual(obk.tekst_pelnej_godziny(10), 'VI')
