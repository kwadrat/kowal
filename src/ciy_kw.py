#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import du_kw


def invariable_time(time_ls, default_value):
    if len(time_ls) > 1 and len(set(time_ls)) == 1:
        result = time_ls[0]
    else:
        result = default_value
    return result


class TestTimeVariability(unittest.TestCase):
    def test_time_variability(self):
        '''
        TestTimeVariability:
        '''
        self.assertEqual(invariable_time([], None), None)
        self.assertEqual(invariable_time(['07:30', '07:30'], None), '07:30')
        self.assertEqual(invariable_time(['08:00', '08:00'], None), '08:00')
        self.assertEqual(invariable_time(['07:30', '08:00'], None), None)
        self.assertEqual(invariable_time(['07:30'], None), None)
        self.assertEqual(invariable_time(['07:30', '07:30', '08:00'], None), None)
        self.assertEqual(invariable_time(['07:30', '08:00'], du_kw.rjb_minuta_przkl), du_kw.rjb_minuta_przkl)
