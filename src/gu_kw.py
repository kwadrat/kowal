#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Konwerter z adresu kolumny dla miesięcy na współrzędne w arkuszu
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KolumnowyAdresator(object):
    def ustaw_ka_wiersz(self, wiersz_bazowy_miesiecy):
        '''
        KolumnowyAdresator:
        '''
        self.wiersz_bazowy_miesiecy = wiersz_bazowy_miesiecy

    def ustaw_ka_kolumne(self, kl_assigned_col):
        '''
        KolumnowyAdresator:
        '''
        self.kl_assigned_col = kl_assigned_col

    def __init__(self, wiersz_bazowy_miesiecy=None, kl_assigned_col=None):
        '''
        KolumnowyAdresator:
        '''
        self.ustaw_ka_wiersz(wiersz_bazowy_miesiecy)
        self.ustaw_ka_kolumne(kl_assigned_col)

    def get_col_letter(self):
        '''
        KolumnowyAdresator:
        '''
        return fv_kw.vx_zero.vx_rev_lt(self.kl_assigned_col)

class TestKolumnowegoAdresatora(unittest.TestCase):
    def test_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator(wiersz_bazowy_miesiecy=0, kl_assigned_col=4)
        self.assertEqual(obk.wiersz_bazowy_miesiecy, 0)
        self.assertEqual(obk.kl_assigned_col, 4)
        self.assertEqual(obk.get_col_letter(), 'E')

    def test_2_kolumnowy_adresator(self):
        '''
        TestKolumnowegoAdresatora:
        '''
        obk = KolumnowyAdresator()
        obk.ustaw_ka_wiersz(1)
        self.assertEqual(obk.wiersz_bazowy_miesiecy, 1)
        obk.ustaw_ka_kolumne(5)
        self.assertEqual(obk.kl_assigned_col, 5)
        self.assertEqual(obk.get_col_letter(), 'F')
