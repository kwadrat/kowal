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
    def set_new_comma(self, after_comma):
        '''
        DetectAmountFieldPrecision:
        '''
        if self.after_comma is None:
            self.after_comma = after_comma
        else:
            raise RuntimeError(
                'Overwrite old value %s with new value %s ?' % (
                repr(self.after_comma),
                repr(after_comma)))

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

    def test_3_detecting_amount_field_precision(self):
        '''
        TestDetectingAmountFieldPrecision:
        '''
        ojt = DetectAmountFieldPrecision('core3')
        ojt.set_new_comma(1)
        self.assertEqual(ojt.after_comma, 1)
        self.assertRaises(RuntimeError, ojt.set_new_comma, 2)
