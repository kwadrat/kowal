#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list ogólny dla dnia/tygodnia/miesiąca
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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

class OgolnyPomiarowySzeregListPoborow(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        OgolnyPomiarowySzeregListPoborow:
        '''
        OgolnySzeregListPoborow.__init__(self, tgk, dfb, krt_pobor)
