#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ho_kw

WykresDlaFakturPomiarow = ho_kw.WykresDlaFakturPomiarow

class WykresPomiarow(WykresDlaFakturPomiarow):
    def __init__(self, tgk, aqr):
        '''
        WykresPomiarow:
        '''
        WykresDlaFakturPomiarow.__init__(self, tgk, aqr)

    def ustaw_diagnostyke(self, tekstowa_diagnostyka=0):
        '''
        WykresPomiarow:
        '''
        self.tekstowa_diagnostyka = tekstowa_diagnostyka
