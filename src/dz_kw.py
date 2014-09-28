#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import du_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

etykieta_wzoru = 'calosc'
# Może taka data w ogóle nie występować, jeśli ktoś nigdy
# wcześniej nie popełnił błędu przy logowaniu
# '2011-12-16'
wzor_dzisiejszy_dzien = re.compile(r'''
^
(?P<''' + etykieta_wzoru + r'''>
(
\d{4}
-
\d{2}
-
\d{2}
)?
)
''', re.VERBOSE)
# 'ca4gqn8bdddb108uvu057u2rg5'
wzor_sesji_trns_plikow = re.compile(r'''
^
(?P<''' + etykieta_wzoru + r'''>
[a-z0-9]{26}
)
''', re.VERBOSE)
# '0c2fe1d7ea468ee02fdbea20c47a6c67'
wzor_sumy_polaczonej = re.compile(r'''
^
(?P<''' + etykieta_wzoru + r'''>
[a-f0-9]{32}
)
''', re.VERBOSE)
wzor_adresu_poczty = re.compile(r'''
^
([-%\+\w]+
\.)*
[-%\+\w]+
@
([-\w]+
\.)+
[-\w]+
$
''', re.VERBOSE)

wzor_plik_dwg = re.compile(r'''
(?P<''' + etykieta_wzoru + r'''>
.+
\.dwg
)$
''', re.VERBOSE + re.IGNORECASE)

wzor_data_dzien_miesiac_rok = re.compile(r'''
^
(?P<day>\d{2})
-
(?P<month>\d{2})
-
(?P<year>\d{4})
$
''', re.VERBOSE)

wzor_hour_csv = re.compile(r'''
^
(?P<hour>\d{1,2})
:
(?P<minute>\d{2})
$
''', re.VERBOSE)

def wyciagnij_date_z_formatu_dmr(napis):
    res = wzor_data_dzien_miesiac_rok.search(napis)
    if res:
        wynik = map(int, (res.group('year', 'month', 'day')))
    else:
        raise RuntimeError('Nierozpoznana data?: %s' % repr(napis))
    return wynik

def extract_csv_hour(napis):
    res = wzor_hour_csv.search(napis)
    if res:
        wynik = map(int, (res.group('hour', 'minute')))
    else:
        wynik = None
    return wynik

def rozpoznaj_wedlug_wyr_regul(wzorzec_reg, napis):
    wynik = None
    res = wzorzec_reg.search(napis)
    if res:
        podciag = res.group(etykieta_wzoru)
        wynik = len(podciag)
    return wynik

def rozpoznaj_dzisiejszy_dzien(napis):
    return rozpoznaj_wedlug_wyr_regul(wzor_dzisiejszy_dzien, napis)

def rozpoznaj_sesje_trns_plikow(napis):
    return rozpoznaj_wedlug_wyr_regul(wzor_sesji_trns_plikow, napis)

def rozpoznaj_sume_polaczona(napis):
    return rozpoznaj_wedlug_wyr_regul(wzor_sumy_polaczonej, napis)

def rozpoznaj_plik_dwg(napis):
    return rozpoznaj_wedlug_wyr_regul(wzor_plik_dwg, napis)

def sprawdz_adres_poczty(napis):
    return wzor_adresu_poczty.search(napis)

class TestRozpoznawania(unittest.TestCase):
    def test_sprawdzania_co_do_dnia(self):
        '''
        TestRozpoznawania:
        '''
        self.assertEqual(rozpoznaj_dzisiejszy_dzien(''), 0)
        self.assertEqual(rozpoznaj_dzisiejszy_dzien('2011-12-16'), 10)
        self.assertEqual(rozpoznaj_dzisiejszy_dzien(du_kw.rjb_data_przkl), 10)

    def test_sprawdzania_sesji_dla_trns_plikow(self):
        '''
        TestRozpoznawania:
        '''
        self.assertEqual(rozpoznaj_sesje_trns_plikow(''), None)
        self.assertEqual(rozpoznaj_sesje_trns_plikow('ca4gqn8bdddb108uvu057u2rg5'), 26)
        self.assertEqual(rozpoznaj_sesje_trns_plikow('ipoetki7gf95ag2mrburspjq12 '), 26)

    def test_sprawdzania_sumy_polaczonej(self):
        '''
        TestRozpoznawania:
        '''
        self.assertEqual(rozpoznaj_sume_polaczona(''), None)
        self.assertEqual(rozpoznaj_sume_polaczona('0c2fe1d7ea468ee02fdbea20c47a6c67'), 32)
        self.assertEqual(rozpoznaj_sume_polaczona('c75777a28aec8af5315c71193bec3690 '), 32)

    def test_adresow_pocztowych(self):
        '''
        TestRozpoznawania:
        '''
        self.assertFalse(sprawdz_adres_poczty('1'))
        self.assertTrue(sprawdz_adres_poczty('abc@w.pl'))

    def test_sprawdzania_plikow_dwg(self):
        '''
        TestRozpoznawania:
        '''
        self.assertEqual(rozpoznaj_plik_dwg(''), None)
        self.assertEqual(rozpoznaj_plik_dwg('abc.dwg'), 7)
        self.assertEqual(rozpoznaj_plik_dwg('X.DWG'), 5)

    def test_daty_dzien_miesiac_rok(self):
        '''
        TestRozpoznawania:
        '''
        self.assertRaises(RuntimeError, wyciagnij_date_z_formatu_dmr, '2006-04-24')
        self.assertEqual(wyciagnij_date_z_formatu_dmr(u'24-04-2006'), [2006, 4, 24])

    def test_czasowy_txt_csv(self):
        '''
        TestRozpoznawania:
        '''
        self.assertEqual(extract_csv_hour('1:00'), [1, 0])
