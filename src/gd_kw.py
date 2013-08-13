#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesiąca
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lh_kw
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

OgolnyPomiarowySzeregListPoborow = gc_kw.OgolnyPomiarowySzeregListPoborow

class PomiarowyMiesiecznySzeregListPoborow(OgolnyPomiarowySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiarowyMiesiecznySzeregListPoborow:
        '''
        OgolnyPomiarowySzeregListPoborow.__init__(self, tgk, dfb, krt_pobor)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiarowyMiesiecznySzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        return lst_h.polacz_html()
