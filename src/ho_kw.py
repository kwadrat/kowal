#!/usr/bin/python
# -*- coding: UTF-8 -*-

import oh_kw


class WykresDlaFakturPomiarow(object):
    def __init__(self, tgk, aqr):
        '''
        WykresDlaFakturPomiarow:
        '''
        self.tgk = tgk
        self.aqr = aqr
        # Ma wartość 0 dla wykresu zbiorczego,
        # większą dla wykresu indywidualnego
        lp_miejsca = self.tgk.gen_num_miejsc.przydziel_kolejny_numer(self)
        self.dnw = oh_kw.SimpleDNW(lp_miejsca)
