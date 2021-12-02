#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import us_kw


class KonstrukcjaSpinki(object):
    def __init__(self, moj_klucz):
        '''
        KonstrukcjaSpinki:
        '''
        self.spinkowe_miejsce, self.spinkowa_data = moj_klucz

    def __repr__(self):
        '''
        KonstrukcjaSpinki:
        '''
        return 'SPN(%s,%s)' % (self.spinkowe_miejsce, self.spinkowa_data)

    def __eq__(self, other):
        '''
        KonstrukcjaSpinki:
        '''
        wynik = self.odspinkuj() == other.odspinkuj()
        if us_kw.TymczasowoWizualizacjaZestawuFaktur:
            if 1:
                tmp_format = 'self.odspinkuj()'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
            if 1:
                tmp_format = 'other.odspinkuj()'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
            if 1:
                tmp_format = 'wynik'
                print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
        return wynik

    def __ne__(self, other):
        '''
        KonstrukcjaSpinki:
        '''
        return not (self == other)

    def odspinkuj(self):
        '''
        KonstrukcjaSpinki:
        '''
        return self.spinkowe_miejsce, self.spinkowa_data

    def spinkowe_kiedy(self):
        '''
        KonstrukcjaSpinki:
        '''
        return self.spinkowa_data

    def spinkowe_gdzie(self):
        '''
        KonstrukcjaSpinki:
        '''
        return self.spinkowe_miejsce


class TestSpinki(unittest.TestCase):
    def test_spinki(self):
        '''
        TestSpinki:
        '''
        krotka_a = ('62437-001', '2014-04-28')
        obk_a = KonstrukcjaSpinki(krotka_a)
        self.assertEqual(obk_a.spinkowe_gdzie(), '62437-001')
        self.assertEqual(obk_a.spinkowe_kiedy(), '2014-04-28')
        krotka_b = ('62437-001', '2016-01-09')
        obk_b = KonstrukcjaSpinki(krotka_b)
        obk_c = KonstrukcjaSpinki(krotka_a)
        self.assertEqual(obk_a == obk_b, 0)
        self.assertEqual(obk_a != obk_b, 1)
        self.assertEqual(obk_a == obk_c, 1)
        self.assertEqual(obk_a != obk_c, 0)
