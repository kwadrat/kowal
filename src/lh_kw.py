#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ze_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

# Sprawdza, że w liście napisów jest co najmniej jeden znak
def mam_znak(lista):
    return filter(None, lista)

class ListaHTML(object):
    '''
    Zbieranie kodu HTML z poszczególnych fragmentów oraz przeplatanie ich separatorem
    '''
    def czysc_wieksze(self):
        '''
        ListaHTML:
        '''
        self.wieksze = []

    def czysc_mniejsze(self):
        '''
        ListaHTML:
        '''
        self.mniejsze = []

    def __init__(self):
        '''
        ListaHTML:
        '''
        self.oddziel_wykresy = ze_kw.formularz_1c_horizontal_rule
        self.czysc_wieksze()
        self.czysc_mniejsze()

    def koniec_segmentu(self):
        '''
        ListaHTML:
        '''
        if mam_znak(self.wieksze) and mam_znak(self.mniejsze):
            # Dodaj separator wykresów
            self.wieksze.append(self.oddziel_wykresy)
        self.wieksze.extend(self.mniejsze)
        self.czysc_mniejsze()

    def polacz_html(self):
        '''
        ListaHTML:
        '''
        if self.mniejsze:
            self.koniec_segmentu()
        wynik = ''.join(self.wieksze)
        self.czysc_wieksze()
        return wynik

    def ddj(self, elem):
        '''
        ListaHTML:
        Działa jak lista.append()
        '''
        self.mniejsze.append(elem)

    def rzsz(self, lista):
        '''
        ListaHTML:
        Działa jak lista.extend()
        '''
        self.mniejsze.extend(lista)

class TestLsH(unittest.TestCase):
    def test_wykonania(self):
        '''
        TestSzLsFkt:
        '''
        self.assertFalse(mam_znak([]))
        self.assertTrue(mam_znak(['a']))
        self.assertFalse(mam_znak(['', '']))
        lst_h = ListaHTML()
        self.assertEqual(lst_h.polacz_html(), '')
        lst_h.ddj('a')
        self.assertEqual(lst_h.polacz_html(), 'a')
        lst_h.ddj('a')
        lst_h.ddj('b')
        self.assertEqual(lst_h.polacz_html(), 'ab')
        lst_h.ddj('a')
        lst_h.koniec_segmentu()
        lst_h.ddj('b')
        lst_h.koniec_segmentu()
        lst_h.ddj('c')
        self.assertEqual(lst_h.polacz_html(), 'a<hr />\nb<hr />\nc')
        lst_h.ddj('a')
        lst_h.koniec_segmentu()
        lst_h.ddj('b')
        self.assertEqual(lst_h.polacz_html(), 'a<hr />\nb')
        lst_h.ddj('a')
        lst_h.koniec_segmentu()
        lst_h.ddj('b')
        lst_h.koniec_segmentu()
        self.assertEqual(lst_h.polacz_html(), 'a<hr />\nb')
        lst_h.ddj('a')
        lst_h.koniec_segmentu()
        lst_h.koniec_segmentu()
        self.assertEqual(lst_h.polacz_html(), 'a')
        lst_h.koniec_segmentu()
        lst_h.ddj('a')
        lst_h.koniec_segmentu()
        self.assertEqual(lst_h.polacz_html(), 'a')
        lst_h.koniec_segmentu()
        lst_h.koniec_segmentu()
        lst_h.ddj('a')
        self.assertEqual(lst_h.polacz_html(), 'a')
        lst_h.koniec_segmentu()
        lst_h.koniec_segmentu()
        lst_h.ddj('')
        self.assertEqual(lst_h.polacz_html(), '')
        lst_h.koniec_segmentu()
        lst_h.ddj('')
        lst_h.koniec_segmentu()
        self.assertEqual(lst_h.polacz_html(), '')
        lst_h.ddj('a')
        lst_h.koniec_segmentu()
        lst_h.ddj('')
        self.assertEqual(lst_h.polacz_html(), 'a')
        lst_h.ddj('')
        lst_h.koniec_segmentu()
        lst_h.ddj('a')
        lst_h.rzsz(['b', 'cd'])
        self.assertEqual(lst_h.polacz_html(), 'abcd')
