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

class PseudoBorders(object):
    def __init__(self):
        '''
        PseudoStyle:
        '''
        self.THIN = None

class PseudoStyle(object):
    def __init__(self):
        '''
        PseudoStyle:
        '''
        self.borders = PseudoBorders()

class FenceMaker(object):
    def __init__(self):
        '''
        FenceMaker:
        '''

    def force_borders(self, the_style):
        '''
        FenceMaker:
        '''
        the_borders = the_style.borders
        the_borders.left = the_borders.right = the_borders.top = the_borders.bottom = the_borders.THIN

class TestFenceShape(unittest.TestCase):
    def test_fence_shape(self):
        '''
        TestFenceShape:
        '''
        obk = FenceMaker()
        the_style = PseudoStyle()
        obk.force_borders(the_style)
