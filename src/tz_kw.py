#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
import sk_ht_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

Skrawek = sk_ht_kw.Skrawek

class SkrWyborEnObiektu(Skrawek):
    '''Wybór aktywnych (ważnych) obiektów lub wszystkich (łącznie z testowymi)
    '''

    def __init__(self, moje_pole):
        '''
        SkrWyborEnObiektu:
        '''
        Skrawek.__init__(self)
        self.moje_pole = moje_pole

    def zbierz_html(self, tgk, dfb):
        '''
        SkrWyborEnObiektu:
        '''
        return sk_ht_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneAktWsz)

class TestAktWsz(unittest.TestCase):
    def test_1_a(self):
        '''
        TestAktWsz:
        '''
        moj_elem = SkrWyborEnObiektu()
