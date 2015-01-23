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

class WaterCanalCorrection(object):
    def __init__(self):
        '''
        WaterCanalCorrection:
        '''

class TestWatCanCor(unittest.TestCase):
    def test_water_canalization_correction(self):
        '''
        TestWatCanCor:
        '''
        obk = WaterCanalCorrection()
