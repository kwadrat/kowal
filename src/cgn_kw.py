#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import gu_kw


class XlrdMerged(object):
    def __init__(self, row_first, row_after_last, col_first, col_after_last):
        '''
        XlrdMerged:
        '''
        row_cnt = row_after_last - row_first
        col_cnt = col_after_last - col_first
        self.klm_a_ads = gu_kw.KolumnowyAdresator(col_cnt=col_cnt, row_cnt=row_cnt)
        self.klm_a_ads.ustaw_ka_wiersz(row_first)
        self.klm_a_ads.ustaw_ka_kolumne(col_first)

    def get_anchor_label(self):
        '''
        XlrdMerged:
        '''
        return self.klm_a_ads.get_ka_official_address()

    def number_of_rows(self):
        '''
        XlrdMerged:
        '''
        return self.klm_a_ads.row_cnt

    def number_of_cols(self):
        '''
        XlrdMerged:
        '''
        return self.klm_a_ads.col_cnt


class TestDecodeMergedDetails(unittest.TestCase):
    def test_merged_cells_shape(self):
        '''
        TestDecodeMergedDetails:
        '''
        obj = XlrdMerged(5, 6, 3, 7)
        self.assertEqual(obj.get_anchor_label(), 'D6')
        self.assertEqual(obj.number_of_rows(), 1)
        self.assertEqual(obj.number_of_cols(), 4)

    def test_2_merged_cells_shape(self):
        '''
        TestDecodeMergedDetails:
        '''
        obj = XlrdMerged(3, 10, 1, 3)
        self.assertEqual(obj.get_anchor_label(), 'B4')
        self.assertEqual(obj.number_of_rows(), 7)
        self.assertEqual(obj.number_of_cols(), 2)
