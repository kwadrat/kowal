#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import rq_kw
import dn_kw
import sk_kw
import ei_kw
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

class SkrARok(Skrawek):
    '''Wybór początkowego roku
    '''
    def __init__(self):
        '''
        SkrARok:
        '''
        Skrawek.__init__(self)
        self.moje_pole = ei_kw.NazwaARok

    def skh_widzialny(self, skp_okres):
        '''
        SkrARok:
        '''
        if skp_okres in rq_kw.PR_PotrzebujeARok:
            return True
        elif skp_okres in rq_kw.PR_NiePotrzebujeARok:
            return False
        else:
            raise RuntimeError('Nieznana wartosc: %s' % repr(skp_okres))

    def zbierz_html(self, tgk, dfb):
        '''
        SkrARok:
        '''
        if self.skh_widzialny(self.prm_okres.wartosc):
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, dn_kw.MozliweLataDlaARok)
        else:
            return self.wartosc_ukryta()

class TestARok(unittest.TestCase):
    def test_1_a(self):
        '''
        TestARok:
        '''
        moj_elem = SkrARok()
        moj_elem.skh_okres(None)
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.PR_Brak))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Miesiac))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_Rok))
        self.assertTrue(moj_elem.skh_widzialny(rq_kw.Dt_RapPierwszy))
        self.assertFalse(moj_elem.skh_widzialny(rq_kw.Dt_RapDrugi))
