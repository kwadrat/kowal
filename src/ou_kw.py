#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import le_kw
import lh_kw
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

class PomiarowySzeregListPoborow(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiarowySzeregListPoborow:
        '''
        OgolnySzeregListPoborow.__init__(self, tgk, dfb, krt_pobor)

    def numer_probki_na_podstawie_formularza(self):
        '''
        PomiarowySzeregListPoborow:
        '''
        tvk_data = self.tgk.wez_date()
        result = le_kw.dq_liczniki_poboru_w_roku(self.dfb, self.table_name, self.id_obiekt, tvk_data)
        return map(lambda x: x[lc_kw.fq_k_sample_qv], result)

    def przygotuj_sie_dla_listy_dni(self, lista_nr_probek):
        '''
        PomiarowySzeregListPoborow:
        '''
        tmp_lista = []
        for nr_probki in lista_nr_probek:
            elem = lu_kw.PoboryDanegoDnia(self.tgk, self.aqr, self.tekstowa_diagnostyka, self.id_obiekt, nr_probki)
            tmp_lista.append(elem)
        self.szereg_poborow = tmp_lista
        return tmp_lista

    def pobory_dla_licznikow(self, szereg_poborow):
        '''
        PomiarowySzeregListPoborow:
        '''
        for lista_poborow in szereg_poborow:
            lista_poborow.pobory_dla_parametrow(self.dfb, self.id_obiekt, self.table_name)

    def przygotuj_dla_poborow(self):
        '''
        PomiarowySzeregListPoborow:
        '''
        self.zapamietaj_wybory_formularza_poborow()
        lista_nr_probek = self.numer_probki_na_podstawie_formularza()
        szereg_poborow = self.przygotuj_sie_dla_listy_dni(lista_nr_probek)
        self.pobory_dla_licznikow(szereg_poborow)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiarowySzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        lst_h.ddj(fy_kw.lxa_47_inst)
        self.przygotuj_dla_poborow()
        self.grafika_poborow_dla_pomiarow(lst_h, krt_pobor)
        return lst_h.polacz_html()
