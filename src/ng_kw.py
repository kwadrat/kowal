#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Etykiety dla styli generowanych plików Excel
'''

import unittest


code_strings = '''
NVB_2_STYLE
NVB_3_STYLE
NVB_5_STYLE
NVB_6_STYLE
NVB_7_STYLE
NVB_8_STYLE
NVB_10_STYLE
NVB_11_STYLE
NVB_12_STYLE
NVB_13_STYLE
NVB_14_STYLE
NVB_15_STYLE
NVB_16_STYLE
NVB_17_STYLE
NVB_18_STYLE
NVB_19_STYLE
'''
for single_name in code_strings.split():
    exec '%(single_name)s = "%(single_name)s"' % dict(
        single_name=single_name,
        )

class TestZnacznikowStylu(unittest.TestCase):
    def test_znacznikow_stylu(self):
        '''
        TestZnacznikowStylu:
        '''
        self.assertEqual(NVB_3_STYLE, 'NVB_3_STYLE')
