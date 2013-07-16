#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
import oa_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KlasaOgolnaSzkieletuDat(object):
    def __init__(self):
        '''
        KlasaOgolnaSzkieletuDat:
        '''

    def przypisz_szkielet(self, nowy_szkielet):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        self.szkielet_dat = nowy_szkielet
        self.szkielet_pocz = self.szkielet_dat[0]
        self.szkielet_kon = self.szkielet_dat[-1]

    def sprowadz_do_zakresu(self, pocz, kon):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        nr_dnia = (pocz + kon) / 2
        if nr_dnia < self.szkielet_pocz:
            nr_dnia = self.szkielet_pocz
        elif nr_dnia > self.szkielet_kon:
            nr_dnia = self.szkielet_kon
        return nr_dnia

    def poziomo_tego_dnia(self, nr_dnia, szerokosc_skali, szerokosc_obrazu):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        return oa_kw.poziomo_dla_dni(self.szkielet_pocz, nr_dnia, self.szkielet_kon, szerokosc_skali, szerokosc_obrazu)

    def miejsce_umieszczenia_slupka(self, pocz, kon, szerokosc_skali, szerokosc_obrazu):
        '''
        KlasaOgolnaSzkieletuDat:
        X w połowie szerokości paska przeznaczonego na dany wykres
        '''
        nr_dnia = self.sprowadz_do_zakresu(pocz, kon)
        SlWspX = int(self.poziomo_tego_dnia(nr_dnia, szerokosc_skali, szerokosc_obrazu))
        return SlWspX

    def liczba_dat_szkieletu(self):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        return len(self.szkielet_dat)

    def malo_dat_szkieletu(self):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        return self.liczba_dat_szkieletu() < 2

    def liczba_paskow(self):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        return self.liczba_dat_szkieletu() - 1

    def pary_szkieletu(self):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        if self.szkielet_dat:
            akt = self.szkielet_pocz
            for nast in self.szkielet_dat[1:]:
                yield akt, nast
                akt = nast

    def przypisz_dla_roku_szkielet(self, wybrany_rok, rok_z_rozszerzeniem):
        '''
        KlasaOgolnaSzkieletuDat:
        '''
        tmp_szkielet = dn_kw.daty_roku(wybrany_rok, rok_z_rozszerzeniem=0)
        self.przypisz_szkielet(tmp_szkielet)

class TestOgolnegoSzkieletuDat(unittest.TestCase):
    def test_ogolnego_szkieletu_dat(self):
        '''
        TestOgolnegoSzkieletuDat:
        '''
        obk = KlasaOgolnaSzkieletuDat()
