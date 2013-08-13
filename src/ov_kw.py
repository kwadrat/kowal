#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pokryciowy szereg list
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import le_kw
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

class PokryciowySzeregListPoborow(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PokryciowySzeregListPoborow:
        '''
        OgolnySzeregListPoborow.__init__(self, tgk, dfb, krt_pobor)

    def wizualizacja_pokrycia_poborami(self, lst_h):
        '''
        PokryciowySzeregListPoborow:
        '''
        result = le_kw.dq_dane_jednego_obiektu(self.dfb, self.table_name, self.id_obiekt)
        lt_kw.zrob_tabele_poborow(lst_h, result)

    def html_pokrycia_szeregu_poborow(self):
        '''
        PokryciowySzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        self.zapamietaj_wybory_formularza_poborow()
        self.wizualizacja_pokrycia_poborami(lst_h)
        return lst_h.polacz_html()
