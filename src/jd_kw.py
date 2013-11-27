#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

class DecProxy(object):
    def __init__(self, dec_value):
        '''
        DecProxy:
        '''
        self.dec_value = dec_value
        self.int_value = int(10000 * self.dec_value)

class TestDecType(unittest.TestCase):
    def test_dec_type(self):
        '''
        TestDecType:
        '''
        dec_value = lm_kw.a2d('38.2902')
        obk = DecProxy(dec_value)
        self.assertEqual(obk.int_value, 382902)
