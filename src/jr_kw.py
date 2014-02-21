#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Koszty jednostkowe energii elektrycznej dla C-21, odczytywane
z arkusza Excel, dla roku 2010, gdzie zmiany taryfy były
z dokładnością do dnia (a nie do miesiąca)
'''

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

class EnergyTable(object):
    def __init__(self):
        '''
        EnergyTable:
        '''
        self.rows = {}

    def set_elem(self, row, col, name):
        '''
        EnergyTable:
        '''
        if row not in self.rows:
            self.rows[row] = {}
        self.rows[row][col] = name

    def show_bag(self):
        '''
        EnergyTable:
        '''
        rnums = self.rows.keys()
        rnums.sort()
        for r_num in rnums:
            r_cols = self.rows[r_num]
            c_nums = r_cols.keys()
            c_nums.sort()
            print ' '.join(map(lambda x: r_cols[x], c_nums))

ManipulateSheet = jv_kw.ManipulateSheet

class EnergyMonthUnitCosts(ManipulateSheet):
    def col_details(self, wiersz, kolumna):
        '''
        EnergyMonthUnitCosts:
        '''
        for i in [2, 3, 4, 5, 7, 8]:
            print self.read_cell(wiersz + i, kolumna)

    def __init__(self, wbk):
        '''
        EnergyMonthUnitCosts:
        '''
        ManipulateSheet.__init__(self)
        self.wbk = wbk
        klm_a_ads = gu_kw.KolumnowyAdresator()
        for self.sheet in self.wbk.sheets()[:17]:
            if 0:
                print self.sheet.name
            klm_a_ads.set_ka_base_address('E8')
            pracuj = 1
            d_col = 0
            while 1:
                wiersz, kolumna = klm_a_ads.get_row_col(col_delta=d_col)
                wartosc_parametru = self.read_cell(wiersz, kolumna)
                if jt_kw.valid_date_format(wartosc_parametru):
                    print wartosc_parametru
                    d_col += 1
                else:
                    break

def generate_unit_2_cost_data(dfb, filename):
    xlrd = la_kw.new_module_for_reading_spreadsheet()
    wbk = xlrd.open_workbook(filename)
    energy_unit_costs = EnergyMonthUnitCosts(wbk)
