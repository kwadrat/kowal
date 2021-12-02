#!/usr/bin/python
# -*- coding: UTF-8 -*-


class ManipulateSheet(object):
    def __init__(self):
        '''
        ManipulateSheet:
        '''

    def read_cell(self, wiersz, kolumna):
        '''
        ManipulateSheet:
        '''
        if kolumna < self.sheet.ncols and wiersz < self.sheet.nrows:
            value = self.sheet.cell(wiersz, kolumna).value
        else:
            value = None
        return value
