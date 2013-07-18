#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
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

def calculate_scale(full_base, value):
    quotient = float(value) / full_base
    result = divmod(math.log10(quotient), 1)
    return result[0]

class ScaleAdvisor(object):
    def set_value(self, my_value):
        '''
        ScaleAdvisor:
        '''
        self.my_value = my_value

    def limit_tick_periods(self, min_tick_periods):
        '''
        ScaleAdvisor:
        '''
        self.min_tick_periods = min_tick_periods

    def __init__(self, tick_base, my_value):
        '''
        ScaleAdvisor:
        '''
        self.tick_base = tick_base
        self.set_value(my_value)
        self.limit_tick_periods(2)

    def rethink_my_state(self, delta):
        '''
        ScaleAdvisor:
        '''
        my_step = self.tick_base * self.min_tick_periods
        scale_factor = calculate_scale(my_step, self.my_value) - delta
        self.little_step = by_ten(my_step, scale_factor)
        tmp_value = by_ten(self.my_value, - scale_factor)
        total_tick_periods = int(tmp_value / my_step)
        return total_tick_periods

    def get_values(self):
        '''
        ScaleAdvisor:
        '''
        total_tick_periods = self.rethink_my_state(0)
        if total_tick_periods < self.min_tick_periods:
            total_tick_periods = self.rethink_my_state(1)
        return (
            total_tick_periods,
            - total_tick_periods * self.little_step,
            self.little_step,
            )


class TestAxisScale(unittest.TestCase):
    def test_helper_functions(self):
        '''
        TestAxisScale:
        '''
        self.assertEqual(by_ten(21, 0), 21)
        self.assertEqual(by_ten(21, 1), 210)
        self.assertEqual(by_ten(21, -1), 2.1)
        self.assertEqual(calculate_scale(2, 3), 0)
        self.assertEqual(calculate_scale(2, 21), 1)
        self.assertEqual(calculate_scale(10, 3), -1)

    def test_axis_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor(1, 10.5)
        self.assertEqual(obk.my_value, 10.5)
        self.assertEqual(obk.get_values(), (5, -10.0, 2.0))
        obk.set_value(9.5)
        self.assertEqual(obk.get_values(), (4, -8.0, 2.0))

    def test_axis_two_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor(2, 10.5)
        self.assertEqual(obk.get_values(), (2, -8.0, 4.0))

    def test_axis_five_scale(self):
        '''
        TestAxisScale:
        '''
        obk = ScaleAdvisor(5, 10.6)
        self.assertEqual(obk.get_values(), (10, -10.0, 1.0))
        obk.limit_tick_periods(3)
        self.assertEqual(obk.get_values(), (7, -10.5, 1.5))
