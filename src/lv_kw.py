#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import lw_kw
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

class SkrPobor(Skrawek):
    '''Wybór poboru:
       - energii
       - mocy
    '''

    def __init__(self, fs_prefix=None):
        '''
        SkrPobor:
        '''
        Skrawek.__init__(self, fs_prefix)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaPobor
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaPobor
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrPobor:
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, lw_kw.DanePoboru)
            ##############################################################################
        else:
            ##############################################################################
            return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, lw_kw.DanePoboru)
            ##############################################################################
