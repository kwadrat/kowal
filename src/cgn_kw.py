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
        TestDecodeMergedDetails:
        '''

    def get_anchor_label(self):
        '''
        TestDecodeMergedDetails:
        '''
        return 'D6'

    def number_of_rows(self):
        '''
        TestDecodeMergedDetails:
        '''
        return 1

class TestDecodeMergedDetails(unittest.TestCase):
    def test_detecting_amount_field_precision(self):
        '''
        TestDecodeMergedDetails:
        '''
        obj = XlrdMerged(5, 6, 3, 7)
        self.assertEqual(obj.get_anchor_label(), 'D6')
        self.assertEqual(obj.number_of_rows(), 1)
