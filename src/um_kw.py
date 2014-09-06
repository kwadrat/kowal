#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import fv_kw
import le_kw
import lp_kw
import lq_kw
import eo_kw
import tq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def normalize_value(before):
    if before == '':
        result = None
    else:
        result = before
    return result

CommonRdWr = tq_kw.CommonRdWr

class TxtSheet(object):
    def __init__(self, single_file=None):
        '''
        TxtSheet:
        '''
        self.single_file = single_file
        if self.single_file is None:
            self.full_matrix = [[None]]
        else:
            file_text = open(self.single_file, 'rb').read()
            with_first_row = '\n' + file_text
            all_rows = with_first_row.splitlines()
            self.full_matrix = map(lambda x: x.split('\t'), all_rows)

    def cell_value(self, my_row, my_col):
        '''
        TxtSheet:
        '''
        return self.full_matrix[my_row][my_col]

class TestSheetInText(unittest.TestCase):
    def test_sheet_in_text(self):
        '''
        TestSheetInText:
        '''
        obk = TxtSheet()
        obk.cell_value(my_col=0, my_row=0)
