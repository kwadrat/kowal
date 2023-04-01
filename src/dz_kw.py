#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import unittest

import du_kw

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

wzor_day_csv = re.compile(r'''
^
(?P<year>\d{4})
-
(?P<month>\d{2})
-
(?P<day>\d{2})
$
''', re.VERBOSE)

wzor_day_full = re.compile(r'''
^
(?P<month>\d{1,2})
/
(?P<day>\d{1,2})
/
(?P<year>\d{4})
\s
(?P<hour>\d{1,2})
:
(?P<minute>\d{2})
$
''', re.VERBOSE)

changed_coding_date_pattern = re.compile(r'''
^
(?P<month>\d{1,2})
-
(?P<day>\d{1,2})
-
(?P<year>\d{4})
\s
00:00:00
$
''', re.VERBOSE)

changed_coding_date_format = '%(year)s-%(month)s-%(day)s'


def wyciagnij_date_z_formatu_dmr(napis):
    res = wzor_data_dzien_miesiac_rok.search(napis)
    if res:
        wynik = list(map(int, (res.group('year', 'month', 'day'))))
    else:
        raise RuntimeError('Nierozpoznana data?: %s' % repr(napis))
    return wynik


def extract_csv_hour(napis):
    res = wzor_hour_csv.search(napis)
    if res:
        wynik = list(map(int, (res.group('hour', 'minute'))))
    else:
        wynik = None
    return wynik


def extract_csv_day(napis):
    res = wzor_day_csv.search(napis)
    if res:
        wynik = list(map(int, (res.group('year', 'month', 'day'))))
    else:
        wynik = None
    return wynik


def extract_csv_full(napis):
    res = wzor_day_full.search(napis)
    if res:
        wynik = list(map(int, (res.group('year', 'month', 'day', 'hour', 'minute'))))
    else:
        wynik = None
    return wynik


def convert_date_pwik(changed_coding_txt):
    res = changed_coding_date_pattern.search(changed_coding_txt)
    if res:
        result = changed_coding_date_format % res.groupdict()
    else:
        result = None
    return result


def convert_float_pwik(changed_coding_txt):
    return changed_coding_txt.replace(' ', '')


def convert_integer_pwik(changed_coding_txt):
    result = changed_coding_txt.replace(' ', '')
    if result[-3:] == ',00':
        result = result[:-3]
    return result


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
        self.assertEqual(extract_csv_day('2006-04-24'), [2006, 4, 24])
        self.assertEqual(extract_csv_full('7/31/2013 22:16'), [2013, 7, 31, 22, 16])

    def test_pwik_csv(self):
        '''
        TestRozpoznawania:
        '''
        self.assertEqual(convert_date_pwik('12-30-2014 00:00:00'), '2014-12-30')
        self.assertEqual(convert_float_pwik('2 692,38'), '2692,38')
        self.assertEqual(convert_integer_pwik('9 432 334,00'), '9432334')
