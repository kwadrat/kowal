#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import re


frag_a = r'''
\s*
'''
frag_b = '''
\s+
numeric
\(
1000,
(?P<decimal_precision>
\d+
)
\)

'''

def extract_precision(one_line, label):
    result = None
    if one_line:
        srch_text = ''.join([
            frag_a,
            label,
            frag_b,
            ])
        reg_res = re.search(srch_text, one_line, re.VERBOSE)
        if reg_res:
            result = reg_res.group('decimal_precision')
            result = int(result)
    return result


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
        after_comma = extract_precision(one_line, self.field_name)
        if after_comma is not None:
            self.set_new_comma(after_comma)

    def analyze_multiline(self, multi_line):
        '''
        DetectAmountFieldPrecision:
        '''
        for one_line in multi_line.splitlines():
            self.analyze_line(one_line)

class TestDetectingAmountFieldPrecision(unittest.TestCase):
    def test_detecting_amount_field_precision(self):
        '''
        TestDetectingAmountFieldPrecision:
        '''
        ojt = DetectAmountFieldPrecision('core')
        self.assertEqual(ojt.field_name, 'core')
        self.assertEqual(ojt.after_comma, None)
        ojt.analyze_line('    core numeric(1000,2),')
        self.assertEqual(ojt.after_comma, 2)
        ojt.analyze_line('')
        self.assertEqual(ojt.after_comma, 2)

    def test_2_detecting_amount_field_precision(self):
        '''
        TestDetectingAmountFieldPrecision:
        '''
        ojt = DetectAmountFieldPrecision('core2')
        ojt.analyze_line('    core2 numeric(1000,4),')
        self.assertEqual(ojt.after_comma, 4)

    def test_3_detecting_amount_field_precision(self):
        '''
        TestDetectingAmountFieldPrecision:
        '''
        ojt = DetectAmountFieldPrecision('core3')
        ojt.set_new_comma(1)
        self.assertEqual(ojt.after_comma, 1)
        self.assertRaises(RuntimeError, ojt.set_new_comma, 2)

    def test_4_detecting_amount_field_precision(self):
        '''
        TestDetectingAmountFieldPrecision:
        '''
        self.assertEqual(extract_precision('', ''), None)
        self.assertEqual(extract_precision('core4 numeric(1000,4),', 'core4'), 4)
        self.assertEqual(extract_precision('core5 numeric(1000,2),', 'core5'), 2)
