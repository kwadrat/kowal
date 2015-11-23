#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ib_kw
import rq_kw
import dn_kw
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

Skrawek = sk_kw.Skrawek

class SkrWybranyRok(Skrawek):
    '''Wybór początkowego roku
    '''
    def __init__(self):
        '''
        SkrWybranyRok:
        '''
        Skrawek.__init__(self)
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaARok
            ##############################################################################
        else:
            ##############################################################################
            self.moje_pole = ei_kw.NazwaARok
            ##############################################################################

    def zbierz_html(self, tgk, dfb):
        '''
        SkrWybranyRok:
        '''
        if 1:
            if ib_kw.AimToObjectFieldName:
                ##############################################################################
                result = sk_kw.ListWyboruOgolna(tgk, self.moje_pole, dn_kw.MozliweLataDlaARok)
                ##############################################################################
            else:
                ##############################################################################
                result = sk_kw.ListWyboruOgolna(tgk, self.moje_pole, dn_kw.MozliweLataDlaARok)
                ##############################################################################
                return result
