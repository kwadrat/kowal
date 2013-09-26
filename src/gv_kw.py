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

DocelowoRich = 1
class RichNumber(object):
    def __init__(self, rn_value, rn_after=2, rn_colour=None):
        '''
        RichNumber:
        '''
        self.rn_value = rn_value
        self.rn_after = rn_after
        self.rn_colour = rn_colour

class TestTheNumber(unittest.TestCase):
    def test_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichNumber(0, rn_after=1, rn_colour='red')

    def test_2_the_number(self):
        '''
        TestTheNumber:
        '''
        obk = RichNumber(1)
        self.assertEqual(obk.rn_after, 2)
