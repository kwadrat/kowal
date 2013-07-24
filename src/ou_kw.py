#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KalejdoskopStron(object):
    def __init__(self, numer_strony):
        '''
        KalejdoskopStron:
        '''
        self.rj_sam_rdzen = 'l%d' % numer_strony
        self.rj_py_wersja = 'l1.py'

class TestKalejdoskopuStron(unittest.TestCase):
    def test_kalejdoskopu_stron(self):
        '''
        TestKalejdoskopuStron:
        '''
        obk = KalejdoskopStron(1)
        self.assertEqual(obk.rj_sam_rdzen, 'l1')
        self.assertEqual(obk.rj_py_wersja, 'l1.py')

    def test_2_kalejdoskopu_stron(self):
        '''
        TestKalejdoskopuStron:
        '''
        obk = KalejdoskopStron(2)
        self.assertEqual(obk.rj_sam_rdzen, 'l2')
