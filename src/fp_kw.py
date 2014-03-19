#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import sf_kw
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
