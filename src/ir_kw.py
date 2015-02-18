#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class CObjectNaming(object):
    def __init__(self):
        '''
        CObjectNaming:
        '''

    def enforce_name_symbol(self, dane_faktury):
        '''
        CObjectNaming:
        '''
        self.nazwa_tego_obiektu = dane_faktury[lc_kw.fq_nazwa_qv]
        self.symbol_tego_obiektu = dane_faktury[lc_kw.fq_symbol_qv]
