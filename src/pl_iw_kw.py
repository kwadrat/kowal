#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import po_iw_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

PozycjeOgolne = po_iw_kw.PozycjeOgolne

class PozycjeLicznikowe(PozycjeOgolne):
    def __init__(self, etykieta, slownik_poczatkowy = None):
        '''
        PozycjeLicznikowe:
        '''
        PozycjeOgolne.__init__(self, etykieta, slownik_poczatkowy)

    def __repr__(self):
        '''
        PozycjeLicznikowe:
        '''
        return self.wzorzec_repr('PozycjeLicznikowe')

    def podaj_ciag(self):
        '''
        PozycjeLicznikowe:
        '''
        return self.klucze_chronologicznie()

    def zwroc_drugiego(self, klucz):
        '''
        PozycjeLicznikowe:
        '''
        return self.pobierz_element(klucz)
