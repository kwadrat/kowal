#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import dn_kw
import dz_kw

rh_ozncz_zst_a = 'ZST'
rh_ozncz_plw_a = 'PLW'
rh_ozncz_jdo_a = 'JDO'
rh_ozncz_cki_a = 'CKI'
rh_kol_data_dla_plyw_judo = ['AG', 'AH', 'AG']
rh_etk_daty_plyw_judo = u'Data Noty Księgowej         dla           Kryta Pływalnia i Pawilon Judo'

legalne_wzory_sumy_brutto = frozenset([
    u'Wartość brutto          [zł]',
    u'Koszt brutto z faktury Vattenfall S/D [zł]',
    u'Wartość brutto z faktury S/D [zł]',
    ])


def sprawdz_ogolnie_zgodnosc(elem, zbior, dodatkowy=None):
    if elem not in zbior:
        if 1:
            tmp_format = 'elem'
            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        if 1:
            tmp_format = 'repr(elem)'
            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        if 1:
            tmp_format = 'zbior'
            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        if dodatkowy is not None:
            if 1:
                tmp_format = 'dodatkowy'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        raise RuntimeError('Nieznany')


def doszlifuj_date(rh_dt):
    if dn_kw.mozliwy_py_time(rh_dt):
        krotka = (rh_dt.year, rh_dt.month, rh_dt.day)
        rh_dt = dn_kw.NapisDaty( * krotka)
    elif dz_kw.rozpoznaj_dzisiejszy_dzien(rh_dt) == 10:
        pass  # Data już w dobrym formacie
    else:
        if rh_dt == u'16-06-200':
            rh_dt = rh_dt + '5'
        elif rh_dt == u'31-11-2006':
            rh_dt = u'30-11-2006'
        krotka = dz_kw.wyciagnij_date_z_formatu_dmr(rh_dt)
        rh_dt = dn_kw.NapisDaty( * krotka)
    return rh_dt


class TestObiektuZespolu(unittest.TestCase):
    def test_szlifowania_daty(self):
        '''
        TestObiektuZespolu:
        '''
        self.assertEqual(doszlifuj_date(u'16-06-200'), '2005-06-16')
        self.assertEqual(doszlifuj_date(u'31-11-2006'), '2006-11-30')
