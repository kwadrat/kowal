#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesięcy w ciągu roku
'''

import unittest

import lc_kw
import lm_kw
import dn_kw
import le_kw
import lw_kw
import dd_kw
import lq_kw
import lh_kw
import ox_kw
import lt_kw

def wyznacz_kwote(krt_pobor, zbiornik_przedzialow, single_key):
    list_of_values = zbiornik_przedzialow[single_key]
    kwota = lq_kw.sum_of_not_nones(krt_pobor.krt_vl_fnctn, list_of_values)
    kwota = lm_kw.dec2flt(kwota)
    return kwota

OgolnaListaPoborow = lt_kw.OgolnaListaPoborow

class PomiaryPoborowMiesiecznie(OgolnaListaPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        aqr = ox_kw.SzkieletMiesiecznyDlaPoborow(krt_pobor)
        OgolnaListaPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def html_rok_poboru(self):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        tvk_data = self.tgk.wez_date()
        fvk_rok, fvk_miesiac = dn_kw.rok_mies_z_napisu(tvk_data)
        return fvk_rok

    def html_przedzialy(self):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        fvk_rok = self.html_rok_poboru()
        zbiornik_przedzialow = {}
        result = le_kw.dq_liczniki_poboru_w_roku(self.dfb, self.table_name, self.id_obiekt, fvk_rok)
        for single_record in result:
            fvk_rok, fvk_miesiac = dn_kw.rok_mies_z_napisu(str(single_record[lc_kw.fq_m_date_qv]))
            if fvk_miesiac not in zbiornik_przedzialow:
                zbiornik_przedzialow[fvk_miesiac] = []
            zbiornik_przedzialow[fvk_miesiac].append(single_record[lc_kw.fq_m_sum_qv])
        return zbiornik_przedzialow

    def html_poboru_dla_miesiaca(self, krt_pobor, zbiornik_przedzialow, single_key):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        akt = single_key - 1
        kwota = wyznacz_kwote(krt_pobor, zbiornik_przedzialow, single_key)
        self.rdzen_kwoty(akt, kwota)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        lst_h = lh_kw.ListaHTML()
        zbiornik_przedzialow = self.html_przedzialy()
        all_keys = zbiornik_przedzialow.keys()
        all_keys.sort()
        for single_key in all_keys:
            self.html_poboru_dla_miesiaca(krt_pobor, zbiornik_przedzialow, single_key)
        self.rdzen_rysowania(lst_h, krt_pobor, lw_kw.PDS_Miesiace)
        return lst_h.polacz_html()

class TestCalculateAmount(unittest.TestCase):
    def test_calculate_amount(self):
        '''
        TestCalculateAmount:
        '''
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dm_Power)
        single_key = 'a'
        zbiornik_przedzialow = {single_key:[]}
        kwota = wyznacz_kwote(krt_pobor, zbiornik_przedzialow, single_key)
        self.assertEqual(kwota, 0)
