#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Obsługa pokazywania wartości średniej (kwota / ilość)
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
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

def dwa_zera(wartosc):
    return '%.2f' % wartosc

def trzy_zera(wartosc):
    return '%.3f' % wartosc

class SrednieZuzycie(object):
    def __init__(self, kwota, zuzycie):
        '''
        SrednieZuzycie:
        '''
        self.kwota = kwota
        self.zuzycie = zuzycie

    def spodziewam_sie_dzielenia_przez_zero(self):
        '''
        SrednieZuzycie:
        '''
        return not self.zuzycie

    if rq_kw.Docelowo_psyco_nie_pygresql:
        ##############################################################################
        def moj_iloraz(self):
            '''
            SrednieZuzycie:
            '''
            return lm_kw.a2d(self.kwota) / self.zuzycie
        ##############################################################################
    else:
        ##############################################################################
        def moj_iloraz(self):
            '''
            SrednieZuzycie:
            '''
            return float(self.kwota) / float(self.zuzycie)
        ##############################################################################

    def klucz_dla_kolejnosci(self):
        '''
        SrednieZuzycie:
        '''
        if self.spodziewam_sie_dzielenia_przez_zero():
            return -1 # Gdy nie da się podzielić przez zerowe zużycie
        else:
            return self.moj_iloraz()

    def srednia_do_pokazania(self, format_sredniej):
        '''
        SrednieZuzycie:
        '''
        if self.spodziewam_sie_dzielenia_przez_zero():
            wynik = '-'
        else:
            wynik = format_sredniej % self.moj_iloraz()
        return wynik

    def srednia_napis(self):
        '''
        SrednieZuzycie:
        '''
        if self.spodziewam_sie_dzielenia_przez_zero():
            ksredni = '0'
        else:
            ksredni = dwa_zera(self.moj_iloraz())
        return ksredni

def rj_srednie_zuzycie(kwota, zuzycie):
    return SrednieZuzycie(kwota, zuzycie).srednia_napis()

class TestZaokraglania(unittest.TestCase):
    def test_zaokraglania(self):
        '''
        TestZaokraglania:
        '''
        self.assertEqual(dwa_zera(.5), '0.50')
        self.assertEqual(trzy_zera(.5), '0.500')
        self.assertEqual(rj_srednie_zuzycie(1, 0), '0')
        self.assertEqual(rj_srednie_zuzycie(1, 2), '0.50')

    if rq_kw.Docelowo_psyco_nie_pygresql:
        ##############################################################################
        def test_average_calculation(self):
            '''
            TestZaokraglania:
            '''
            SrednieZuzycie(lm_kw.a2d('1'), lm_kw.a2d('2')).moj_iloraz()
        ##############################################################################
    else:
        ##############################################################################
        def test_average_calculation(self):
            '''
            TestZaokraglania:
            '''
            SrednieZuzycie('1', 2).moj_iloraz()
        ##############################################################################
