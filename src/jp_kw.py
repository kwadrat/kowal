#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lk_kw
import hj_kw
import oc_kw


class KalejdoskopStron(object):
    def __init__(self, numer_strony):
        '''
        KalejdoskopStron:
        '''
        self.rj_sam_rdzen = 'l%d' % numer_strony
        self.rj_py_wersja = oc_kw.dodaj_py(self.rj_sam_rdzen)


rjb_strona_pierwsza = KalejdoskopStron(1)
rjb_strona_druga = KalejdoskopStron(2)
rjb_strona_trzecia = KalejdoskopStron(3)
rjb_strona_czwarta = KalejdoskopStron(4)
rjb_strona_piata = KalejdoskopStron(5)
rjb_strona_szosta = KalejdoskopStron(6)
rjb_strona_siodma = KalejdoskopStron(7)
rjb_strona_osma = KalejdoskopStron(8)
rjb_strona_dziewiata = KalejdoskopStron(9)
rjb_strona_dziesiata = KalejdoskopStron(10)
rjb_strona_jedenasta = KalejdoskopStron(11)
rjb_strona_dwunasta = KalejdoskopStron(12)
rjb_strona_trzynasta = KalejdoskopStron(13)
rjb_strona_czternasta = KalejdoskopStron(14)
rjb_strona_pietnasta = KalejdoskopStron(15)


def fn_adres_post(wersja_produkcyjna):
    return hj_kw.fx_jn(
        lk_kw.rjb_sam_slsh,
        oc_kw.fn_a_in_dwa(wersja_produkcyjna),
        lk_kw.rjb_sam_slsh,
        oc_kw.dodaj_py(rjb_strona_druga.rj_sam_rdzen),
        )


class TestCaleidPages(unittest.TestCase):
    def test_caleid_pages(self):
        '''
        TestCaleidPages:
        '''
        self.assertEqual(fn_adres_post(1), '/inne/l2.py')
        self.assertEqual(fn_adres_post(0), '/inne2/l2.py')
        self.assertEqual(rjb_strona_pierwsza.rj_sam_rdzen, 'l1')
        self.assertEqual(rjb_strona_pierwsza.rj_py_wersja, 'l1.py')
        self.assertEqual(rjb_strona_druga.rj_sam_rdzen, 'l2')
        self.assertEqual(rjb_strona_piata.rj_sam_rdzen, 'l5')
        self.assertEqual(rjb_strona_piata.rj_py_wersja, 'l5.py')
        self.assertEqual(rjb_strona_szosta.rj_sam_rdzen, 'l6')
        self.assertEqual(rjb_strona_szosta.rj_py_wersja, 'l6.py')
        self.assertEqual(rjb_strona_siodma.rj_sam_rdzen, 'l7')
        self.assertEqual(rjb_strona_siodma.rj_py_wersja, 'l7.py')
        self.assertEqual(rjb_strona_osma.rj_sam_rdzen, 'l8')
        self.assertEqual(rjb_strona_osma.rj_py_wersja, 'l8.py')
        self.assertEqual(rjb_strona_dziewiata.rj_sam_rdzen, 'l9')
        self.assertEqual(rjb_strona_dziewiata.rj_py_wersja, 'l9.py')
        self.assertEqual(rjb_strona_dziesiata.rj_sam_rdzen, 'l10')
        self.assertEqual(rjb_strona_dziesiata.rj_py_wersja, 'l10.py')
        self.assertEqual(rjb_strona_jedenasta.rj_sam_rdzen, 'l11')
        self.assertEqual(rjb_strona_jedenasta.rj_py_wersja, 'l11.py')
        self.assertEqual(rjb_strona_dwunasta.rj_sam_rdzen, 'l12')
        self.assertEqual(rjb_strona_dwunasta.rj_py_wersja, 'l12.py')
        self.assertEqual(rjb_strona_trzynasta.rj_sam_rdzen, 'l13')
        self.assertEqual(rjb_strona_trzynasta.rj_py_wersja, 'l13.py')
        self.assertEqual(rjb_strona_czternasta.rj_sam_rdzen, 'l14')
        self.assertEqual(rjb_strona_czternasta.rj_py_wersja, 'l14.py')
        self.assertEqual(rjb_strona_pietnasta.rj_sam_rdzen, 'l15')
        self.assertEqual(rjb_strona_pietnasta.rj_py_wersja, 'l15.py')

    def test_kalejdoskopu_stron(self):
        '''
        TestCaleidPages:
        '''
        obk = KalejdoskopStron(1)
        self.assertEqual(obk.rj_sam_rdzen, 'l1')
        self.assertEqual(obk.rj_py_wersja, 'l1.py')

    def test_2_kalejdoskopu_stron(self):
        '''
        TestCaleidPages:
        '''
        obk = KalejdoskopStron(2)
        self.assertEqual(obk.rj_sam_rdzen, 'l2')
        self.assertEqual(obk.rj_py_wersja, 'l2.py')
