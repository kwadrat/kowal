#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''Obsługa łańcucha zbiorczego dla kawałków kodu HTML
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hv_kw
import ze_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class LancOgolOgniw(object):
    def __init__(self):
        '''
        LancOgolOgniw:
        '''
        self.lista = []

    def dolcz(self, napis):
        '''
        LancOgolOgniw:
        '''
        self.lista.append(napis)

    def polaczona_tresc(self):
        '''
        LancOgolOgniw:
        '''
        return ''.join(self.lista)

    def rozp_wiersza(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_67c_pocz_wiersza)

    def zak_wiersza(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_67c_kon_wiersza)

    def zak_tabeli(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_1c_kon_tabeli)

    def rozp_komorki(self, class_=None):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.op_td(class_=class_))

    def zak_komorki(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_1c_kon_komorki)

    def zak_slct(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_1c_kon_slct)

    def zak_formularza(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_1c_kon_formularza)

    def miedzy_wierszami(self):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.formularz_67c_kon_wiersza)
        self.dolcz(ze_kw.op_tr())

    def kobalt(self, kropelka, ten_styl='', ten_col_span=None, ten_row_span=None, title=None):
        '''
        LancOgolOgniw:
        '''
        self.pocz_kom(
            ten_styl=ten_styl,
            ten_col_span=ten_col_span,
            ten_row_span=ten_row_span,
            title=title,
            )
        self.dolcz(kropelka)
        self.zak_komorki()

    def dwu_zerowo(self, slownik, etykieta):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(hv_kw.dwa_zera(slownik[etykieta]))

    def troj_zerowo(self, slownik, etykieta):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(hv_kw.trzy_zera(slownik[etykieta]))

    def tq_srednie_zuzycie(self, slownik, fvk_pole_z_kwota, fvk_pole_z_iloscia):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(hv_kw.rj_srednie_zuzycie(slownik[fvk_pole_z_kwota], slownik[fvk_pole_z_iloscia]))

    def rtj_wspolny_wybor_opcji(self, oh_wspolny, etyk, wartosc):
        '''
        LancOgolOgniw:
        '''
        self.dolcz(ze_kw.op_option(
            etyk,
            wartosc,
            oh_wspolny.mt_wybrany(wartosc)))

    def to_t_cast(self, elem):
        '''
        LancOgolOgniw:
        '''
        self.dolcz('%s' % elem)

class TestOgolnegoLancucha(unittest.TestCase):
    def test_calego_lancucha(self):
        '''
        TestOgolnegoLancucha:
        '''
        obk = LancOgolOgniw()
        obk.dolcz('napis')
        obk.dolcz('a')
        obk.dolcz('b')
        obk.dolcz('c')
        obk.to_t_cast(0)
        self.assertEqual(obk.polaczona_tresc(), 'napisabc0')

    def test_dzielenia_przez_zero(self):
        '''
        TestOgolnegoLancucha:
        '''
        obk = LancOgolOgniw()
        obk.tq_srednie_zuzycie(dict(k=1, i=0), 'k', 'i')
        self.assertEqual(obk.polaczona_tresc(), '0')

    def test_dzielenia_przez_dwa(self):
        '''
        TestOgolnegoLancucha:
        '''
        obk = LancOgolOgniw()
        obk.tq_srednie_zuzycie(dict(k=1, i=2), 'k', 'i')
        self.assertEqual(obk.polaczona_tresc(), '0.50')

    def test_rozp_zwyklej_komorki(self):
        '''
        TestOgolnegoLancucha:
        '''
        obk = LancOgolOgniw()
        obk.rozp_komorki()
        self.assertEqual(obk.polaczona_tresc(), '<td>')
