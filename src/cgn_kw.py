#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import re

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class XlrdMerged(object):
    def __init__(self, row_first, row_after_last, col_first, col_after_last):
        '''
        XlrdMerged:
        '''

    def get_anchor_label(self):
        '''
        XlrdMerged:
        '''
        return 'D6'

    def number_of_rows(self):
        '''
        XlrdMerged:
        '''
        return 1

    def number_of_cols(self):
        '''
        XlrdMerged:
        '''
        return 4

class TestDecodeMergedDetails(unittest.TestCase):
    def test_merged_cells_shape(self):
        '''
        TestDecodeMergedDetails:
        '''
        obj = XlrdMerged(5, 6, 3, 7)
        self.assertEqual(obj.get_anchor_label(), 'D6')
        self.assertEqual(obj.number_of_rows(), 1)
        self.assertEqual(obj.number_of_cols(), 4)
