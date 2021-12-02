#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pj_kw


class ZeszytOgolny(object):
    def podlacz_arkusz_tego_pliku(self, pae, nazwa_pliku, nazwa_arkusza):
        '''
        ZeszytOgolny:
        '''
        self.vx_ss = pae.otworz_plik_tego_zeszytu(nazwa_pliku)
        self.sh = self.vx_ss.Sheets(nazwa_arkusza)
        self.ae = pj_kw.ArkuszExcel(self.sh)

    def ustaw_bufor(self, slownik):
        '''
        ZeszytOgolny:
        '''
        self.vx_buforowane = slownik

    def __init__(self):
        '''
        ZeszytOgolny:
        '''
        self.ustaw_bufor(None)

    def zamknij_zeszyt(self):
        '''
        ZeszytOgolny:
        '''
        self.ae = None
        self.sh = None
        self.vx_ss.Close()
        self.vx_ss = None
        self.ustaw_bufor(None)

    def vx_buf_rd(self, lb_col, wiersz, ksztalt=None):
        '''
        ZeszytOgolny:
        '''
        if self.vx_buforowane is None:
            return self.ae.vx_odczyt(lb_col, wiersz, ksztalt=ksztalt)
        else:
            return self.vx_buforowane[(lb_col, wiersz)]
