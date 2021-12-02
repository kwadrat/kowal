#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import um_kw


class TxtBook(object):
    def __init__(self, single_file):
        '''
        TxtBook:
        '''
        self.single_file = single_file
        self.datemode = None

    def text_sheet(self):
        '''
        TxtBook:
        '''
        sheet = um_kw.TxtSheet(self.single_file)
        return sheet


class TestTextBook(unittest.TestCase):
    def test_text_book(self):
        '''
        TestTextBook:
        '''
        obk = TxtBook(single_file=None)
        obk.text_sheet()
        self.assertEqual(obk.datemode, None)
