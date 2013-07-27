#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import dv_kw
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
formularz_1c_nw_wrsz = '\n'
formularz_1c_zlm_wrsz = '<br />\n'
formularz_1c_kon_formularza = '</form>\n'
hard_space = '&nbsp;'
formularz_1c_kon_dzialu = '</div>\n'
formularz_1c_pocz_pozycji = '<li>'
formularz_1c_kon_pozycji = '</li>\n'
Jedn_zlotowki = 'zł'
naglowek_na_prawo = 'float: right;'

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

formularz_67c_pocz_wiersza = op_tr()

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

def op_select(nzw_sel, brak_idnt=0, class_=None, onchange=None, style=None, to_id=None, multiple=0):
    if to_id is None:
        moje_id = nzw_sel
    else:
        moje_id = to_id
    if brak_idnt:
        kawalek_idnt = ''
    else:
        kawalek_idnt = ' id="%(moje_id)s"' % dict(moje_id = moje_id)
    if class_ is None:
        kawalek_klasy = ''
    else:
        kawalek_klasy = ' class="%(class_)s"' % dict(class_ = class_)
    if onchange is None:
        kawalek_zmiany = ''
    else:
        kawalek_zmiany = ' onchange="%(onchange)s"' % dict(onchange = onchange)
    if style is None:
        kawalek_stylu = ''
    else:
        kawalek_stylu = ' style="%(style)s"' % dict(style = style)
    if multiple:
        kawalek_mltp = ' multiple="multiple"'
    else:
        kawalek_mltp = ''
    return '<select%(kawalek_idnt)s name="%(nzw_sel)s"%(kawalek_klasy)s%(kawalek_mltp)s%(kawalek_stylu)s%(kawalek_zmiany)s>\n' % dict(
        nzw_sel = nzw_sel,
        kawalek_idnt = kawalek_idnt,
        kawalek_klasy = kawalek_klasy,
        kawalek_mltp = kawalek_mltp,
        kawalek_stylu = kawalek_stylu,
        kawalek_zmiany = kawalek_zmiany,
        )

def op_30_sbf(nzw_sel):
    return op_select(nzw_sel=nzw_sel, brak_idnt=1, onchange=fy_kw.lxa_45_inst, class_=fy_kw.lxa_44_inst)

def op_dh(detect_missing_keyword=None, id=None, class_=None):
    if detect_missing_keyword is not None:
        raise RuntimeError('Value without keyword detected: %s' % repr(detect_missing_keyword))
    wstawka_id = wyznacz_wstawke('id', id)
    wstawka_cls = wyznacz_wstawke('class', class_)
    return '<div%(wstawka_id)s%(wstawka_cls)s>\n' % dict(
        wstawka_id=wstawka_id,
        wstawka_cls=wstawka_cls,
        )

def op_li(srodek):
    return ''.join([
        formularz_1c_pocz_pozycji,
        srodek,
        formularz_1c_kon_pozycji,
        ])

def qh_ahtt(wstawka_adresu, tmp_tekst, tmp_title, target=0):
    if target:
        wstawka_tgt = ' target="_blank"'
    else:
        wstawka_tgt = ''
    wstawka_tytulu = qh_ttl(tmp_title)
    return ('<a href="%(wstawka_adresu)s"%(wstawka_tytulu)s%(wstawka_tgt)s>%(tmp_tekst)s</a>' % dict(
        wstawka_adresu=wstawka_adresu,
        wstawka_tytulu=wstawka_tytulu,
        tmp_tekst=tmp_tekst,
        wstawka_tgt=wstawka_tgt,
        ))

def sp_a_stl(style, napis):
    return '<span style="%(style)s">%(napis)s</span>' % dict(
        style=style,
        napis=napis,
        )

def sp_b_stl(napis):
    return '<font size=+1 style="color:red;">%(napis)s</font>' % dict(
        napis=napis,
        )

def sp_stl(liczba_tekstowo, jednostka):
    pieces = []
    pieces.append(formularz_1c_nw_wrsz)
    middle_a = ('(suma narastająco: <font size=+1 style="color:red;">%(liczba_tekstowo)s %(jednostka)s</font>)' %
        dict(
            liczba_tekstowo=liczba_tekstowo,
            jednostka=jednostka,
            ))
    elem = sp_a_stl(naglowek_na_prawo, middle_a)
    pieces.append(elem)
    pieces.append(formularz_1c_zlm_wrsz)
    together = ''.join(pieces)
    return together

def pokoloruj(napis, kolor):
    '''Podkreślenie podanego napisu'''
    middle_a = 'background-color: %(kolor)s;' % dict(
        kolor = kolor,
        )
    polaczony = sp_a_stl(middle_a, napis)
    return polaczony

class TestTytuluHtml(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual
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
        self.assertEqual(formularz_67c_pocz_wiersza, '<tr>\n')
        self.assertEqual(formularz_67c_kon_wiersza, '</tr>\n')
        self.assertEqual(formularz_1c_kon_komorki, '</td>\n')
        self.assertEqual(formularz_1c_kon_slct, '</select>\n')
        self.assertEqual(formularz_1c_kon_formularza, '</form>\n')
        self.assertEqual(formularz_1c_kon_dzialu, '</div>\n')
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
        self.assertEqual(op_select('abc', brak_idnt = 1), '<select name="abc">\n')
        self.assertEqual(op_select('abc'), '<select id="abc" name="abc">\n')
        self.assertEqual(op_select('abc', class_ = 'klasa_css'), '<select id="abc" name="abc" class="klasa_css">\n')
        self.assertEqual(op_select('abc', class_ = 'klasa_css', onchange = 'def'), '<select id="abc" name="abc" class="klasa_css" onchange="def">\n')
        self.assertEqual(op_select('abc', class_ = 'klasa_css', onchange = 'def', style ='ghi'),
            '<select id="abc" name="abc" class="klasa_css" style="ghi" onchange="def">\n')
        self.assertEqual(op_30_sbf('abc'), '<select name="abc" class="selwyborca" onchange="this.form.submit();">\n')
        self.assertEqual(op_dh(id='abc'), '<div id="abc">\n')
        self.assertEqual(op_dh(class_='klasa_css'), '<div class="klasa_css">\n')
        self.assertRaises(RuntimeError, op_dh, 'abc')
        self.assertEqual(op_sel_lgc(False), '')
        self.assertEqual(op_sel_lgc(True), ' selected="selected"')
        self.assertEqual(formularz_1c_pocz_pozycji, '<li>')
        self.assertEqual(formularz_1c_kon_pozycji, '</li>\n')
        self.assertEqual(op_li('abc'), '<li>abc</li>\n')
        self.assertEqual(qh_ahtt('ghi', 'def', 'abc'), '<a href="ghi" title="abc">def</a>')
        self.assertEqual(qh_ahtt('ghi', 'def', 'abc', target=1), '<a href="ghi" title="abc" target="_blank">def</a>')
        self.assertEqual(naglowek_na_prawo, 'float: right;')
        self.assertEqual(sp_a_stl(naglowek_na_prawo, 'napis'), '<span style="float: right;">napis</span>')
        self.assertEqual(
            sp_b_stl('srodek'),
            '<font size=+1 style="color:red;">srodek</font>')
        self.assertEqual(
            sp_stl('12', Jedn_zlotowki),
            '\n<span style="float: right;">(suma narastająco: <font size=+1 style="color:red;">12 zł</font>)</span><br />\n')
        self.assertEqual(Jedn_zlotowki, 'zł')
        self.assertEqual(formularz_1c_zlm_wrsz, '<br />\n')
        self.assertEqual(formularz_1c_nw_wrsz, '\n')
        self.assertEqual(
            pokoloruj('yellow', 'napis'),
            '<span style="background-color: napis;">yellow</span>')
