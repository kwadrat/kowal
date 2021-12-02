#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


def dict_ls_key_mapper(the_label, entry_ls):
    return map(lambda the_dict: the_dict[the_label], entry_ls)


class TestExtractingByKey(unittest.TestCase):
    def test_extracting_by_key(self):
        '''
        TestExtractingByKey:
        '''
        self.assertEqual(dict_ls_key_mapper(None, []), [])
        self.assertEqual(dict_ls_key_mapper('a', [{'a': 1}]), [1])
        self.assertEqual(dict_ls_key_mapper('b', [{'b': 1}]), [1])
        self.assertEqual(dict_ls_key_mapper('b', [{'b': 1}, {'b': 2}]), [1, 2])
