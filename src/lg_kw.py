#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import sa_kw


class OkreslMiejsce(object):
    '''
    Możliwe sposoby uruchomienia:
    1. z bash przez podanie interpretera i nazwy modułu
    2. mod_wsgi/httpd
    3. z interpretera przez zaimportowanie modułu
    '''
    def zeruj_zestaw(self):
        '''
        OkreslMiejsce:
        '''
        self.to_cmd_line = False
        self.to_przz_ws_gi = False
        self.to_przz_imprt_intrpr = False

    def __init__(self):
        '''
        OkreslMiejsce:
        '''
        self.zeruj_zestaw()

    def to_bedzie_ws_gi(self):
        '''
        OkreslMiejsce:
        '''
        self.zeruj_zestaw()
        self.to_przz_ws_gi = True

    def ustaw_miejsce(self, nazwa):
        '''
        OkreslMiejsce:
        '''
        if nazwa == '__main__':
            self.zeruj_zestaw()
            self.to_cmd_line = True
        elif nazwa[-9:] == 'logika_kw':
            self.zeruj_zestaw()
            self.to_przz_imprt_intrpr = True
        elif nazwa[:10] == '_mod_wsgi_':
            self.to_bedzie_ws_gi()

    def ustaw_domowy(self, kat_dom):
        '''
        OkreslMiejsce:
        '''
        if kat_dom == '/var/www':
            self.to_bedzie_ws_gi()

    def sprawdz_linia_polecen(self):
        '''
        OkreslMiejsce:
        '''
        return self.to_cmd_line

    def sprawdz_przez_wsgi(self):
        '''
        OkreslMiejsce:
        '''
        return self.to_przz_ws_gi

    def sprawdz_import_interpr(self):
        '''
        OkreslMiejsce:
        '''
        return self.to_przz_imprt_intrpr


class TestStyku(unittest.TestCase):
    '''Sprawdza, czy poprawnie działa funkcja
    określająca miejsce wywołania (linia poleceń, WSGI)
    '''

    def test_jednego_styku(self):
        '''
        TestStyku:
        '''
        obk = OkreslMiejsce()
        wynik = obk.sprawdz_linia_polecen()
        self.assertFalse(wynik)
        obk.ustaw_miejsce('__main__')
        wynik = obk.sprawdz_linia_polecen()
        self.assertTrue(wynik)
        wynik = obk.sprawdz_import_interpr()
        self.assertFalse(wynik)
        wynik = obk.sprawdz_przez_wsgi()
        self.assertFalse(wynik)
        obk.ustaw_miejsce('_mod_wsgi_17a6fbfd067a8e6219cbaf1387f14f39')
        wynik = obk.sprawdz_przez_wsgi()
        self.assertTrue(wynik)
        wynik = obk.sprawdz_import_interpr()
        self.assertFalse(wynik)
        obk.ustaw_miejsce('logika_kw')
        wynik = obk.sprawdz_import_interpr()
        self.assertTrue(wynik)


sa_kw.UstawienieLocale()
gdzie_podlaczony = OkreslMiejsce()
