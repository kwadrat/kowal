#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ckb_kw


class PorcjowanieLinii(object):
    def __init__(self, liczba):
        '''
        PorcjowanieLinii:
        '''
        self.rh_liczba = liczba
        self.zeruj()

    def zeruj(self):
        '''
        PorcjowanieLinii:
        '''
        self.rh_licznik = 0

    def paginate(self):
        '''
        PorcjowanieLinii:
        '''
        self.rh_licznik += 1
        if self.rh_licznik >= self.rh_liczba:
            self.zeruj()
            ckb_kw.both_input('Press Enter: ')
