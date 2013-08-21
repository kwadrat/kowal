#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesiąca
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import lm_kw
import ze_kw
import dn_kw
import le_kw
import lw_kw
import lh_kw
import jb_kw
import ge_kw
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

class PomiaryPoborowSasiadujacychDni(OgolnaListaPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiaryPoborowSasiadujacychDni:
        '''
        tvk_data = tgk.wez_date()
        my_pob_czas = tgk.wez_pob_czas()
        if my_pob_czas == lw_kw.DPC_Tydzien:
            my_start_day = dn_kw.napis_na_numer_dnia(tvk_data)
            my_start_day = dn_kw.get_monday(my_start_day)
            my_end_day = my_start_day + 7
        elif my_pob_czas == lw_kw.DPC_Miesiac:
            my_year, my_month = dn_kw.rok_mies_z_napisu(tvk_data)
            my_start_day, my_end_day = dn_kw.ZakresMiesiaca(my_year, my_month)
        else:
            raise RuntimeError('Nieznany my_pob_czas?: %s' % repr(my_pob_czas))
        aqr = ge_kw.SzkieletDziennyDlaPoborow(krt_pobor, my_start_day, my_end_day)
        OgolnaListaPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def html_poboru_dla_dnia(self, jeden_pobor):
        '''
        PomiaryPoborowSasiadujacychDni:
        '''
        my_cur_date = str(jeden_pobor[lc_kw.fq_m_date_qv])
        my_cur_day = dn_kw.napis_na_numer_dnia(my_cur_date)
        akt = my_cur_day - self.aqr.my_start_day
        kwota = lm_kw.dec2flt(jeden_pobor[lc_kw.fq_m_sum_qv])
        self.rdzen_kwoty(akt, kwota)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiaryPoborowSasiadujacychDni:
        '''
        lst_h = lh_kw.ListaHTML()
        my_start_date = dn_kw.NapisDnia(self.aqr.my_start_day)
        my_end_date = dn_kw.NapisDnia(self.aqr.my_end_day)
        szereg_poborow = le_kw.dq_liczniki_poboru_w_miesiacu(self.dfb, self.table_name, self.id_obiekt, my_start_date, my_end_date)
        for jeden_pobor in szereg_poborow:
            self.html_poboru_dla_dnia(jeden_pobor)
        self.rdzen_rysowania(lst_h, krt_pobor, lw_kw.PDS_Dni)
        return lst_h.polacz_html()
