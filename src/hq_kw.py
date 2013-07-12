#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ho_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

WykresDlaFakturPomiarow = ho_kw.WykresDlaFakturPomiarow

class WykresPomiarow(WykresDlaFakturPomiarow):
    def __init__(self, tgk, aqr):
        '''
        WykresPomiarow:
        '''
        WykresDlaFakturPomiarow.__init__(self, tgk, aqr)

    def ustaw_diagnostyke(self, tekstowa_diagnostyka=0):
        '''
        WykresPomiarow:
        '''
        self.tekstowa_diagnostyka = tekstowa_diagnostyka
