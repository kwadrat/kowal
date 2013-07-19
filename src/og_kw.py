#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ej_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class LisSzerMiesiecznychFaktur(object):
    def __init__(self):
        '''
        LisSzerMiesiecznychFaktur:
        '''

    def slupek_dla_faktur(self, tgk):
        '''
        LisSzerMiesiecznychFaktur:
        '''
        return ej_kw.FakturoweMiesieczneSlupki(tgk, self.aqr, self.dnw)
