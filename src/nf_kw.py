#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


(
    BRD_SINGLE,
    BRD_DOUBLE,
    ) = range(2)


class PseudoBorders(object):
    def __init__(self):
        '''
        PseudoBorders:
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


brd_1_obk = FenceMaker()


class TestFenceShape(unittest.TestCase):
    def test_fence_shape(self):
        '''
        TestFenceShape:
        '''
        obk = FenceMaker()
        the_style = PseudoStyle()
        obk.force_borders(the_style)
