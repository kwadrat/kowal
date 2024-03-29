#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sf_kw
import jk_kw

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
        print('')
        print('|%s|' % odp)
        print('|%s|' % wzor)
    self.assertEqual(odp, wzor)


def vassertEqual(self, odp, wzor):
    if odp != wzor:
        print('')
        print('|%s|' % odp)
        print('|%s|' % wzor)
        if 1:
            zapisz_dla_diagnostyki(odp, wzor)
    self.assertEqual(odp, wzor)


def passertEqual(self, odp, wzor):
    if odp != wzor:
        zapisz_ladnie_diagnostyke(odp, wzor)
    self.assertEqual(odp, wzor)
