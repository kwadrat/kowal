#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Remove trailing zeros from float presented in text mode
'''

import unittest
import re

zero_finished = re.compile(r'''
^
(?P<before_point>
\d+
)
\.
0+
$
''', re.VERBOSE)
non_zero_after = re.compile(r'''
^
(?P<with_point>
\d+
\.
\d
\d
)
0+
$
''', re.VERBOSE)


def detach_zeros(one_txt):
    res = zero_finished.search(one_txt)
    if res:
        one_txt = res.group('before_point')
    else:
        res = non_zero_after.search(one_txt)
        if res:
            one_txt = res.group('with_point')
    return one_txt


class TestTrailingZeros(unittest.TestCase):
    def test_trailing_zeros(self):
        '''
        TestTrailingZeros:
        '''
        self.assertEqual(detach_zeros('176.000000'), '176')
        self.assertEqual(detach_zeros('30.000000'), '30')
        self.assertEqual(detach_zeros('X30.000000'), 'X30.000000')
        self.assertEqual(detach_zeros('1851.590000'), '1851.59')
