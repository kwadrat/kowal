#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Koszty jednostkowe energii elektrycznej dla C-21, odczytywane
z arkusza Excel, dla roku 2010, gdzie zmiany taryfy były
z dokładnością do dnia (a nie do miesiąca)
'''

import unittest

import la_kw


def non_wrapped_lines():
    return '# ' 'v' 'i' 'm' ': nowrap'


def constant_width(max_len):
    return '%-' + str(max_len) + 's'


class EnergyTable(object):
    def init_dict(self):
        '''
        EnergyTable:
        '''
        self.rows = {}

    def __init__(self):
        '''
        EnergyTable:
        '''
        self.init_dict()
        self.ls_lines = []

    def set_elem(self, row, col, name):
        '''
        EnergyTable:
        '''
        if row not in self.rows:
            self.rows[row] = {}
        self.rows[row][col] = name

    def end_object(self):
        '''
        EnergyTable:
        '''
        rnums = list(self.rows.keys())
        rnums.sort()
        for r_num in rnums:
            r_cols = self.rows[r_num]
            c_nums = list(r_cols.keys())
            c_nums.sort()
            elem = ' '.join(map(lambda x: r_cols[x], c_nums))
            self.ls_lines.append(elem)
        self.init_dict()

    def show_summary(self):
        '''
        EnergyTable:
        '''
        max_len = max(map(len, self.ls_lines))
        common_frmt = constant_width(max_len)
        self.ls_lines = list(map(lambda x: common_frmt % x, self.ls_lines))
        self.ls_lines.append(non_wrapped_lines())
        print('\n'.join(self.ls_lines))


def workbook_for_verbose_reading(filename):
    xlrd = la_kw.new_module_for_reading_spreadsheet()
    wbk = xlrd.open_workbook(filename, formatting_info=True)
    return wbk


class TestSkomplikowanegoRoku(unittest.TestCase):
    def test_skomplikowanego_roku(self):
        '''
        TestSkomplikowanegoRoku:
        '''
        self.assertEqual(constant_width(140), '%-140s')
