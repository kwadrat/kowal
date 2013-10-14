#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Rich (value, digits after comma, colour) numer
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

ECR_indigo = 'indigo'
ECR_red = 'red'
ECR_sea_green = 'sea_green'

class RichCommon(object):
    def update_value(self, rn_value):
        '''
        RichCommon:
        '''
        self.rn_value = rn_value

    def update_colour(self, rn_colour):
        '''
        RichCommon:
        '''
        self.rn_colour = rn_colour

    def update_size(self, rn_size):
        '''
        RichCommon:
        '''
        self.rn_size = rn_size

    def update_centered(self, rn_centered):
        '''
        RichCommon:
        '''
        self.rn_centered = rn_centered

    def __init__(self, rn_value=None, rn_colour=None, rn_size=None, rn_centered=0):
        '''
        RichCommon:
        '''
        self.update_value(rn_value)
        self.update_colour(rn_colour)
        self.update_size(rn_size)
        self.update_centered(rn_centered)

class RichString(RichCommon):
    def __init__(self, rn_value=None, rn_size=None, rn_centered=0):
        '''
        RichString:
        '''
        RichCommon.__init__(self, rn_value, rn_size=rn_size, rn_centered=rn_centered)

class RichNumber(RichCommon):
    def update_after(self, rn_after):
        '''
        RichNumber:
        '''
        self.rn_after = rn_after

    def __init__(self, rn_value, rn_after=2, rn_colour=None, rn_size=None):
        '''
        RichNumber:
        '''
        RichCommon.__init__(self, rn_value, rn_colour=rn_colour, rn_size=rn_size)
        self.update_after(rn_after)

class TestTheNumber(unittest.TestCase):
    def test_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichNumber(0, rn_after=1, rn_colour=ECR_red)
        self.assertEqual(obk.rn_colour, 'red')
        obk.update_colour(ECR_indigo)
        self.assertEqual(obk.rn_colour, 'indigo')

    def test_2_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichNumber(1, rn_size=14)
        self.assertEqual(obk.rn_after, 2)
        obk.update_after(3)
        self.assertEqual(obk.rn_after, 3)
        self.assertEqual(obk.rn_size, 14)

    def test_3_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichCommon(rn_colour=ECR_red)
        self.assertEqual(obk.rn_colour, 'red')

    def test_4_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichString()

    def test_5_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichString('abc')
        self.assertEqual(obk.rn_value, 'abc')

    def test_6_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichString('abc', rn_size=8)
        self.assertEqual(obk.rn_size, 8)
        self.assertEqual(obk.rn_centered, 0)
