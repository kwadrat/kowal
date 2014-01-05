#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

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

class Pseudo_Book(object):
    def __init__(self):
        '''
        Pseudo_Book:
        '''
        self.nsheets = 1
        self.datemode = None

    def sheet_by_name(self, name):
        '''
        Pseudo_Book:
        '''
        return Pseudo_Sheet()

class Pseudo_XLRD(object):
    def __init__(self):
        '''
        Pseudo_XLRD:
        '''

    def open_workbook(self, single_file):
        '''
        Pseudo_XLRD:
        '''
        return Pseudo_Book()

    def xldate_as_tuple(self, value, datemode):
        '''
        Pseudo_XLRD:
        '''
        if len(value) == 3:
            result = value + (0, 0, 0)
        else:
            result = (0, 0, 0) + value + (0,)
        return result

class Pseudo_Sheet(object):
    def __init__(self):
        '''
        Pseudo_Sheet:
        '''
        self.grid = {}

    def cell_value(self, row, col):
        '''
        Pseudo_Sheet:
        '''
        return self.grid[(row, col)]

    def cell_set_value(self, row, col, value):
        '''
        Pseudo_Sheet:
        '''
        self.grid[(row, col)] = value

class Test_XLRD(unittest.TestCase):
    def test_1_xlrd(self):
        '''
        Test_XLRD:
        '''
        xlrd = Pseudo_XLRD()
        value = (1, 2)
        odp = xlrd.xldate_as_tuple(value, None)
        self.assertEqual(odp, (0, 0, 0, 1, 2, 0))

    def test_2_xlrd(self):
        '''
        Test_XLRD:
        '''
        xlrd = Pseudo_XLRD()
        value = (2014, 1, 4)
        odp = xlrd.xldate_as_tuple(value, None)
        self.assertEqual(odp, (2014, 1, 4, 0, 0, 0))
