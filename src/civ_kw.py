#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


xs_1_ql = ' ORDER BY '
xs_2_ql = 'UNION\n'
xs_3_ql = '\n' + xs_2_ql
xs_4_ql = 'UNION ALL\n'
xs_semicolon_ql = ';'
xs_comma_ql = ','
xs_6_ql = ' DESC'

class TestPartsSQL(unittest.TestCase):
    def test_parts_sql(self):
        '''
        TestPartsSQL:
        '''
        self.assertEqual(xs_1_ql, ' ORDER BY ')
        self.assertEqual(xs_2_ql, 'UNION\n')
        self.assertEqual(xs_3_ql, '\nUNION\n')
        self.assertEqual(xs_4_ql, 'UNION ALL\n')
        self.assertEqual(xs_semicolon_ql, ';')
        self.assertEqual(xs_comma_ql, ',')
        self.assertEqual(xs_6_ql, ' DESC')
