#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
import dq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

KlasaOgolnaSzkieletuDat = dq_kw.KlasaOgolnaSzkieletuDat

class KlasaSzkieletuDat(KlasaOgolnaSzkieletuDat):
    def __init__(self):
        '''
        KlasaSzkieletuDat:
        '''
        KlasaOgolnaSzkieletuDat.__init__(self)
        self.szkielet_dat = []

    def skrajne_daty(self):
        '''
        KlasaSzkieletuDat:
        '''
        return self.szkielet_pocz, self.szkielet_kon

    def kolejne_dni_szkieletu(self):
        '''
        KlasaSzkieletuDat:
        '''
        return range(self.szkielet_pocz, self.szkielet_kon)

    def rok_poczatku(self):
        '''
        KlasaSzkieletuDat:
        '''
        return dn_kw.RokDnia(self.szkielet_pocz)
