#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sf_kw
import dn_kw

plik_logu = 'arch_log.txt'

ZablokujLogowanie = 1


def loguj(* lista):
    if not ZablokujLogowanie:
        plik = sf_kw.otworz_do_logowania(plik_logu)
        for element_do_zapisu in lista:
            plik.write(element_do_zapisu)
            plik.write('\n')
        plik.close()


def log_sec_txt(napis):
    loguj(napis + dn_kw.SekTeraz())


def log_begin_sec():
    log_sec_txt('BGN: ')


def log_end_sec():
    log_sec_txt('END: ')
