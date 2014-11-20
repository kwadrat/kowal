#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
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

class SkrPoborowegoCzasu(Skrawek):
    '''
    Wybór okresu poboru:
    - dzień
    - tydzień
    - miesiąc
    '''
    def __init__(self, fs_prefix=None):
        '''
        SkrPoborowegoCzasu:
        '''
        Skrawek.__init__(self, fs_prefix)
        self.moje_pole = ei_kw.NazwaPobCzas

    def zbierz_html(self, tgk, dfb):
        '''
        SkrPoborowegoCzasu:
        '''
        return sk_kw.ListWyboruOgolna(tgk, self.moje_pole, lw_kw.DanePoborowegoCzasu)
