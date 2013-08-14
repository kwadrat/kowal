#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesiąca
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import dn_kw
import le_kw
import lw_kw
import lh_kw
import ge_kw
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

OgolnySzeregListPoborow = lt_kw.OgolnySzeregListPoborow

class PomiarowaMiesiecznaListaPoborow(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiarowaMiesiecznaListaPoborow:
        '''
        tvk_data = tgk.wez_date()
        my_pob_czas = tgk.wez_pob_czas()
        if my_pob_czas == lw_kw.DPC_Tydzien:
            my_start_day = dn_kw.napis_na_numer_dnia(tvk_data)
            my_end_day = my_start_day + 7
        elif my_pob_czas == lw_kw.DPC_Miesiac:
            my_year, my_month = dn_kw.rok_mies_z_napisu(tvk_data)
            my_start_day, my_end_day = dn_kw.ZakresMiesiaca(my_year, my_month)
        else:
            raise RuntimeError('Nieznany my_pob_czas?: %s' % repr(my_pob_czas))
        aqr = ge_kw.SzkieletDziennyDlaPoborow(krt_pobor, my_start_day, my_end_day)
        OgolnySzeregListPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiarowaMiesiecznaListaPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        lst_h.ddj(fy_kw.lxa_47_inst)
        my_start_date = dn_kw.NapisDnia(self.aqr.my_start_day)
        my_end_date = dn_kw.NapisDnia(self.aqr.my_end_day)
        szereg_poborow = le_kw.dq_liczniki_poboru_w_miesiacu(self.dfb, self.table_name, self.id_obiekt, my_start_date, my_end_date)
        return lst_h.polacz_html()
