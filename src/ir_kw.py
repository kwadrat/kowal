#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lc_kw

class CObjectNaming(object):
    def __init__(self):
        '''
        CObjectNaming:
        '''

    def enforce_name_symbol(self, dane_faktury, tvk_junction):
        '''
        CObjectNaming:
        '''
        self.nazwa_tego_obiektu = dane_faktury[lc_kw.fq_nazwa_qv]
        if tvk_junction is None:
            self.symbol_tego_obiektu = dane_faktury[lc_kw.fq_symbol_qv]
        else:
            self.symbol_tego_obiektu = '%(main)s-%(junc_name)s' % dict(
                main=dane_faktury[lc_kw.fq_symbol_qv],
                junc_name=tvk_junction,
                )
