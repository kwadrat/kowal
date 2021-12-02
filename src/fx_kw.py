#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Statystyka poboru w jednym dniu - liczba komórek pustych (None) oraz
o zerowej wartości
'''

import unittest

import lm_kw
import ze_kw

CLL_Background_OK = 'zielone-tlo'
CLL_Background_Problems = 'czerwone-tlo'

class DayCellsStats(object):
    def __init__(self):
        '''
        DayCellsStats:
        '''
        self.empty_cells = 0
        self.zero_cells = 0

    def cell_params(self, empty_cells, zero_cells):
        '''
        DayCellsStats:
        '''
        self.empty_cells = empty_cells
        self.zero_cells = zero_cells

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
        obk.cell_params(1, 0)
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
        obk.cell_params(0, 1)
        self.assertEqual(obk.empty_cells, 0)
        self.assertEqual(obk.zero_cells, 1)
        self.assertEqual(obk.cell_background(), CLL_Background_Problems)
        self.assertEqual(obk.cell_message(), '0/1')
        self.assertEqual(obk.cell_problems(), 1)
