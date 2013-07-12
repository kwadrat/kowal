#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import oh_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class WykresDlaFakturPomiarow:
    def __init__(self, tgk, aqr):
        '''
        WykresDlaFakturPomiarow:
        '''
        self.tgk = tgk
        self.aqr = aqr
        # Ma wartość 0 dla wykresu zbiorczego,
        # większą dla wykresu indywidualnego
        lp_miejsca = self.tgk.gen_num_miejsc.przydziel_kolejny_numer(self)
        self.dnw = oh_kw.SimpleDWN(lp_miejsca)
