#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Rodzaje wolframów
'''

import unittest

(
    cx_numer_faktury,
    cx_data_faktury,
    cx_poczatek_okresu,
    cx_koniec_okresu,
    cx_licznikowy_numer,
    cx_nazwa_taryfy,
    cx_stawka_podatku_vat,
    cx_kwota_podatku_vat,
    cx_nic_float,
    cx_req_liczba,
    cx_req_int,
    cx_nic_int,
    cx_req_data,
    cx_nic_data,
    cx_ogolne_tekstowe,
    ) = range(15)

(
    cx_ext_trojcyfrowe,
    cx_ext_czterocyfrowe,
    cx_ext_pieciocyfrowe,
    ) = range(3)

class KlasaStalowejWiedzy(object):
    def __init__(self):
        '''
        KlasaStalowejWiedzy:
        '''
        self.zbior_z_kalendarzem = frozenset(
            [cx_data_faktury, cx_poczatek_okresu, cx_koniec_okresu,
            cx_req_data, cx_nic_data])

    def cx_chce_kalendarz(self, stalowe_cx):
        '''
        KlasaStalowejWiedzy:
        '''
        return stalowe_cx in self.zbior_z_kalendarzem

    def cx_jaki_typ(self, stalowe_cx, ekstra_cx=None):
        '''
        KlasaStalowejWiedzy:
        '''
        if stalowe_cx in (cx_numer_faktury, cx_nazwa_taryfy, cx_licznikowy_numer, cx_ogolne_tekstowe):
            return 'text'
        elif self.cx_chce_kalendarz(stalowe_cx):
            return 'date'
        elif stalowe_cx in (cx_stawka_podatku_vat, cx_kwota_podatku_vat, cx_nic_float, cx_req_liczba):
            if ekstra_cx == cx_ext_trojcyfrowe:
                return 'numeric(1000,3)'
            elif ekstra_cx == cx_ext_czterocyfrowe:
                return 'numeric(1000,4)'
            elif ekstra_cx == cx_ext_pieciocyfrowe:
                return 'numeric(1000,5)'
            else:
                return 'numeric(1000,2)'
        elif stalowe_cx in (cx_req_int, cx_nic_int):
            return 'integer'
        else:
            raise RuntimeError('Nieznane stalowe_cx: %s' % repr(stalowe_cx))

cx_obkt = KlasaStalowejWiedzy()

class TestStalowych(unittest.TestCase):
    def test_stalowych_rodzajow(self):
        '''
        TestStalowych:
        '''
        obk = KlasaStalowejWiedzy()
        self.assertEqual(obk.cx_chce_kalendarz(cx_req_liczba), 0)
        self.assertEqual(obk.cx_chce_kalendarz(cx_data_faktury), 1)
        self.assertEqual(obk.cx_jaki_typ(cx_numer_faktury), 'text')
        self.assertRaises(RuntimeError, obk.cx_jaki_typ, None)
        self.assertEqual(obk.cx_jaki_typ(cx_data_faktury), 'date')
        self.assertEqual(obk.cx_jaki_typ(cx_poczatek_okresu), 'date')
        self.assertEqual(obk.cx_jaki_typ(cx_nazwa_taryfy), 'text')
        self.assertEqual(obk.cx_jaki_typ(cx_stawka_podatku_vat), 'numeric(1000,2)')
        self.assertEqual(obk.cx_jaki_typ(cx_kwota_podatku_vat), 'numeric(1000,2)')
        self.assertEqual(obk.cx_jaki_typ(cx_nic_float), 'numeric(1000,2)')
        self.assertEqual(obk.cx_jaki_typ(cx_req_liczba), 'numeric(1000,2)')
        self.assertEqual(obk.cx_jaki_typ(cx_req_int), 'integer')
        self.assertEqual(obk.cx_jaki_typ(cx_nic_int), 'integer')
        self.assertEqual(obk.cx_jaki_typ(cx_req_data), 'date')
        self.assertEqual(obk.cx_jaki_typ(cx_nic_data), 'date')
        self.assertEqual(obk.cx_jaki_typ(cx_licznikowy_numer), 'text')
        self.assertEqual(cx_ext_trojcyfrowe, 0)
        self.assertEqual(cx_ext_czterocyfrowe, 1)
        self.assertEqual(cx_ext_pieciocyfrowe, 2)
        self.assertEqual(obk.cx_jaki_typ(cx_req_liczba, cx_ext_trojcyfrowe), 'numeric(1000,3)')
        self.assertEqual(obk.cx_jaki_typ(cx_req_liczba, cx_ext_pieciocyfrowe), 'numeric(1000,5)')
        self.assertEqual(obk.cx_jaki_typ(cx_req_liczba, cx_ext_czterocyfrowe), 'numeric(1000,4)')
        self.assertEqual(obk.cx_jaki_typ(cx_ogolne_tekstowe), 'text')
