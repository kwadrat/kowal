#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import en_kw
import rq_kw
import oc_kw
import ckd_kw


class LogujWiadomosci(object):
    def __init__(self):
        '''
        LogujWiadomosci:
        '''
        self.nazwa_pliku = oc_kw.LogDir + '/%d_log_kowal.txt' % rq_kw.MamBazeProd
        self.nazwa_usr_pliku = oc_kw.LogDir + '/log_kowal_usermode.txt'

    def lqg_open(self):
        '''
        LogujWiadomosci:
        '''
        self.byl_plik = os.path.isfile(self.nazwa_pliku)
        if ckd_kw.three_or_more:
            write_mode = 'a'
        else:
            write_mode = 'ab'
        try:
            self.fd = open(self.nazwa_pliku, write_mode)
        except IOError:
            print('Nie udało się otworzyć oryginalnego pliku, będę używać: %s' % self.nazwa_usr_pliku)
            self.fd = open(self.nazwa_usr_pliku, write_mode)
        return self.fd

    def lqg_write(self, napis, enter=1):
        '''
        LogujWiadomosci:
        Zapisuje do pliku podany napis.
        Opcjonalnie (domyślnie) dopisuje Enter na końcu tekstu.
        '''
        self.fd.write(en_kw.str_to_bt(napis))
        if enter:
            self.fd.write(en_kw.str_to_bt('\n'))

    def lqg_close(self):
        '''
        LogujWiadomosci:
        '''
        self.fd.close()
        if not self.byl_plik:
            os.chmod(self.nazwa_pliku, 0o660)

    def lqg_razem(self, napis, enter):
        '''
        LogujWiadomosci:
        '''
        self.lqg_open()
        self.lqg_write(napis, enter)
        self.lqg_close()


lqg_ob = LogujWiadomosci()


def diagx(napis, enter=1):
    lqg_ob.lqg_razem(napis, enter)
