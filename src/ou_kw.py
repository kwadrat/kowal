#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lh_kw
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
    def __init__(self, tgk, dfb):
        '''
        PomiarowySzeregListPoborow:
        '''
        OgolnySzeregListPoborow.__init__(self, tgk, dfb)

    def przygotuj_dla_poborow(self):
        '''
        PomiarowySzeregListPoborow:
        '''
        self.zapamietaj_wybory_formularza_poborow()
        lista_nr_probek = self.numer_probki_na_podstawie_formularza()
        self.przygotuj_sie_dla_listy_dni(lista_nr_probek)
        self.pobory_dla_licznikow()

    def html_szeregu_poborow(self, on_mouse):
        '''
        PomiarowySzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        lst_h.ddj(fy_kw.lxa_47_inst)
        self.przygotuj_dla_poborow()
        self.grafika_poborow_dla_pomiarow(lst_h, on_mouse)
        return lst_h.polacz_html()
