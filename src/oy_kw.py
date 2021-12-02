#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ub_kw

index_zero_number = 0
index_zero_text = str(index_zero_number)
index_minus_one_number = -1
index_minus_one_text = str(index_minus_one_number)
WBR_WSZYSTKIE = '-'  # Wybór wszystkich (np. obiektów)
element_wszystkich = [{ub_kw.EYK_klcz: index_zero_number, ub_kw.EYK_wrtsc: WBR_WSZYSTKIE}]
element_surowy_wszystkich = [(index_zero_number, WBR_WSZYSTKIE)]


def rj_wstaw_kreske_jako_pierwsze(lista_i_n, czy_wszystkie):
    if czy_wszystkie:
        lista_i_n = element_wszystkich + lista_i_n
    return lista_i_n


def rj_wstaw_surowa_kreske_jako_pierwsze(lista_i_n, czy_wszystkie):
    if czy_wszystkie:
        lista_i_n = element_surowy_wszystkich + lista_i_n
    return lista_i_n


def rj_adjoin_all_in_one(lista_i_n):
    return lista_i_n + [(index_minus_one_number, 'wszystkie')]


class TestInsertingAll(unittest.TestCase):
    def test_inserting_all(self):
        '''
        TestInsertingAll:
        '''
        self.assertEqual(index_zero_number, 0)
        self.assertEqual(index_zero_text, '0')
        self.assertEqual(index_minus_one_number, -1)
        self.assertEqual(WBR_WSZYSTKIE, '-')
        self.assertEqual(element_wszystkich, [{'kl_zast': 0, 'nz_zast': '-'}])
        self.assertEqual(element_surowy_wszystkich, [(0, '-')])
        self.assertEqual(rj_wstaw_kreske_jako_pierwsze([], 0), [])
        self.assertEqual(rj_wstaw_kreske_jako_pierwsze([], 1), [{'kl_zast': 0, 'nz_zast': '-'}])
        self.assertEqual(rj_wstaw_surowa_kreske_jako_pierwsze([], 0), [])
        self.assertEqual(rj_wstaw_surowa_kreske_jako_pierwsze([], 1), [(0, '-')])
        self.assertEqual(rj_adjoin_all_in_one(['actual']), ['actual', (-1, 'wszystkie')])
