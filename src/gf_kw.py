#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lk_kw


class GenericPathAssembler(object):
    def __init__(self):
        '''
        GenericPathAssembler:
        '''

    def ustaw_poczatek_sciezki(self, cqi):
        '''
        GenericPathAssembler:
        '''
        self.cqi = cqi
        self.file_deska_data = self.cqi.file_deska_data

    def skladanie_a_sciezki(self):
        '''
        GenericPathAssembler:
        '''
        return self.skladanie_i_sciezki(lk_kw.CHC_FL)

    def skladanie_u_sciezki(self, skad_typ, jaki_obr):
        '''
        GenericPathAssembler:
        '''
        self.uy_ustaw_obr(jaki_obr)
        return self.skladanie_i_sciezki(skad_typ)

    def skladanie_r_sciezki(self):
        '''
        GenericPathAssembler:
        '''
        skad_typ = lk_kw.CHC_FL
        jaki_obr = lk_kw.CHC_PIC_NON
        return self.skladanie_u_sciezki(skad_typ, jaki_obr)


class TestOgolnegoSkladaniaSciezki(unittest.TestCase):
    def test_ogolnego_skladania_sciezki(self):
        '''
        TestOgolnegoSkladaniaSciezki:
        '''
        obk = GenericPathAssembler()
        self.assertEqual(hasattr(obk, 'ustaw_poczatek_sciezki'), True)
