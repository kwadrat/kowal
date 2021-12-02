#!/usr/bin/python
# -*- coding: UTF-8 -*-

import em_kw


class LisSzerRocznychFaktur(object):
    def __init__(self):
        '''
        LisSzerRocznychFaktur:
        '''

    def slupek_dla_faktur(self, tgk, rn_after):
        '''
        LisSzerRocznychFaktur:
        '''
        return em_kw.FakturoweRoczneSlupki(tgk, self.aqr, self.dnw, rn_after)
