#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Statystyka poboru w jednym dniu - liczba komórek pustych (None) oraz
o zerowej wartości
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
import ze_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

CLL_Background_OK = 'zielone-tlo'
CLL_Background_Problems = 'czerwone-tlo'

class DayCellsStats(object):
    def __init__(self):
        '''
        DayCellsStats:
        '''
        self.empty_cells = 0
        self.zero_cells = 0
        self.sum_of_cells = lm_kw.wartosc_zero_globalna

    def analyze_the_cell(self, value_in_cell):
        '''
        DayCellsStats:
        '''
        if value_in_cell is None:
            self.empty_cells += 1
        elif value_in_cell == lm_kw.wartosc_zero_globalna:
            self.zero_cells += 1

    def cell_problems(self):
        '''
        DayCellsStats:
        '''
        return self.empty_cells or self.zero_cells

    def cell_background(self):
        '''
        DayCellsStats:
        '''
        if self.cell_problems():
            return CLL_Background_Problems
        return CLL_Background_OK

    def cell_message(self):
        '''
        DayCellsStats:
        '''
        if self.cell_problems():
            return '%d/%d' % (self.empty_cells, self.zero_cells)
        return ze_kw.hard_space

    def cell_title(self):
        '''
        DayCellsStats:
        '''
        if self.cell_problems():
            return ('brakujących pomiarów: %d, zerowych wartości: %d' %
                (self.empty_cells, self.zero_cells))
        return None


class TestDeficits(unittest.TestCase):
    def test_constants_for_deficits(self):
        '''
        TestDeficits:
        '''
        self.assertEqual(CLL_Background_OK, 'zielone-tlo')
        self.assertEqual(CLL_Background_Problems, 'czerwone-tlo')

    def test_deficits(self):
        '''
        TestDeficits:
        '''
        obk = DayCellsStats()
        self.assertEqual(obk.empty_cells, 0)
        self.assertEqual(obk.zero_cells, 0)
        self.assertEqual(obk.cell_background(), CLL_Background_OK)
        self.assertEqual(obk.cell_problems(), 0)
        self.assertEqual(obk.cell_message(), ze_kw.hard_space)
        self.assertEqual(obk.cell_title(), None)
        obk.analyze_the_cell(None)
        self.assertEqual(obk.empty_cells, 1)
        self.assertEqual(obk.cell_background(), CLL_Background_Problems)
        self.assertEqual(obk.cell_message(), '1/0')
        self.assertEqual(obk.cell_problems(), 1)
        self.assertEqual(obk.cell_title(), 'brakujących pomiarów: 1, zerowych wartości: 0')

    def test_2_deficits(self):
        '''
        TestDeficits:
        '''
        obk = DayCellsStats()
        obk.analyze_the_cell(lm_kw.wartosc_zero_globalna)
        self.assertEqual(obk.empty_cells, 0)
        self.assertEqual(obk.zero_cells, 1)
        self.assertEqual(obk.cell_background(), CLL_Background_Problems)
        self.assertEqual(obk.cell_message(), '0/1')
        self.assertEqual(obk.cell_problems(), 1)

    def test_3_deficits(self):
        '''
        TestDeficits:
        '''
        obk = DayCellsStats()
        self.assertEqual(obk.sum_of_cells, lm_kw.wartosc_zero_globalna)
