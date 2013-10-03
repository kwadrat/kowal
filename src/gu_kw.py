#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Konwerter z adresu kolumny dla miesięcy na współrzędne w arkuszu
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
import fv_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KolumnowyAdresator(object):
    def ustaw_ka_wiersz(self, wiersz_bazowy_miesiecy):
        '''
        KolumnowyAdresator:
        '''
        self.wiersz_bazowy_miesiecy = wiersz_bazowy_miesiecy

    def ustaw_ka_kolumne(self, kl_assigned_col):
        '''
        KolumnowyAdresator:
        '''
        self.kl_assigned_col = kl_assigned_col

    def __init__(self, wiersz_bazowy_miesiecy=None, kl_assigned_col=None):
        '''
        KolumnowyAdresator:
        '''
        self.ustaw_ka_wiersz(wiersz_bazowy_miesiecy)
        self.ustaw_ka_kolumne(kl_assigned_col)

    def get_col_letter(self):
        '''
        KolumnowyAdresator:
        '''
        return fv_kw.vx_zero.vx_rev_lt(self.kl_assigned_col)

    def set_ka_letter_address(self, the_letters):
        '''
        KolumnowyAdresator:
        '''
        kl_assigned_col = fv_kw.vx_zero.vx_lt(the_letters)
        self.ustaw_ka_kolumne(kl_assigned_col)

    def set_ka_number_address(self, the_number):
        '''
        KolumnowyAdresator:
        '''
        wiersz_bazowy_miesiecy = the_number - 1
        self.ustaw_ka_wiersz(wiersz_bazowy_miesiecy)

    def set_ka_base_address(self, the_label):
        '''
        KolumnowyAdresator:
        '''
        the_letters, the_number = hj_kw.rc_rozszczep(the_label)
        self.set_ka_number_address(the_number)
        self.set_ka_letter_address(the_letters)

    def get_ka_official_address(self, fvk_miesiac=0):
        '''
        KolumnowyAdresator:
        '''
        return self.get_col_letter() + str(self.wiersz_bazowy_miesiecy + fvk_miesiac + 1)

    def set_next_col(self):
        '''
        KolumnowyAdresator:
        '''
        self.kl_assigned_col += 1

    def get_row_col(self):
        '''
        KolumnowyAdresator:
        '''
        return self.wiersz_bazowy_miesiecy, self.kl_assigned_col

    def advance_row_by(self, row_delta=1):
        '''
        KolumnowyAdresator:
        '''
        self.wiersz_bazowy_miesiecy += row_delta

    def advance_col_by(self, col_delta=1):
        '''
        KolumnowyAdresator:
        '''
        self.kl_assigned_col += col_delta

    def create_new_ka_delta(self, row_delta, col_delta):
        '''
        KolumnowyAdresator:
        '''
        return KolumnowyAdresator(
            self.wiersz_bazowy_miesiecy + row_delta,
            self.kl_assigned_col + col_delta)

def generate_every_three(start_label, end_label):
    labels = []
    klm_ads = KolumnowyAdresator()
    klm_ads.set_ka_base_address(end_label)
    the_last_row = klm_ads.wiersz_bazowy_miesiecy
    klm_ads.set_ka_base_address(start_label)
    while klm_ads.wiersz_bazowy_miesiecy <= the_last_row:
        the_label = klm_ads.get_ka_official_address()
        labels.append(the_label)
        klm_ads.advance_row_by(3)
    return labels

class TestKolumnowegoAdresatora(unittest.TestCase):
    def test_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator(wiersz_bazowy_miesiecy=0, kl_assigned_col=4)
        self.assertEqual(obk.wiersz_bazowy_miesiecy, 0)
        self.assertEqual(obk.kl_assigned_col, 4)
        self.assertEqual(obk.get_col_letter(), 'E')

    def test_2_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator()
        obk.ustaw_ka_wiersz(1)
        self.assertEqual(obk.wiersz_bazowy_miesiecy, 1)
        obk.ustaw_ka_kolumne(5)
        self.assertEqual(obk.kl_assigned_col, 5)
        self.assertEqual(obk.get_col_letter(), 'F')

    def test_3_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator()
        obk.ustaw_ka_kolumne(0)
        self.assertEqual(obk.kl_assigned_col, 0)
        obk.ustaw_ka_wiersz(5)
        self.assertEqual(obk.get_ka_official_address(), 'A6')
        self.assertEqual(obk.get_ka_official_address(fvk_miesiac=1), 'A7')
        obk.ustaw_ka_wiersz(1)
        self.assertEqual(obk.get_ka_official_address(), 'A2')
        obk.ustaw_ka_kolumne(26)
        self.assertEqual(obk.kl_assigned_col, 26)
        obk.ustaw_ka_wiersz(1)
        self.assertEqual(obk.get_ka_official_address(), 'AA2')

    def test_3_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator()
        obk.set_ka_base_address('B22')
        self.assertEqual(obk.get_ka_official_address(), 'B22')
        obk.set_ka_base_address('D41')
        self.assertEqual(obk.get_ka_official_address(), 'D41')
        obk.set_ka_letter_address('C')
        self.assertEqual(obk.get_ka_official_address(), 'C41')
        obk.set_ka_number_address(42)
        self.assertEqual(obk.get_ka_official_address(), 'C42')
        obk.set_next_col()
        self.assertEqual(obk.get_ka_official_address(), 'D42')
        self.assertEqual(obk.get_row_col(), (41, 3))
        obk.advance_row_by()
        self.assertEqual(obk.get_ka_official_address(), 'D43')
        obk.advance_row_by(3)
        self.assertEqual(obk.get_ka_official_address(), 'D46')
        self.assertEqual(generate_every_three('B10', 'B16'), ['B10', 'B13', 'B16'])
        self.assertEqual(generate_every_three('B42', 'B51'), ['B42', 'B45', 'B48', 'B51'])
        nowy = obk.create_new_ka_delta(1, 2)
        self.assertEqual(nowy.get_ka_official_address(), 'F47')
        nowy.advance_col_by(6)
        self.assertEqual(nowy.get_ka_official_address(), 'L47')
