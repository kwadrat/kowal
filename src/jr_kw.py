#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Koszty jednostkowe energii elektrycznej dla C-21, odczytywane
z arkusza Excel, dla roku 2010, gdzie zmiany taryfy były
z dokładnością do dnia (a nie do miesiąca)
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import jv_kw
import gu_kw
import jt_kw
import la_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
        rnums = self.rows.keys()
        rnums.sort()
        for r_num in rnums:
            r_cols = self.rows[r_num]
            c_nums = r_cols.keys()
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
        self.ls_lines = map(lambda x: common_frmt % x, self.ls_lines)
        print '\n'.join(self.ls_lines)

ManipulateSheet = jv_kw.ManipulateSheet

class EnergyMonthUnitCosts(ManipulateSheet):
    def col_details(self, en_tb, d_col, wiersz, kolumna):
        '''
        EnergyMonthUnitCosts:
        '''
        for i in [0, 2, 3, 4, 5, 7, 8]:
            kawalek = '%14s' % self.read_cell(wiersz + i, kolumna)
            en_tb.set_elem(i, d_col, kawalek)

    def __init__(self, wbk):
        '''
        EnergyMonthUnitCosts:
        '''
        ManipulateSheet.__init__(self)
        self.wbk = wbk
        klm_a_ads = gu_kw.KolumnowyAdresator()
        en_tb = EnergyTable()
        for self.sheet in self.wbk.sheets()[:17]:
            en_tb.set_elem(-1, 0, self.sheet.name)
            klm_a_ads.set_ka_base_address('E8')
            pracuj = 1
            d_col = 0
            while 1:
                wiersz, kolumna = klm_a_ads.get_row_col(col_delta=d_col)
                wartosc_parametru = self.read_cell(wiersz, kolumna)
                if jt_kw.valid_date_format(wartosc_parametru):
                    self.col_details(en_tb, d_col, wiersz, kolumna)
                    d_col += 1
                else:
                    break
            en_tb.end_object()
        en_tb.show_summary()

def generate_unit_2_cost_data(dfb, filename):
    xlrd = la_kw.new_module_for_reading_spreadsheet()
    wbk = xlrd.open_workbook(filename)
    energy_unit_costs = EnergyMonthUnitCosts(wbk)

class TestSkomplikowanegoRoku(unittest.TestCase):
    def test_skomplikowanego_roku(self):
        '''
        TestSkomplikowanegoRoku:
        '''
        self.assertEqual(constant_width(140), '%-140s')
