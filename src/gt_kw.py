#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Raport opłat stałych, zmiennych za gaz W-5
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class OgOpDaneDlaMiesiaca(object):
    def __init__(self):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        self.faktury_w_miesiacu = []
        self.jednorazowe_wartosci = {}

    def wstaw_informacje_o_fakturze(self, dane_faktury):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        self.faktury_w_miesiacu.append(dane_faktury)

    def faktur_w_miesiacu(self):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        return len(self.faktury_w_miesiacu)

    def wybierz_ze_slownikow(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        return map(lambda the_dict: the_dict[tmp_key], self.faktury_w_miesiacu)

    def oblicz_jednorazowo(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = lm_kw.wartosc_zero_z_bazy
        for jedna_faktura in self.faktury_w_miesiacu:
            moja_wartosc = jedna_faktura.get(tmp_key)
            if moja_wartosc is not None:
                moja_suma += moja_wartosc
        return moja_suma

    def wyznacz_sume_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = self.jednorazowe_wartosci.get(tmp_key)
        if moja_suma is None:
            moja_suma = self.oblicz_jednorazowo(tmp_key)
            self.jednorazowe_wartosci[tmp_key] = moja_suma
        return moja_suma

class TestMiesiacaGazu(unittest.TestCase):
    def test_miesiaca_gazu(self):
        '''
        TestMiesiacaGazu:
        '''
        obk = OgOpDaneDlaMiesiaca()
        self.assertEqual(obk.faktur_w_miesiacu(), 0)
        obk.wstaw_informacje_o_fakturze({'a': 1})
        self.assertEqual(obk.faktur_w_miesiacu(), 1)
        self.assertEqual(obk.wybierz_ze_slownikow('a'), [1])
        self.assertEqual(obk.wyznacz_sume_faktur('a'), 1)

    def test_2_miesiaca_gazu(self):
        '''
        TestMiesiacaGazu:
        '''
        obk = OgOpDaneDlaMiesiaca()
        obk.wstaw_informacje_o_fakturze({'a': 1, 'b': 2})
        self.assertEqual(obk.wybierz_ze_slownikow('b'), [2])
