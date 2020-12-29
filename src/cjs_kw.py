#!/usr/bin/env python2
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

yq_1_yq = '%Y.%m.%d_%H.%M.%S'
yq_2_yq = '%Y-%m-%d'
yq_3_yq = '%Y-%m'
yq_4_yq = '%Y-%m-%d %H:%M:%S'
yq_5_yq = '%Y%m%d%H%M%S'
yq_6_yq = '%H:%M'
yq_7_yq = '%H:%M:%S'


class TestTimeFormats(unittest.TestCase):
    def test_time_formats(self):
        '''
        TestTimeFormats:
        '''
        self.assertEqual(yq_1_yq, '%Y.%m.%d_%H.%M.%S')
        self.assertEqual(yq_2_yq, '%Y-%m-%d')
        self.assertEqual(yq_3_yq, '%Y-%m')
        self.assertEqual(yq_4_yq, '%Y-%m-%d %H:%M:%S')
        self.assertEqual(yq_5_yq, '%Y%m%d%H%M%S')
        self.assertEqual(yq_6_yq, '%H:%M')
        self.assertEqual(yq_7_yq, '%H:%M:%S')
