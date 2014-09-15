#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class DomenowaKlasaMocy(object):
    def wyznacz_mi_pola(self, grupa_kolumn):
        '''
        DomenowaKlasaMocy:
        '''
        return grupa_kolumn.rh_kolumny

    def zmien_ilosc_dla_brylantu(self, bnh):
        '''
        DomenowaKlasaMocy:
        '''

    def teksty_domeny(self, tmp_wkrs, jedn_mocy):
        '''
        DomenowaKlasaMocy:
        '''
        return jedn_mocy, lc_kw.fq_moc_qv

    def przedstaw_pole_sumy(self, bfs):
        '''
        DomenowaKlasaMocy:
        '''
        return bfs.pole_dla_mocy

    def zawsze_moge_dodac_mr(self):
        '''
        DomenowaKlasaMocy:
        '''
        return 0
