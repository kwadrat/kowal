#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Nazwa pola: nazwa właściwa, przedrostek
'''

import unittest


AimToObjectFieldName = 0


class FieldDesc(object):
    def __init__(self, fs_core, fs_prefix):
        '''
        FieldDesc:
        '''
        self.fs_core = fs_core
        self.fs_prefix = fs_prefix
        if self.fs_prefix is None:
            self.official_name = self.fs_core
        else:
            self.official_name = self.fs_prefix + self.fs_core


class TestMojegoPola(unittest.TestCase):
    def test_mojego_pola(self):
        '''
        TestMojegoPola:
        '''
        obk = FieldDesc('pole', 'przed_')
        self.assertEqual(obk.fs_core, 'pole')
        self.assertEqual(obk.fs_prefix, 'przed_')
        self.assertEqual(obk.official_name, 'przed_pole')

    def test_bez_przedrostka(self):
        '''
        TestMojegoPola:
        '''
        obk = FieldDesc('proste', None)
        self.assertEqual(obk.fs_core, 'proste')
        self.assertEqual(obk.fs_prefix, None)
        self.assertEqual(obk.official_name, 'proste')
