#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import rq_kw
import chg_kw
import sk_kw
import ei_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

Skrawek = chg_kw.Skrawek

class SkrOkres(Skrawek):
    '''Wybór okresu:
       - w latach (całe lata pokazujemy na wykresie)
       - rok (tylko konkretny rok)
       - Raport 1
       - Raport 2
    '''

    def __init__(self):
        '''
        SkrOkres:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaOkres
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaOkres
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrOkres:
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneOkresu)
            ##############################################################################
        else:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, rq_kw.DaneOkresu)
            ##############################################################################
