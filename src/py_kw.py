#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import pj_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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

    def vx_buf_rd(self, kolumna, wiersz, ksztalt=None):
        '''
        ZeszytOgolny:
        '''
        if self.vx_buforowane is None:
            return self.ae.vx_odczyt(kolumna, wiersz, ksztalt=ksztalt)
        else:
            return self.vx_buforowane[(kolumna, wiersz)]
