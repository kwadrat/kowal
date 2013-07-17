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

class ScaleAdvisor(object):
    def __init__(self):
        '''
        ScaleAdvisor:
        '''

class TestAxisScale(unittest.TestCase):
    def test_axis_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor()
