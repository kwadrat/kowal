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
import lh_kw
import jb_kw
import ey_kw
import wn_kw
import eq_kw
import lu_kw
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

class PomiarowyDziennaListaPoborow(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiarowyDziennaListaPoborow:
        '''
        aqr = ey_kw.SzkieletDatDlaPoborow(krt_pobor)
        OgolnySzeregListPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def grafika_poborow_dla_pomiarow(self, lst_h, krt_pobor, szereg_poborow):
        '''
        PomiarowyDziennaListaPoborow:
        '''
        for lista_poborow in szereg_poborow:
            lista_poborow.html_ls_poborow(lst_h, krt_pobor, self.dfb, self.id_obiekt, self.table_name)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiarowyDziennaListaPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        lst_h.ddj(fy_kw.lxa_47_inst)
        tvk_data = self.tgk.wez_date()
        result = le_kw.dq_liczniki_poboru_w_roku(self.dfb, self.table_name, self.id_obiekt, tvk_data)
        lista_nr_probek = map(lambda x: x[lc_kw.fq_k_sample_qv], result)
        szereg_poborow = []
        for nr_probki in lista_nr_probek:
            elem = lu_kw.PoboryDanegoDnia(self.tgk, self.aqr, self.id_obiekt, nr_probki)
            szereg_poborow.append(elem)
        self.grafika_poborow_dla_pomiarow(lst_h, krt_pobor, szereg_poborow)
        return lst_h.polacz_html()
