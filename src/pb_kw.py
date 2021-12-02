#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import dv_kw
import gb_kw
import ze_kw


class NaglowekKolumny(object):
    '''Nagłówek kolumny, opcjonalnie z jednostką, być może
    ze złamanym wierszem dla jednostki
    '''
    def __init__(self, nazwa, jednostka=None, separator=' '):
        '''
        NaglowekKolumny:
        '''
        self.nazwa = nazwa
        self.jednostka = jednostka
        self.separator = separator

    def nx_pelny(self):
        '''
        NaglowekKolumny:
        '''
        lista = []
        lista.append(self.nazwa)
        if self.jednostka is not None:
            lista.append(self.separator)
            lista.append(gb_kw.nawiasy_kwadratowe(self.jednostka))
        return ''.join(lista)


ux_1_a = NaglowekKolumny('Moc wykonana', jednostka=gb_kw.JednMet3h).nx_pelny()
ux_2_a = NaglowekKolumny('Moc umowna', jednostka=gb_kw.JednMet3h).nx_pelny()
ux_3_a = NaglowekKolumny('Zużycie', jednostka=gb_kw.JednM3, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_4_a = NaglowekKolumny('Moc wykonana', jednostka=gb_kw.JednMet3h, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_5_a = NaglowekKolumny('Moc umowna', jednostka=gb_kw.JednMet3h, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_6_a = NaglowekKolumny('Moc - umowna', jednostka=gb_kw.Jedn_kWtow, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_7_a = NaglowekKolumny('Moc - pobrana', jednostka=gb_kw.Jedn_kWtow, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_8_a = NaglowekKolumny('Razem Brutto', jednostka=gb_kw.Jedn_zlotowki, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_9_a = NaglowekKolumny('Zużycie', jednostka=gb_kw.Jedn_kW_MWh, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_10_a = NaglowekKolumny('Zużycie', jednostka=gb_kw.Jedn_kWh, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_11_a = NaglowekKolumny('Zużycie', jednostka=gb_kw.Jedn_MWh, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_12_a = NaglowekKolumny('Zużycie', jednostka=gb_kw.JednGJ, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_13_a = NaglowekKolumny('Moc - umowna', jednostka=gb_kw.JednMW, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_14_a = NaglowekKolumny('Moc wykonana', jednostka=gb_kw.Jedn_a_kWh_h).nx_pelny()
ux_15_a = NaglowekKolumny('Moc zamówiona', jednostka=gb_kw.Jedn_a_kWh_h).nx_pelny()
ux_16_a = NaglowekKolumny('Moc wykonana', jednostka=gb_kw.Jedn_a_kWh_h, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()
ux_17_a = NaglowekKolumny('Moc zamówiona', jednostka=gb_kw.Jedn_a_kWh_h, separator=ze_kw.formularz_1c_zlm_wrsz).nx_pelny()


class TestNagKol(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual

    def test_naglowka_kolumny(self):
        '''
        TestNagKol:
        '''
        obk = NaglowekKolumny('abc')
        odp = obk.nx_pelny()
        self.assertEqual(odp, 'abc')
        self.assertEqual(ux_1_a, 'Moc wykonana [m<sup>3</sup>/h]')
        self.assertEqual(ux_2_a, 'Moc umowna [m<sup>3</sup>/h]')
        self.assertEqual(ux_3_a, 'Zużycie<br />\n[m<sup>3</sup>]')
        self.assertEqual(ux_4_a, 'Moc wykonana<br />\n[m<sup>3</sup>/h]')
        self.assertEqual(ux_5_a, 'Moc umowna<br />\n[m<sup>3</sup>/h]')
        self.assertEqual(ux_10_a, 'Zużycie<br />\n[kWh]')
        self.assertEqual(ux_14_a, 'Moc wykonana [kWh/h]')
        self.assertEqual(ux_15_a, 'Moc zamówiona [kWh/h]')
        self.assertEqual(ux_16_a, 'Moc wykonana<br />\n[kWh/h]')
        self.assertEqual(ux_17_a, 'Moc zamówiona<br />\n[kWh/h]')
