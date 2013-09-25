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

class TestMiesiacaGazu(unittest.TestCase):
    def test_miesiaca_gazu(self):
        '''
        TestMiesiacaGazu:
        '''
        obk = OgOpDaneDlaMiesiaca()
        self.assertEqual(obk.faktur_w_miesiacu(), 0)
        obk.wstaw_informacje_o_fakturze(None)
        self.assertEqual(obk.faktur_w_miesiacu(), 1)
