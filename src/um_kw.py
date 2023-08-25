#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


def normalize_value(before):
    if before == '':
        result = None
    else:
        result = before
    return result


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
            all_rows = file_text.splitlines()
            the_last = all_rows[-1]
            if the_last and the_last.isspace():
                all_rows = all_rows[:-1]
            self.full_matrix = list(map(lambda x: x.split('\t'), all_rows))
        self.nrows = len(self.full_matrix)

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
