#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lb_kw
import oa_kw
import wb_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class SimpleDWN(object):
    def __init__(self, lp_miejsca):
        '''
        SimpleDWN:
        '''
        self.lp_miejsca = lp_miejsca
        # Lista wersji danego obrazka - z zaznaczoną jedną (lub więcej) fakturą
        self.odmiany_grafiki = []
        # Lista odcinków bazowych - lista elementów do wykreślenia w postaci
        # słupków: [pocz, kon, kwota, {lp miejsca: [lista lp faktur]}]
        self.odcinki_bazowe = lb_kw.ListaOdcBazowych()

    def mam_wykres_zbiorczy(self):
        '''
        SimpleDWN:
        '''
        return not self.lp_miejsca

    def kolor_tla(self):
        '''
        SimpleDWN:
        Wykres zbiorczy ma mieć inne tło
        '''
        if self.mam_wykres_zbiorczy():
            moje_tlo = oa_kw.KOLOR_TLO_SELEDYN
        else:
            moje_tlo = oa_kw.KOLOR_EXCEL_TLO_SZARE
        return moje_tlo

    def ustaw_zbitke(self, punkt_pocz, punkt_kon):
        '''
        SimpleDWN:
        '''
        self.zbitki_qm = wb_kw.KlasaZbitki(punkt_pocz, punkt_kon)

class TestProstychDanych(unittest.TestCase):
    def test_prostych_danych(self):
        '''
        TestProstychDanych:
        '''
        obk = SimpleDWN(0)
        self.assertTrue(obk.mam_wykres_zbiorczy())
        self.assertEqual(obk.kolor_tla(), oa_kw.KOLOR_TLO_SELEDYN)
        self.assertFalse(obk.odmiany_grafiki)
        self.assertTrue(obk.odcinki_bazowe)
        self.assertEqual(obk.odcinki_bazowe.len_odcinkow_bazowych(), 0)
        obk.ustaw_zbitke(15309, 15765)

    def test_prostych_2_danych(self):
        '''
        TestProstychDanych:
        '''
        obk = SimpleDWN(1)
        self.assertFalse(obk.mam_wykres_zbiorczy())
        self.assertEqual(obk.kolor_tla(), oa_kw.KOLOR_EXCEL_TLO_SZARE)
