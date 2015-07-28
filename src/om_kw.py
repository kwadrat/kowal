#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import em_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class LisSzerRocznychFaktur(object):
    def __init__(self):
        '''
        LisSzerRocznychFaktur:
        '''

    def slupek_dla_faktur(self, tgk, rn_after):
        '''
        LisSzerRocznychFaktur:
        '''
        return em_kw.FakturoweRoczneSlupki(tgk, self.aqr, self.dnw, rn_after)
