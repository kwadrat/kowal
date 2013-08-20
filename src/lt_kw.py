#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza zużycia - szereg list pomiarów, prezentacja w postacji HTML
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ze_kw
import hq_kw
import gc_kw
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
    def __init__(self, tgk, aqr, dfb, krt_pobor):
        '''
        OgolnySzeregListPoborow:
        '''
        self.dfb = dfb
        self.lista_slupkow = []
        self.table_name = krt_pobor.krt_table
        tgk.przygotuj_pobory()
        WykresPomiarow.__init__(self, tgk, aqr)
        self.id_obiekt = int(self.tgk.wez_obiekt())
        self.ustaw_diagnostyke()
