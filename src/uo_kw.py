#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class DomenowaKlasaEnergii(object):
    def wyznacz_mi_pola(self, grupa_kolumn):
        '''
        DomenowaKlasaEnergii:
        '''
        return grupa_kolumn.rh_kolumny + grupa_kolumn.kol_energia

    def zmien_ilosc_dla_brylantu(self, bnh):
        '''
        DomenowaKlasaEnergii:
        '''

    def przedstaw_pole_sumy(self, bfs):
        '''
        DomenowaKlasaEnergii:
        '''
        return bfs.pole_dla_energii

    def zawsze_moge_dodac_mr(self):
        '''
        DomenowaKlasaEnergii:
        '''
        return 0

    def moge_dodac_prog_mocy(self):
        '''
        DomenowaKlasaEnergii:
        '''
        return 0
