#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def rok_przestepny(rok):
    '''
    Wartość zwracana:
    1 - rok jest przestępny, 0 - rok nie jest przestępny
    '''
    if rok % 4 != 0:
        przestepny = 0
    elif rok % 100 != 0:
        przestepny = 1
    elif rok % 400 != 0:
        przestepny = 0
    else:
        przestepny = 1
    return przestepny

class TestLeapYearDetection(unittest.TestCase):
    def test_leap_year_detection(self):
        '''
        TestLeapYearDetection:
        '''
        self.assertEqual(rok_przestepny(1900), 0)
        self.assertEqual(rok_przestepny(1999), 0)
        self.assertEqual(rok_przestepny(2000), 1)
        self.assertEqual(rok_przestepny(2004), 1)
