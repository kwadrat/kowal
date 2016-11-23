#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import sf_kw
import jk_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

jedno_krotny = jk_kw.JednoKrotny(use_bool=1)

def zapisz_dla_diagnostyki(odp, wzor):
    if jedno_krotny.wywolaj_jednokrotnie():
        sf_kw.zapisz_plik('a', odp)
        sf_kw.zapisz_plik('b', wzor)
        raise RuntimeError('Saved to files: a b')
    else:
        raise RuntimeError('Skipped - only the first difference was saved.')

def zapisz_ladnie_diagnostyke(odp, wzor):
    sf_kw.zapisz_ladnie('a', odp)
    sf_kw.zapisz_ladnie('b', wzor)

def wassertEqual(self, odp, wzor):
    if odp != wzor:
        print
        print '|%s|' % odp
        print '|%s|' % wzor
    self.assertEqual(odp, wzor)

def vassertEqual(self, odp, wzor):
    if odp != wzor:
        print
        print '|%s|' % odp
        print '|%s|' % wzor
        if 1:
            zapisz_dla_diagnostyki(odp, wzor)
    self.assertEqual(odp, wzor)

def passertEqual(self, odp, wzor):
    if odp != wzor:
        zapisz_ladnie_diagnostyke(odp, wzor)
    self.assertEqual(odp, wzor)
