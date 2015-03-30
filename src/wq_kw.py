#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import gb_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class DomenowaKlasaKwoty(object):
    def wyznacz_mi_pola(self, grupa_kolumn):
        '''
        DomenowaKlasaKwoty:
        '''
        return grupa_kolumn.rh_kolumny + grupa_kolumn.kwota_kol

    def zmien_ilosc_dla_brylantu(self, bnh):
        '''
        DomenowaKlasaKwoty:
        '''

    def teksty_domeny(self, tmp_wkrs, jedn_mocy):
        '''
        DomenowaKlasaKwoty:
        '''
        return gb_kw.Jedn_zlotowki, 'koszty', 2

    def przedstaw_pole_sumy(self, bfs):
        '''
        DomenowaKlasaKwoty:
        '''
        return bfs.pole_dla_kwoty

    def zawsze_moge_dodac_mr(self):
        '''
        DomenowaKlasaKwoty:
        '''
        return 1

    def moge_dodac_prog_mocy(self):
        '''
        DomenowaKlasaKwoty:
        '''
        return 0
