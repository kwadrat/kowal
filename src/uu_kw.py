#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


def vx_wiersze(pocz, kon, krok=1):
    return list(xrange(pocz, kon + 1, krok))


class TestZakresuOdDo(unittest.TestCase):
    def test_zakresu_od_do(self):
        '''
        TestZakresuOdDo:
        '''
        self.assertEqual(vx_wiersze(2, 4), [2,3,4])
        self.assertEqual(vx_wiersze(2, 8, 2), [2,4,6,8])
