#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Etykiety dla danych poszczególnych faktur'''

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

(
    iy_tfi,
    iy_ntf,
    iy_twb,
    iy_tjl,
    iy_zld,
    iy_bdk,
    ) = range(6)

class TestEtykietRodzajowFaktur(unittest.TestCase):
    def test_etykiet_rodzajow_faktur(self):
        '''
        TestEtykietRodzajowFaktur:
        '''
        self.assertEqual(iy_tfi, 0)
        self.assertEqual(iy_ntf, 1)
        self.assertEqual(iy_twb, 2)
        self.assertEqual(iy_tjl, 3)
        self.assertEqual(iy_zld, 4)
        self.assertEqual(iy_bdk, 5)
