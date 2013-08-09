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
    def __init__(self, tgk, dfb):
        '''
        PokryciowySzeregListPoborow:
        '''
        OgolnySzeregListPoborow.__init__(self, tgk, dfb)

    def numer_probki_pokrycia_na_podstawie_formularza(self):
        '''
        PokryciowySzeregListPoborow:
        '''
        result = le_kw.dq_ogolnie_liczniki_poboru(self.dfb, self.table_name, self.id_obiekt)
        return map(lambda x: x[lc_kw.fq_k_sample_qv], result)

    def html_pokrycia_szeregu_poborow(self):
        '''
        PokryciowySzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        self.zapamietaj_wybory_formularza_poborow()
        self.wizualizacja_pokrycia_poborami(lst_h)
        return lst_h.polacz_html()
