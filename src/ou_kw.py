#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import lm_kw
import ze_kw
import le_kw
import lw_kw
import lh_kw
import jb_kw
import ey_kw
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

class PomiaryPoborowJednegoDnia(OgolnaListaPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiaryPoborowJednegoDnia:
        '''
        aqr = ey_kw.SzkieletDatDlaPoborow(krt_pobor)
        OgolnaListaPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def zbuduj_odcinki_y_bazowe(self, lista_pomiarow):
        '''
        PomiaryPoborowJednegoDnia:
        '''
        for akt, kwota in enumerate(lista_pomiarow):
            nast = akt + 1
            kwota = lm_kw.dec2flt(kwota)
            if kwota is not None:
                slownik_qm = wn_kw.KlasaSlownika()
                slownik_qm.jh_ustaw_kwt_qm(kwota)
                self.dnw.odcinki_bazowe.app_end(jb_kw.JedenOdcinekBazowy(2 * akt, 2 * nast, slownik_qm))

    def html_ls_poborow(self, lst_h, krt_pobor, dfb, id_obiekt, table_name, single_record):
        '''
        PomiaryPoborowJednegoDnia:
        '''
        lista_pomiarow = single_record[lc_kw.fq_m_samples_qv]
        self.zbuduj_odcinki_y_bazowe(lista_pomiarow)
        dolny_podpis = lw_kw.PDS_Godziny
        self.rdzen_rysowania(lst_h, krt_pobor, dolny_podpis)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiaryPoborowJednegoDnia:
        '''
        lst_h = lh_kw.ListaHTML()
        tvk_data = self.tgk.wez_date()
        result = le_kw.dq_liczniki_poboru_w_dniu(self.dfb, self.table_name, self.id_obiekt, tvk_data)
        for single_record in result:
            self.html_ls_poborow(lst_h, krt_pobor, self.dfb, self.id_obiekt, self.table_name, single_record)
        return lst_h.polacz_html()
