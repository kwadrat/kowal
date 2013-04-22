#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
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

def convert_all(my_values):
    return "'{%s}'" % hj_kw.Poprzecinkuj(map(lm_kw.for_storing, my_values))

class TestConvertingVector(unittest.TestCase):
    def test_converting_vector(self):
        '''
        TestConvertingVector:
        '''
        self.assertEqual(convert_all([None] * 4), "'{NULL,NULL,NULL,NULL}'")
