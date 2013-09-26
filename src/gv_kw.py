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

class RichNumber(object):
    def update_after(self, rn_after):
        '''
        RichNumber:
        '''
        self.rn_after = rn_after

    def update_colour(self, rn_colour):
        '''
        RichNumber:
        '''
        self.rn_colour = rn_colour

    def __init__(self, rn_value, rn_after=2, rn_colour=None):
        '''
        RichNumber:
        '''
        self.rn_value = rn_value
        self.update_after(rn_after)
        self.update_colour(rn_colour)

class TestTheNumber(unittest.TestCase):
    def test_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichNumber(0, rn_after=1, rn_colour='red')
        obk.update_colour('indigo')

    def test_2_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichNumber(1)
        self.assertEqual(obk.rn_after, 2)
        obk.update_after(3)
        self.assertEqual(obk.rn_after, 3)
