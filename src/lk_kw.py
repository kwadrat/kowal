#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

PrawaDostepuPliku = 0777
CHC_NO = 0
CHC_YES = 1
LITERA_SLUPEK = 's'
LITERA_PASEK = 'p'
LITERA_WYKRES = 'w'
KLD_CIEMNY = 0
KLD_JASNY = 1
EtykietaLP = 'L.p.' # Liczba porządkowa
LTR_GLR_STAMP = 'stamp'
LTR_GLR_SMALL = 'small'
CHC_PIC_NON = 0 # to nie zdjęcie
CHC_PIC_ORYG = 1 # oryginał zdjęcia
CHC_PIC_STAMP = 2 # miniaturka zdjęcia
CHC_PIC_SMALL = 3 # zdjęcie standardowe

wyznacz_wielkosc = {
    CHC_PIC_ORYG: lc_kw.fq_oryg_qv,
    CHC_PIC_STAMP: LTR_GLR_STAMP,
    CHC_PIC_SMALL: LTR_GLR_SMALL,
    }

class TestSomeConstants(unittest.TestCase):
    def test_some_constants(self):
        '''
        TestSomeConstants:
        '''
        self.assertEqual(wyznacz_wielkosc[CHC_PIC_ORYG], lc_kw.fq_oryg_qv)
        self.assertEqual(wyznacz_wielkosc[CHC_PIC_STAMP], LTR_GLR_STAMP)
        self.assertEqual(wyznacz_wielkosc[CHC_PIC_SMALL], LTR_GLR_SMALL)
