#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class CommonTGK(object):
    def __init__(self):
        '''
        CommonTGK:
        '''

    def wyznacz_unikalny_moment_dla_grafiki(self):
        '''
        CommonTGK:
        '''
        self.znacznik_unik = dn_kw.zn_unik()
