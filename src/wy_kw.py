#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Wyjątki w datach faktur energii elektrycznej
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def zrob_same_daty(napis):
    zebrane = []
    for linia in napis.splitlines():
        segmenty = linia.split()
        data_pocz = segmenty[0]
        data_kon = segmenty[1]
        zebrane.append((data_pocz, data_kon))
    return frozenset(zebrane)

# C-21
faktura_c_21_jest_niezrozumiala = zrob_same_daty('''\
2010-10-01 2010-12-31 Szkoła Podstawowa nr 20
''')

faktura_c_21_ma_poltora_miesiaca = zrob_same_daty('''\
2010-01-15 2010-02-28 Szkoła Podstawowa nr 35
''')

# C-21C
tylko_koncowa_data_jest_dobra = zrob_same_daty('''\
2010-01-31 2010-02-28 Szkoła Podstawowa nr 3 im. Św. Stanisława Kostki
2010-08-31 2010-09-30 Gimnazjum nr 4
2012-06-30 2012-07-31 Gimnazjum nr 4
2011-11-29 2011-12-31 Zespół Szkół nr 2
2013-05-29 2013-06-30 Urząd Miasta-Rzeczna
2015-06-29 2015-07-31 Zespół Szkolno-Przedszkolny nr 7
''')

faktura_jest_za_dwa_miesiace = zrob_same_daty('''\
2011-02-01 2011-03-31 Szkoła Podstawowa nr 3 im. Św. Stanisława Kostki
2011-01-01 2011-02-28 Zespół Szkolno-Przedszkolny nr 3
2013-01-01 2013-02-28 Szkoła Podstawowa nr 34
''')

faktura_jest_za_trzy_miesiace = zrob_same_daty('''\
2011-08-30 2011-11-28 Zespół Szkół nr 2
2011-08-30 2011-10-31 Zespół Szkół nr 2
2015-10-01 2015-12-31 Zespół Szkół nr 2
''')

faktura_jest_niezrozumiala = zrob_same_daty('''\
2011-01-02 2011-02-28 Szkoła Podstawowa nr 11
2010-01-01 2010-02-06 Gimnazjum nr 11
''')

def okresl_spcf_dla_blednych(data_pocz, data_kon):
    krotka_dat = (data_pocz, data_kon)
    if krotka_dat in tylko_koncowa_data_jest_dobra:
        spcf_wyznaczona = dn_kw.rok_mies_z_napisu(data_kon)
    elif krotka_dat in faktura_jest_za_dwa_miesiace:
        spcf_wyznaczona = dn_kw.rok_mies_z_napisu(data_kon)
    elif krotka_dat in faktura_jest_za_trzy_miesiace:
        spcf_wyznaczona = dn_kw.rok_mies_z_napisu(data_kon)
    elif krotka_dat in faktura_jest_niezrozumiala:
        spcf_wyznaczona = dn_kw.rok_mies_z_napisu(data_kon)
    elif krotka_dat in faktura_c_21_jest_niezrozumiala:
        spcf_wyznaczona = dn_kw.rok_mies_z_napisu(data_pocz)
    elif krotka_dat in faktura_c_21_ma_poltora_miesiaca:
        spcf_wyznaczona = dn_kw.rok_mies_z_napisu(data_kon)
    else:
        spcf_wyznaczona = None
    return spcf_wyznaczona

def oba_konce_miesiecy(data_pocz, data_kon):
    numer_a = dn_kw.napis_na_numer_dnia(data_pocz)
    numer_b = numer_a + 1
    numer_c = dn_kw.napis_na_numer_dnia(data_kon)
    numer_d = numer_c + 1
    rm_dla_a = dn_kw.RokMscDnia(numer_a)
    rm_dla_b = dn_kw.RokMscDnia(numer_b)
    rm_dla_c = dn_kw.RokMscDnia(numer_c)
    rm_dla_d = dn_kw.RokMscDnia(numer_d)
    if (rm_dla_a != rm_dla_b and # Koniec miesiąca
            rm_dla_c != rm_dla_d and # Koniec miesiąca
            rm_dla_b == rm_dla_c): # Między końcami jest dokładnie jeden miesiąc
        spcf_wyznaczona = rm_dla_c
    else:
        spcf_wyznaczona = None
    return spcf_wyznaczona

def dates_of_energy_as_month_and_year(data_pocz, data_kon):
    spcf_pocz = okresl_spcf_dla_blednych(data_pocz, data_kon)
    if spcf_pocz is None:
        spcf_pocz = oba_konce_miesiecy(data_pocz, data_kon)
    if spcf_pocz is None:
        spcf_pocz = dn_kw.one_common_date_of_energy_as_month_and_year(data_pocz, data_kon)
    return spcf_pocz

class TestNiejasnychDatEnElektr(unittest.TestCase):
    def test_energy_date(self):
        '''
        TestNiejasnychDatEnElektr:
        '''
        self.assertEqual(dates_of_energy_as_month_and_year('2010-01-01', '2010-01-30'), (2010, 1))
        self.assertEqual(dates_of_energy_as_month_and_year('2010-01-31', '2010-02-28'), (2010, 2))
        self.assertEqual(dates_of_energy_as_month_and_year('2010-08-31', '2010-09-30'), (2010, 9))
        self.assertEqual(dates_of_energy_as_month_and_year('2011-02-01', '2011-03-31'), (2011, 3))
        self.assertEqual(dates_of_energy_as_month_and_year('2011-01-02', '2011-02-28'), (2011, 2))
        self.assertEqual(dates_of_energy_as_month_and_year('2011-01-01', '2011-02-28'), (2011, 2))
        self.assertEqual(dates_of_energy_as_month_and_year('2012-06-30', '2012-07-31'), (2012, 7))
        self.assertEqual(dates_of_energy_as_month_and_year('2011-08-30', '2011-11-28'), (2011, 11))
        self.assertEqual(dates_of_energy_as_month_and_year('2011-11-29', '2011-12-31'), (2011, 12))
        self.assertEqual(dates_of_energy_as_month_and_year('2010-10-01', '2010-12-31'), (2010, 10))
        self.assertEqual(dates_of_energy_as_month_and_year('2010-01-15', '2010-02-28'), (2010, 2))
        self.assertEqual(dates_of_energy_as_month_and_year('2011-08-30', '2011-10-31'), (2011, 10))
        self.assertEqual(dates_of_energy_as_month_and_year('2013-01-01', '2013-02-28'), (2013, 2))
        self.assertRaises(RuntimeError, dates_of_energy_as_month_and_year, '2010-01-01', '2010-02-01')

    def test_faktury_koncow_miesiecy(self):
        '''
        TestNiejasnychDatEnElektr:
        '''
        self.assertEqual(oba_konce_miesiecy('2013-05-31', '2013-06-30'), (2013, 6))
        self.assertEqual(oba_konce_miesiecy('2013-05-31', '2013-06-29'), None)
        self.assertEqual(oba_konce_miesiecy('2013-05-30', '2013-06-30'), None)
        self.assertEqual(oba_konce_miesiecy('2013-04-30', '2013-06-30'), None)
