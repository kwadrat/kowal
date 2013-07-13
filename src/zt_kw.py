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

class PorcjowanieLinii(object):
    def __init__(self, liczba):
        '''
        PorcjowanieLinii:
        '''
        self.rh_liczba = liczba
        self.zeruj()

    def zeruj(self):
        '''
        PorcjowanieLinii:
        '''
        self.rh_licznik = 0

    def paginate(self):
        '''
        PorcjowanieLinii:
        '''
        self.rh_licznik += 1
        if self.rh_licznik >= self.rh_liczba:
            self.zeruj()
            raw_input('Press Enter: ')
