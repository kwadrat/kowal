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

class ObiektLiterujacy(object):
    def __init__(self, liczba_potrzebnych_liter):
        '''
        ObiektLiterujacy:
        '''
        self.liczba_potrzebnych_liter = liczba_potrzebnych_liter
        self.biezacy_indeks_litery = 0

    def chcemy_numerowac(self):
        '''
        ObiektLiterujacy:
        '''
        return self.liczba_potrzebnych_liter > 1

    def daj_koncowke_literowa(self):
        '''
        ObiektLiterujacy:
        '''
        assert self.biezacy_indeks_litery < self.liczba_potrzebnych_liter, (
          '%d < %d' % (self.biezacy_indeks_litery, self.liczba_potrzebnych_liter))
        assert self.biezacy_indeks_litery < 26 # Liczba dostępnych liter
        koncowka = '/' + chr(ord('A') + self.biezacy_indeks_litery)
        self.biezacy_indeks_litery += 1
        return koncowka
