#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Etykiety dla danych poszczególnych faktur'''

import unittest


(
    iy_tfi,
    iy_ntf,
    iy_twb,
    iy_tjl,
    iy_zld,
    iy_bdk,
    ) = range(6)


class TestEtykietRodzajowFaktur(unittest.TestCase):
    def test_etykiet_rodzajow_faktur(self):
        '''
        TestEtykietRodzajowFaktur:
        '''
        self.assertEqual(iy_tfi, 0)
        self.assertEqual(iy_ntf, 1)
        self.assertEqual(iy_twb, 2)
        self.assertEqual(iy_tjl, 3)
        self.assertEqual(iy_zld, 4)
        self.assertEqual(iy_bdk, 5)
