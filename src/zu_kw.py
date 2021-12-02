#!/usr/bin/python
# -*- coding: UTF-8 -*-

import if_kw
import rq_kw
import lm_kw

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

    def licz_przypisz_zuzycie(self, wskazowka_kiedy, jakie_zuzycie):
        '''
        ZuzycieLicznika:
        '''
        if WlaczDiagnostykeZuzycia:
            print '%s: przypisanie, %s, %s' % (self.moj_napis, wskazowka_kiedy, jakie_zuzycie)
        if wskazowka_kiedy not in self.slownik_zuzycia:
            self.slownik_zuzycia[wskazowka_kiedy] = jakie_zuzycie
        elif self.slownik_zuzycia[wskazowka_kiedy] != jakie_zuzycie:
            tmp_format = 'self.slownik_zuzycia[wskazowka_kiedy]'; print 'Eval:', tmp_format, eval(tmp_format)
            tmp_format = 'jakie_zuzycie'; print 'Eval:', tmp_format, eval(tmp_format)
            if_kw.warn_halt(rq_kw.AimToStrictWaterCanal, 'Rozne zuzycia')

    def wyczytaj_jednego(self, wskazowka_kiedy, opcjonalnie=0):
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
