#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import rq_kw
import oc_kw

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
        try:
            self.fd = open(self.nazwa_pliku, 'ab')
        except IOError:
            print 'Nie udało się otworzyć oryginalnego pliku, będę używać:', self.nazwa_usr_pliku
            self.fd = open(self.nazwa_usr_pliku, 'ab')
        return self.fd

    def lqg_write(self, napis, enter=1):
        '''
        LogujWiadomosci:
        Zapisuje do pliku podany napis.
        Opcjonalnie (domyślnie) dopisuje Enter na końcu tekstu.
        '''
        self.fd.write(napis)
        if enter:
            self.fd.write('\n')

    def lqg_close(self):
        '''
        LogujWiadomosci:
        '''
        self.fd.close()
        if not self.byl_plik:
            os.chmod(self.nazwa_pliku, 0660)

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
