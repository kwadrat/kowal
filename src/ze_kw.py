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

def op_td(class_ = None, colspan=None, rowspan=None, title=None):
    if class_:
        kawalek_klasy = ' class="%(class_)s"' % dict(class_ = class_)
    else:
        kawalek_klasy = ''
    if colspan is None:
        kawalek_csp = ''
    else:
        kawalek_csp = ' colspan="%d"' % colspan
    kawalek_rws = wstawka_liczba('rowspan', rowspan)
    wstawka_tytulu = qh_ttl(title)
    return '<td%(kawalek_klasy)s%(kawalek_csp)s%(kawalek_rws)s%(wstawka_tytulu)s>' % dict(
      kawalek_klasy = kawalek_klasy,
      kawalek_csp = kawalek_csp,
      kawalek_rws = kawalek_rws,
      wstawka_tytulu=wstawka_tytulu,
      )

class TestTytuluHtml(unittest.TestCase):
    def test_tytulu_html(self):
        '''
        TestTytuluHtml:
        '''
        self.assertEqual(qh_ttl('abc'), ' title="abc"')
        self.assertEqual(qh_ttl(None), '')
        self.assertEqual(wstawka_liczba('abc', 7), ' abc="7"')
        self.assertEqual(op_td(), '<td>')
        self.assertEqual(op_td(class_ = 'klasa_css'), '<td class="klasa_css">')
        self.assertEqual(op_td(class_ = 'klasa_css', colspan=2, rowspan=3), '<td class="klasa_css" colspan="2" rowspan="3">')
        self.assertEqual(op_td(class_ = 'klasa_css', colspan=2, rowspan=3, title='abc'), '<td class="klasa_css" colspan="2" rowspan="3" title="abc">')
