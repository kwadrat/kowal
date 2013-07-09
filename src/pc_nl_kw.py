#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

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

Miejsc_dla_ilosci = 3
Miejsc_dla_kwoty = 2

class LiczbaPrecyzyjna:
    def __init__(self, wartosc, precyzja = None):
        '''
        LiczbaPrecyzyjna:
        '''
        self.miejsc_po_przecinku = precyzja
        if self.miejsc_po_przecinku == None:
            if lm_kw.have_dec_type(wartosc):
                self.moja_wartosc = wartosc
            else:
                raise RuntimeError('wartosc = %s' % repr(wartosc))
        else:
            self.moja_wartosc = lm_kw.readjust_number(self.miejsc_po_przecinku, wartosc)

    def __repr__(self):
        '''
        LiczbaPrecyzyjna:
        '''
        return 'LP(%s)' % repr(self.moja_wartosc)

    def pob_d(self):
        '''
        LiczbaPrecyzyjna:
        '''
        return self.moja_wartosc

    def pomnoz_przez_d(self, mnoznik):
        '''
        LiczbaPrecyzyjna:
        '''
        iloczyn = self.moja_wartosc * mnoznik.pob_d()
        return LiczbaPrecyzyjna(iloczyn, self.miejsc_po_przecinku)

    def oblicz_podatek(self, akt_stopa):
        '''
        LiczbaPrecyzyjna:
        '''
        iloczyn = self.moja_wartosc * akt_stopa
        iloczyn = iloczyn / 100
        return LiczbaPrecyzyjna(iloczyn, self.miejsc_po_przecinku)

    def get_nv(self):
        '''
        LiczbaPrecyzyjna:
        '''
        napis = str(self.moja_wartosc)
        return float(napis)

    def podziel(self, dzielnik):
        '''
        LiczbaPrecyzyjna:
        '''
        return LiczbaPrecyzyjna(self.moja_wartosc / dzielnik)

    def dzielenie_d(self, dzielnik):
        '''
        LiczbaPrecyzyjna:
        '''
        return LiczbaPrecyzyjna(self.moja_wartosc / dzielnik.pob_d())

    def suma(self, dodajnik):
        '''
        LiczbaPrecyzyjna:
        '''
        return LiczbaPrecyzyjna(self.moja_wartosc + dodajnik.pob_d())

    def zwieksz(self, dodajnik):
        '''
        LiczbaPrecyzyjna:
        '''
        skladnik = dodajnik.pob_d()
        self.moja_wartosc += skladnik

    def zmniejsz(self, odejmowane):
        '''
        LiczbaPrecyzyjna:
        '''
        odjemnik = odejmowane.pob_d()
        self.moja_wartosc -= odjemnik

class TestLczPrec(unittest.TestCase):
    def testZwiekszania(self):
        '''
        TestLczPrec:
        '''
        tmp_zm = LiczbaPrecyzyjna(2.5, precyzja = 1)
        zwiekszenie = LiczbaPrecyzyjna(1, precyzja = 0)
        tmp_zm.zwieksz(zwiekszenie)
        assert tmp_zm.pob_d() == lm_kw.a2d('3.5')

class LiczbaIlosci(LiczbaPrecyzyjna):
    def __init__(self, wartosc):
        '''
        LiczbaIlosci:
        '''
        LiczbaPrecyzyjna.__init__(self, wartosc, Miejsc_dla_ilosci)

class LiczbaKwoty(LiczbaPrecyzyjna):
    def __init__(self, wartosc):
        '''
        LiczbaKwoty:
        '''
        LiczbaPrecyzyjna.__init__(self, wartosc, Miejsc_dla_kwoty)

def czy_mam_licz_prec(element):
    return isinstance(element, LiczbaPrecyzyjna)
