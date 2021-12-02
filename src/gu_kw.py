#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Konwerter z adresu kolumny dla miesięcy na współrzędne w arkuszu
'''

import unittest

import hj_kw
import fv_kw


def combine_rc(col_label, row_number):
    return '%s%d' % (col_label, row_number)


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

    def __init__(self, wiersz_bazowy_miesiecy=None, kl_assigned_col=None, col_cnt=None, row_cnt=None):
        '''
        KolumnowyAdresator:
        '''
        self.ustaw_ka_wiersz(wiersz_bazowy_miesiecy)
        self.ustaw_ka_kolumne(kl_assigned_col)
        self.col_cnt = col_cnt
        self.row_cnt = row_cnt

    def get_col_letter(self, col_delta=0):
        '''
        KolumnowyAdresator:
        '''
        return fv_kw.vx_zero.vx_rev_lt(self.kl_assigned_col + col_delta)

    def set_ka_letter_address(self, lb_col):
        '''
        KolumnowyAdresator:
        '''
        kl_assigned_col = fv_kw.vx_zero.vx_lt(lb_col)
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
        lb_col, the_number = hj_kw.rc_rozszczep(the_label)
        self.set_ka_number_address(the_number)
        self.set_ka_letter_address(lb_col)

    def get_ka_official_row(self, fvk_miesiac=0):
        '''
        KolumnowyAdresator:
        '''
        return self.wiersz_bazowy_miesiecy + fvk_miesiac + 1

    def get_ka_official_address(self, fvk_miesiac=0, col_delta=0):
        '''
        KolumnowyAdresator:
        '''
        col_label = self.get_col_letter(col_delta=col_delta)
        row_number = self.get_ka_official_row(fvk_miesiac=fvk_miesiac)
        return combine_rc(col_label, row_number)

    def set_next_col(self):
        '''
        KolumnowyAdresator:
        '''
        self.kl_assigned_col += 1

    def get_only_row(self, row_delta=0):
        '''
        KolumnowyAdresator:
        '''
        return self.wiersz_bazowy_miesiecy + row_delta

    def get_row_col(self, row_delta=0, col_delta=0):
        '''
        KolumnowyAdresator:
        '''
        return (
            self.get_only_row(row_delta),
            self.kl_assigned_col + col_delta,
            )

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

    def opposite_col_label(self):
        '''
        KolumnowyAdresator:
        '''
        return self.get_col_letter(col_delta=self.col_cnt - 1)

    def opposite_row_nr(self):
        '''
        KolumnowyAdresator:
        '''
        return self.get_ka_official_row(self.row_cnt) - 1

    def opposite_corner_label(self):
        '''
        KolumnowyAdresator:
        '''
        col_label = self.opposite_col_label()
        row_number = self.opposite_row_nr()
        return combine_rc(col_label, row_number)

    def row_start_end_labels(self, row_offset=0):
        '''
        KolumnowyAdresator:
        '''
        col_a_label = self.get_col_letter()
        col_b_label = self.opposite_col_label()
        row_number = self.get_ka_official_row(fvk_miesiac=row_offset)
        return (
            combine_rc(col_a_label, row_number),
            combine_rc(col_b_label, row_number))

    def col_start_end_labels(self, col_offset=0, moj_pierwszy=None, moj_ostatni=None):
        '''
        KolumnowyAdresator:
        '''
        col_label = self.get_col_letter(col_delta=col_offset)
        if moj_pierwszy is None:
            row_a_number = self.get_ka_official_row()
        else:
            row_a_number = self.get_ka_official_row(moj_pierwszy)
        if moj_ostatni is None:
            row_b_number = self.opposite_row_nr()
        else:
            row_b_number = self.get_ka_official_row(moj_ostatni)
        return (
            combine_rc(col_label, row_a_number),
            combine_rc(col_label, row_b_number))

    def col_iter(self):
        '''
        KolumnowyAdresator:
        '''
        return range(self.col_cnt)

    def row_iter(self, extra=0):
        '''
        KolumnowyAdresator:
        '''
        return range(self.row_cnt + extra)


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
    def test_1_kolumnowy_adresator(self):
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
        self.assertEqual(obk.get_ka_official_address(fvk_miesiac=1, col_delta=1), 'B7')
        obk.ustaw_ka_wiersz(1)
        self.assertEqual(obk.get_ka_official_address(), 'A2')
        obk.ustaw_ka_kolumne(26)
        self.assertEqual(obk.kl_assigned_col, 26)
        obk.ustaw_ka_wiersz(1)
        self.assertEqual(obk.get_ka_official_address(), 'AA2')

    def test_4_kolumnowy_adresator(self):
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
        self.assertEqual(obk.get_only_row(), 41)
        self.assertEqual(obk.get_only_row(row_delta=1), 42)
        self.assertEqual(obk.get_row_col(), (41, 3))
        self.assertEqual(obk.get_row_col(row_delta=1), (42, 3))
        self.assertEqual(obk.get_row_col(row_delta=1, col_delta=2), (42, 5))
        obk.advance_row_by()
        self.assertEqual(obk.get_ka_official_address(), 'D43')
        obk.advance_row_by(3)
        self.assertEqual(obk.get_ka_official_address(), 'D46')
        self.assertEqual(generate_every_three('B10', 'B16'), ['B10', 'B13', 'B16'])
        self.assertEqual(generate_every_three('B42', 'B51'), ['B42', 'B45', 'B48', 'B51'])
        nowy = obk.create_new_ka_delta(1, 2)
        self.assertEqual(nowy.get_ka_official_address(), 'F47')
        nowy.advance_col_by(6)
        self.assertEqual(nowy.get_ka_official_row(), 47)
        self.assertEqual(nowy.get_ka_official_address(), 'L47')

    def test_5_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator(wiersz_bazowy_miesiecy=1, kl_assigned_col=2, col_cnt=96, row_cnt=30)
        self.assertEqual(obk.opposite_col_label(), 'CT')
        self.assertEqual(obk.opposite_row_nr(), 31)
        self.assertEqual(obk.opposite_corner_label(), 'CT31')
        self.assertEqual(obk.row_start_end_labels(), ('C2', 'CT2'))
        self.assertEqual(obk.row_start_end_labels(1), ('C3', 'CT3'))
        self.assertEqual(obk.col_start_end_labels(), ('C2', 'C31'))
        self.assertEqual(obk.col_start_end_labels(1), ('D2', 'D31'))
        self.assertEqual(obk.col_start_end_labels(col_offset=96, moj_pierwszy=2, moj_ostatni=6), ('CU4', 'CU8'))

    def test_6_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        self.assertEqual(combine_rc('X', 7), 'X7')
        obk = KolumnowyAdresator(wiersz_bazowy_miesiecy=40, kl_assigned_col=2, col_cnt=24, row_cnt=31)
        self.assertEqual(obk.opposite_col_label(), 'Z')
        self.assertEqual(obk.opposite_row_nr(), 71)
        self.assertEqual(obk.opposite_corner_label(), 'Z71')

    def test_7_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator(col_cnt=3, row_cnt=4)
        self.assertEqual(map(None, obk.col_iter()), [0, 1, 2])
        self.assertEqual(map(None, obk.row_iter()), [0, 1, 2, 3])
        self.assertEqual(map(None, obk.row_iter(1)), [0, 1, 2, 3, 4])
