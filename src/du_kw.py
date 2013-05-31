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

rjb_data_przkl = '2011-12-13 10:41:32'
rjb_dzien_przkl = '2011-12-13'
rjb_godzina_przkl = '10:41:32'
rjb_minuta_przkl = '10:41'

class TestStalychCzasowych(unittest.TestCase):
    def test_stalych_czasowych(self):
        '''
        TestStalychCzasowych:
        '''
        self.assertEqual(rjb_data_przkl, '2011-12-13 10:41:32')
        self.assertEqual(rjb_dzien_przkl, '2011-12-13')
        self.assertEqual(rjb_godzina_przkl, '10:41:32')
        self.assertEqual(rjb_minuta_przkl, '10:41')
