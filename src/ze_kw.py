#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def qh_ttl(tmp_title):
    if tmp_title is None:
        wynik = ''
    else:
        wynik = ' title="%(tmp_title)s"' % dict(tmp_title=tmp_title)
    return wynik

def wstawka_liczba(nazwa, liczba):
    if liczba is None:
        napis = ''
    else:
        napis = ' %s="%d"' % (nazwa, liczba)
    return napis

class TestTytuluHtml(unittest.TestCase):
    def test_tytulu_html(self):
        '''
        TestTytuluHtml:
        '''
        self.assertEqual(qh_ttl('abc'), ' title="abc"')
        self.assertEqual(qh_ttl(None), '')
        self.assertEqual(wstawka_liczba('abc', 7), ' abc="7"')
