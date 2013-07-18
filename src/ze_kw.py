#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

formularz_1c_kon_slct = '</select>\n'
formularz_1c_kon_tabeli = '</table>\n'
formularz_67c_kon_wiersza = '</tr>\n'
formularz_1c_kon_komorki = '</td>\n'
formularz_1c_zlm_wrsz = '<br />\n'
hard_space = '&nbsp;'

def op_sel_lgc(warunek):
    if warunek:
        napis = ' selected="selected"'
    else:
        napis = ''
    return napis

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

def wyznacz_wstawke(nazwa, wartosc):
    if wartosc is None:
        napis = ''
    else:
        napis = ' %s="%s"' % (nazwa, wartosc)
    return napis

def op_option(napis, wartosc=None, zaznaczenie=0, id=None):
    if wartosc is None:
        kod_wart = ''
    else:
        kod_wart = ' value="%s"' % wartosc
    kod_idntf = wyznacz_wstawke('id', id)
    kod_zazn = op_sel_lgc(zaznaczenie)
    return '<option%s%s%s>%s</option>\n' % (kod_wart, kod_zazn, kod_idntf, napis)

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

def op_tr(id=None, nzw_wrsz=None, ukryty=0):
    wstawka_id = wyznacz_wstawke('id', id)
    wstawka_nzw = wyznacz_wstawke('name', nzw_wrsz)
    return '<tr%(wstawka_id)s%(wstawka_nzw)s>\n' % dict(
      wstawka_id = wstawka_id,
      wstawka_nzw = wstawka_nzw)

def op_tbl(cellspacing=None, cellpadding=None, class_=None, border=None):
    wstawka_spc = wstawka_liczba('cellspacing', cellspacing)
    wstawka_pdd = wstawka_liczba('cellpadding', cellpadding)
    wstawka_bdr = wstawka_liczba('border', border)
    wstawka_cls = wyznacz_wstawke('class', class_)
    return '<table%(wstawka_spc)s%(wstawka_pdd)s%(wstawka_cls)s%(wstawka_bdr)s>\n' % dict(
      wstawka_spc=wstawka_spc,
      wstawka_pdd=wstawka_pdd,
      wstawka_cls=wstawka_cls,
      wstawka_bdr=wstawka_bdr,
      )

def op_ptd(srodek, *lista, **slownik):
    return ''.join([
      op_td(*lista, **slownik),
      srodek,
      formularz_1c_kon_komorki,
      ])

def op_32_sbf():
    return op_tbl(class_=fy_kw.lxa_40_inst, border=1)

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
        self.assertEqual(wyznacz_wstawke('e1', None), '')
        self.assertEqual(wyznacz_wstawke('e2', 'napis'), ' e2="napis"')
        self.assertEqual(op_tr(id = 'abc'), '<tr id="abc">\n')
        self.assertEqual(op_tr(id='abc', nzw_wrsz='def'), '<tr id="abc" name="def">\n')
        self.assertEqual(op_tbl(), '<table>\n')
        self.assertEqual(op_tbl(cellspacing=1, cellpadding=0), '<table cellspacing="1" cellpadding="0">\n')
        self.assertEqual(op_tbl(cellspacing=1, cellpadding=2), '<table cellspacing="1" cellpadding="2">\n')
        self.assertEqual(op_tbl(cellspacing=1, cellpadding=1, class_='abc'), '<table cellspacing="1" cellpadding="1" class="abc">\n')
        self.assertEqual(op_tbl(cellspacing=1, cellpadding=2, class_='def'), '<table cellspacing="1" cellpadding="2" class="def">\n')
        self.assertEqual(formularz_1c_kon_tabeli, '</table>\n')
        self.assertEqual(formularz_67c_kon_wiersza, '</tr>\n')
        self.assertEqual(formularz_1c_kon_komorki, '</td>\n')
        self.assertEqual(formularz_1c_kon_slct, '</select>\n')
        self.assertEqual(op_ptd('abc'), '<td>abc</td>\n')
        self.assertEqual(op_ptd('de', class_='klasa', colspan=7), '<td class="klasa" colspan="7">de</td>\n')
        self.assertEqual(op_ptd('fghi', colspan=2), '<td colspan="2">fghi</td>\n')
        self.assertEqual(hard_space, '&nbsp;')
        self.assertEqual(op_32_sbf(), '<table class="tabelkowiec" border="1">\n')
        self.assertEqual(op_option('abc'), '<option>abc</option>\n')
        self.assertEqual(op_option('abc', 'a'), '<option value="a">abc</option>\n')
        self.assertEqual(op_option('abc', 'a', 1), '<option value="a" selected="selected">abc</option>\n')
        self.assertEqual(op_option('abc', 'a', 0), '<option value="a">abc</option>\n')
        self.assertEqual(op_option('abc', 'b', id='identyf'), '<option value="b" id="identyf">abc</option>\n')

    def test_zaznaczania_opcji(self):
        '''
        TestTytuluHtml:
        '''
        self.assertEqual(op_sel_lgc(False), '')
        self.assertEqual(op_sel_lgc(True), ' selected="selected"')
