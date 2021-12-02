#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lc_kw
import hj_kw
import oc_kw
import oa_kw
import mf_kw

link_area_pocz = '''<area shape="rect" coords="%(px)d,%(py)d,%(kx)d,%(ky)d"\n'''
link_area_alt_title = ''' alt="%(tekst)s" title="%(tekst)s"'''
link_area_kon = ''' />\n'''
link_area_alter_this = ''' onMouseOver="%(over)s"\n onMouseOut="%(out)s"\n'''


def zmniejsz_obszar_aktywny_dla_firefox(jestem_msie, slownik):
    if not jestem_msie:
        slownik[oc_kw.fq_kx_qv] -= 1
        slownik[oc_kw.fq_ky_qv] -= 1


def poszerz_pozycje(jestem_msie, pozycja):
    (px, py, kx, ky) = pozycja
    if jestem_msie:
        # MSIE ma tylko wnętrze, poszerzymy trochę koniec X i koniec Y
        kx += 1
        ky += 1
    else:
        # Firefox
        pass
    return (px, py, kx, ky)


def set_src(name, value):
    return "%s.src='%s'" % (name, value)


def set_bg_color(name, value):
    return "%s.bgColor='%s'" % (name, value)


def link_a_mapy(on_real_mouse, slownik, jestem_msie, html_name, moja_nazwa):
    wynik = []
    zmniejsz_obszar_aktywny_dla_firefox(jestem_msie, slownik)
    # Początek i współrzędne obszaru
    wynik.append(link_area_pocz % slownik)
    # Zmiana aktualnego obrazka
    lista_over = []
    lista_out = []
    if oc_kw.fq_nowy_this_qv in slownik:
        lista_over.append(set_src(html_name, oc_kw.core_resolver.pelna_generowana_nazwa(slownik[oc_kw.fq_nowy_this_qv])))
        lista_out.append(set_src(html_name, oc_kw.core_resolver.pelna_generowana_nazwa(moja_nazwa)))
    if oc_kw.EYK_lporz_fktr in slownik:
        moj_nr_faktury = slownik[oc_kw.EYK_lporz_fktr]
        etyk = mf_kw.nazwa_wiersza(moj_nr_faktury)
        lista_over.append(set_bg_color(etyk, oa_kw.HEX_ZIELONY))
        lista_out.append(set_bg_color(etyk, oa_kw.HEX_BIALY))
        if lc_kw.fq_tekst_qv not in slownik:
            slownik[lc_kw.fq_tekst_qv] = 'Faktura: %d' % moj_nr_faktury
    if lista_over or lista_out:
        zmiany = dict(
        over = hj_kw.semicolon_join(lista_over),
        out = hj_kw.semicolon_join(lista_out),
        )
        on_the_mouse = link_area_alter_this % zmiany
        wynik.append(on_the_mouse)
        if oc_kw.EYK_lporz_fktr in slownik:
            on_real_mouse[slownik[oc_kw.EYK_lporz_fktr]] = on_the_mouse
    # Dymek (opcjonalny)
    if lc_kw.fq_tekst_qv in slownik:
        wynik.append(link_area_alt_title % slownik)
    # Zakończenie adresu
    wynik.append(link_area_kon)
    return ''.join(wynik)


class TestLinkuMapy(unittest.TestCase):
    def test_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        self.assertEqual(link_area_pocz, '''<area shape="rect" coords="%(px)d,%(py)d,%(kx)d,%(ky)d"\n''')
        self.assertEqual(link_area_alt_title, ''' alt="%(tekst)s" title="%(tekst)s"''')
        self.assertEqual(link_area_kon, ''' />\n''')
        self.assertEqual(link_area_alter_this, ''' onMouseOver="%(over)s"\n onMouseOut="%(out)s"\n''')

    def test_2_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        slownik = {
            oc_kw.fq_kx_qv: 10,
            oc_kw.fq_ky_qv: 20,
            }
        zmniejsz_obszar_aktywny_dla_firefox(1, slownik)
        self.assertEqual(slownik[oc_kw.fq_kx_qv], 10)
        self.assertEqual(slownik[oc_kw.fq_ky_qv], 20)

    def test_3_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        slownik = {
            oc_kw.fq_kx_qv: 10,
            oc_kw.fq_ky_qv: 20,
            }
        zmniejsz_obszar_aktywny_dla_firefox(0, slownik)
        self.assertEqual(slownik[oc_kw.fq_kx_qv], 9)
        self.assertEqual(slownik[oc_kw.fq_ky_qv], 19)

    def test_4_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        self.assertEqual(poszerz_pozycje(1, (10, 20, 30, 40)), (10, 20, 31, 41))
        self.assertEqual(poszerz_pozycje(0, (10, 20, 30, 40)), (10, 20, 30, 40))
        self.assertEqual(set_src('abc', 'def'), "abc.src='def'")
        self.assertEqual(set_bg_color('abc', 'def'), "abc.bgColor='def'")
