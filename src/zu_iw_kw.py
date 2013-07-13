#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

WlaczDiagnostykeZuzycia = 0

class ZuzycieLicznika(object):
    def __init__(self, napis):
        '''
        ZuzycieLicznika:
        '''
        self.slownik_zuzycia = {}
        self.moj_napis = napis
        if WlaczDiagnostykeZuzycia:
            print '%s: rozpoczecie' % self.moj_napis

    def licz_przypisz_zuzycie(self, wskazowka_kiedy, zuzycie):
        '''
        ZuzycieLicznika:
        '''
        if WlaczDiagnostykeZuzycia:
            print '%s: przypisanie, %s, %s' % (self.moj_napis, wskazowka_kiedy, zuzycie)
        if wskazowka_kiedy not in self.slownik_zuzycia:
            self.slownik_zuzycia[wskazowka_kiedy] = zuzycie
        elif self.slownik_zuzycia[wskazowka_kiedy] != zuzycie:
            tmp_format = 'self.slownik_zuzycia[wskazowka_kiedy]'; print 'Eval:', tmp_format, eval(tmp_format)
            tmp_format = 'zuzycie'; print 'Eval:', tmp_format, eval(tmp_format)
            raise RuntimeError('Rozne zuzycia')

    def wyczytaj_jednego(self, wskazowka_kiedy, opcjonalnie = 0):
        '''
        ZuzycieLicznika:
        '''
        if WlaczDiagnostykeZuzycia:
            print '%s: wyczyt, %s' % (self.moj_napis, wskazowka_kiedy)
        if not opcjonalnie or wskazowka_kiedy in self.slownik_zuzycia:
            return self.slownik_zuzycia[wskazowka_kiedy]
        else:
            return lm_kw.wartosc_zero_globalna

    def wyczytaj_klucze(self):
        '''
        ZuzycieLicznika:
        '''
        if WlaczDiagnostykeZuzycia:
            print '%s: jakie_mam_klucze' % (self.moj_napis)
        return self.slownik_zuzycia.keys()
