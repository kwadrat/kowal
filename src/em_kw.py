#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
import es_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

MojeSlupki = es_kw.MojeSlupki

class FakturoweRoczneSlupki(MojeSlupki):
    def __init__(self, tgk, aqr, dwk):
        '''
        FakturoweRoczneSlupki:
        '''
        MojeSlupki.__init__(self, tgk, aqr, dwk)

    def ustaw_skalowanie_obrazu(self):
        '''
        FakturoweRoczneSlupki:
        '''
        self.ustaw_skalowany_obraz()

    def wyznacz_etykiete(self, pocz):
        '''
        FakturoweRoczneSlupki:
        '''
        return str(dn_kw.RokDnia(pocz))
