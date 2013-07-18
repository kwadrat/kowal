#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
import sk_ht_kw
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

Skrawek = sk_ht_kw.Skrawek

class SkrPobor(Skrawek):
    '''Wybór poboru:
       - energii
       - mocy
    '''

    def __init__(self):
        '''
        SkrPobor:
        '''
        Skrawek.__init__(self)
        self.moje_pole = ei_kw.NazwaPobor

    def zbierz_html(self, tgk, dfb):
        '''
        SkrPobor:
        '''
        return sk_ht_kw.ListWyboruOgolna(tgk, self.moje_pole, lw_kw.DanePoboru)
