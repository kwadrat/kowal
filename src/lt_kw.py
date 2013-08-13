#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza zużycia - szereg list pomiarów, prezentacja w postacji HTML
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ey_kw
import hq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

WykresPomiarow = hq_kw.WykresPomiarow

class OgolnySzeregListPoborow(WykresPomiarow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        OgolnySzeregListPoborow:
        '''
        self.dfb = dfb
        self.lista_slupkow = []
        self.table_name = krt_pobor.krt_table
        aqr = ey_kw.SzkieletDatDlaPoborow(krt_pobor)
        tgk.przygotuj_pobory(aqr, self.dfb)
        WykresPomiarow.__init__(self, tgk, aqr)
        self.ustaw_diagnostyke()

    def zapamietaj_wybory_formularza_poborow(self):
        '''
        OgolnySzeregListPoborow:
        '''
        self.id_obiekt = int(self.tgk.wez_obiekt())

    def grafika_poborow_dla_pomiarow(self, lst_h, krt_pobor, szereg_poborow):
        '''
        OgolnySzeregListPoborow:
        '''
        for lista_poborow in szereg_poborow:
            lista_poborow.html_ls_poborow(lst_h, krt_pobor)
