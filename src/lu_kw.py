#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesięcy w ciągu roku
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import lm_kw
import ze_kw
import dn_kw
import le_kw
import lw_kw
import lq_kw
import lh_kw
import jb_kw
import ox_kw
import wn_kw
import gc_kw
import lt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

OgolnaListaPoborow = lt_kw.OgolnaListaPoborow

class PomiaryPoborowMiesiecznie(OgolnaListaPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        aqr = ox_kw.SzkieletMiesiecznyDlaPoborow(krt_pobor)
        OgolnaListaPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def html_przedzialy(self, fvk_rok):
        '''
        PomiaryPoborowMiesiecznie:
        '''
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
        list_of_values = zbiornik_przedzialow[single_key]
        kwota = lq_kw.sum_of_not_nones(krt_pobor.krt_vl_fnctn, list_of_values)
        kwota = lm_kw.dec2flt(kwota)
        self.rdzen_kwoty(akt, kwota)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        lst_h = lh_kw.ListaHTML()
        tvk_data = self.tgk.wez_date()
        fvk_rok, fvk_miesiac = dn_kw.rok_mies_z_napisu(tvk_data)
        zbiornik_przedzialow = self.html_przedzialy(fvk_rok)
        all_keys = zbiornik_przedzialow.keys()
        all_keys.sort()
        for single_key in all_keys:
            self.html_poboru_dla_miesiaca(krt_pobor, zbiornik_przedzialow, single_key)
        self.rdzen_rysowania(lst_h, krt_pobor, lw_kw.PDS_Miesiace)
        return lst_h.polacz_html()
