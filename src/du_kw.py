#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


rjb_data_przkl = '2011-12-13 10:41:32'
rjb_dzien_przkl = '2011-12-13'
rjb_godzina_przkl = '10:41:32'
rjb_minuta_przkl = '10:41'


class TestStalychCzasowych(unittest.TestCase):
    def test_stalych_czasowych(self):
        '''
        TestStalychCzasowych:
        '''
        self.assertEqual(rjb_data_przkl, '2011-12-13 10:41:32')
        self.assertEqual(rjb_dzien_przkl, '2011-12-13')
        self.assertEqual(rjb_godzina_przkl, '10:41:32')
        self.assertEqual(rjb_minuta_przkl, '10:41')
