#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Single cell or multi-row/-column rectangle area
'''

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

class MergedCoords(object):
    def __init__(self):
        '''
        MergedCoords:
        '''

    def is_one(self):
        '''
        MergedCoords:
        '''
        return 1

class TestMergedCoords(unittest.TestCase):
    def test_merged_coords(self):
        '''
        TestMergedCoords:
        '''
        obk = MergedCoords()
        self.assertEqual(obk.is_one(), 1)
