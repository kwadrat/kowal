#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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

class SkrBRok(Skrawek):
    '''Wybór końcowego roku
    '''

    def skh_arok(self, elem_arok):
        '''
        SkrBRok:
        '''
        self.elem_arok = elem_arok

    def __init__(self):
        '''
        SkrBRok:
        '''
        Skrawek.__init__(self)
        self.moje_pole = ei_kw.NazwaBRok

    def skh_a_widzialny(self, prm_arok):
        '''
        SkrBRok:
        '''
        if prm_arok in rq_kw.NiePtrzBRok:
            return False
        else:
            return True

    def skh_widzialny(self, mam_arok, chce_brok):
        '''
        SkrBRok:
        '''
        return mam_arok and chce_brok

    def zbierz_html(self, tgk, dfb):
        '''
        SkrBRok:
        '''
        mam_arok = self.elem_arok.skh_widzialny(self.prm_okres.wartosc)
        chce_brok = self.skh_a_widzialny(self.elem_arok.wartosc)
        if self.skh_widzialny(mam_arok, chce_brok):
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, dn_kw.MozliweLataDlaBRok)
        else:
            return self.wartosc_ukryta()

class TestBRok(unittest.TestCase):
    def test_1_a(self):
        '''
        TestBRok:
        '''
        moj_elem = SkrBRok()
        moj_elem.skh_okres(None)
        moj_elem.skh_arok(None)
        self.assertFalse(moj_elem.skh_a_widzialny(None))
        self.assertFalse(moj_elem.skh_a_widzialny(rq_kw.PoleWszystko))
        self.assertTrue(moj_elem.skh_a_widzialny('2005'))
        self.assertFalse(moj_elem.skh_widzialny(False, False))
        self.assertFalse(moj_elem.skh_widzialny(False, True))
        self.assertFalse(moj_elem.skh_widzialny(True, False))
        self.assertTrue(moj_elem.skh_widzialny(True, True))
