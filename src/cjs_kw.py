#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import unittest


yq_1_yq = '%Y.%m.%d_%H.%M.%S'
yq_3_yq = '%Y-%m'
yq_2_yq = yq_3_yq + '-%d'
yq_5_yq = '%Y%m%d%H%M%S'
yq_6_yq = '%H:%M'
yq_7_yq = yq_6_yq + ':%S'
yq_4_yq = ''.join([
    yq_2_yq,
    ' ',
    yq_7_yq,
    ])


class TestTimeFormats(unittest.TestCase):
    def test_time_formats(self):
        '''
        TestTimeFormats:
        '''
        self.assertEqual(yq_1_yq, '%Y.%m.%d_%H.%M.%S')
        self.assertEqual(yq_3_yq, '%Y-%m')
        self.assertEqual(yq_2_yq, '%Y-%m-%d')
        self.assertEqual(yq_5_yq, '%Y%m%d%H%M%S')
        self.assertEqual(yq_6_yq, '%H:%M')
        self.assertEqual(yq_7_yq, '%H:%M:%S')
        self.assertEqual(yq_4_yq, '%Y-%m-%d %H:%M:%S')
