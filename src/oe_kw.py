#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class LisSzerMiesiecznoRocznychFaktur(object):
    def __init__(self):
        '''
        LisSzerMiesiecznoRocznychFaktur:
        '''

    def najpierw_linia_tytulowa(self, lst_h, dfb, pokazywanie_licznikow):
        '''
        LisSzerMiesiecznoRocznychFaktur:
        '''
        tytul_zestawienia = self.linia_tytulu(dfb, self.tfi_domena, pokazywanie_licznikow)
        lst_h.ddj(tytul_zestawienia)
