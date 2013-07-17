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

def by_ten(value, ten_exponent):
    return value * 10 ** ten_exponent

class ScaleAdvisor(object):
    def __init__(self, tick_base):
        '''
        ScaleAdvisor:
        '''
        self.tick_base = tick_base

    def calculate_tick_periods(self, my_value):
        '''
        ScaleAdvisor:
        '''
        return int(my_value / self.tick_base)

    def set_value(self, my_value):
        '''
        ScaleAdvisor:
        '''
        self.my_value = my_value
        self.last_tick_value = int(self.my_value)
        self.total_tick_periods = self.calculate_tick_periods(self.my_value)

    def limit_tick_periods(self, min_tick_periods):
        '''
        ScaleAdvisor:
        '''
        self.min_tick_periods = min_tick_periods
        self.total_tick_periods = self.calculate_tick_periods(self.my_value * 10)


class TestAxisScale(unittest.TestCase):
    def test_axis_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor(1)
        obk.set_value(10.5)
        self.assertEqual(obk.my_value, 10.5)
        self.assertEqual(obk.last_tick_value, 10.0)
        self.assertEqual(obk.total_tick_periods, 10)
        obk.set_value(9.5)
        self.assertEqual(obk.last_tick_value, 9.0)
        self.assertEqual(obk.total_tick_periods, 9)

    def test_axis_two_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor(2)
        obk.set_value(10.5)
        self.assertEqual(obk.total_tick_periods, 5)

    def test_axis_five_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor(5)
        obk.set_value(10.6)
        self.assertEqual(obk.total_tick_periods, 2)
        obk.limit_tick_periods(3)
        self.assertEqual(obk.total_tick_periods, 21)

    def test_helper_functions(self):
        '''
        TestAxisScale:
        '''
        self.assertEqual(by_ten(21, 0), 21)
        self.assertEqual(by_ten(21, 1), 210)
        self.assertEqual(by_ten(21, -1), 2.1)
