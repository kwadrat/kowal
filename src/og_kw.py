#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ej_kw

class LisSzerMiesiecznychFaktur(object):
    def __init__(self):
        '''
        LisSzerMiesiecznychFaktur:
        '''

    def slupek_dla_faktur(self, tgk, rn_after):
        '''
        LisSzerMiesiecznychFaktur:
        '''
        return ej_kw.FakturoweMiesieczneSlupki(tgk, self.aqr, self.dnw, rn_after)
