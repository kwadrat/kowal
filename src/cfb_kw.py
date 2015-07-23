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

class DetectAmountFieldPrecision(object):
    def __init__(self, field_name):
        '''
        DetectAmountFieldPrecision:
        '''
        self.field_name = field_name
        self.after_comma = None

    def analyze_line(self, one_line):
        '''
        DetectAmountFieldPrecision:
        '''
        self.after_comma = 2

class TestDetectingAmountFieldPrecision(unittest.TestCase):
    def test_detecting_amount_field_precision(self):
        '''
        TestDetectingAmountFieldPrecision:
        '''
        ojt = DetectAmountFieldPrecision('core')
        self.assertEqual(ojt.field_name, 'core')
        self.assertEqual(ojt.after_comma, None)
        ojt.analyze_line('    weg_ilosc numeric(1000,2),')
        self.assertEqual(ojt.after_comma, 2)
