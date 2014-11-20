#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import dn_kw
import sk_kw
import ei_kw
import ro_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

Skrawek = sk_kw.Skrawek

class SkrZuzRok(Skrawek):
    '''Wybór roku dla analizy zużyć.
    '''

    def __init__(self):
        '''
        SkrZuzRok:
        '''
        Skrawek.__init__(self)
        self.moje_pole = ei_kw.NazwaRok

    def analiza_parametrow(self, tgk, dfb):
        '''
        SkrZuzRok:
        '''
        self.wartosc = tgk.qparam.get(self.moje_pole, None)
        if self.wartosc == None:
            # Domyślnie pokazujemy aktualny rok
            self.wartosc = dn_kw.RokTeraz()
        return self.wartosc != None

    def zbierz_html(self, tgk, dfb):
        '''
        SkrZuzRok:
        '''
        return ro_kw.ListaWyboruRoku(tgk)

class TestZuzRok(unittest.TestCase):
    def test_1_a(self):
        '''
        TestZuzRok:
        '''
        moj_elem = SkrZuzRok()
