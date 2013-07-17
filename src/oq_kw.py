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
        self.last_tick_value = 10

    def set_value(self, my_value):
        '''
        ScaleAdvisor:
        '''
        self.my_value = my_value
        self.last_tick_value = int(self.my_value)

class TestAxisScale(unittest.TestCase):
    def test_axis_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor()
        obk.set_value(10.5)
        self.assertEqual(obk.my_value, 10.5)
        self.assertEqual(obk.last_tick_value, 10.0)
        obk.set_value(9.5)
        self.assertEqual(obk.last_tick_value, 9.0)
