#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


def husk_object(fvk_ob_ct):
    (id_obkt, tvk_junction) = fvk_ob_ct
    return id_obkt

class TestHuskingIdentifier(unittest.TestCase):
    def test_husking_identifier(self):
        '''
        TestHuskingIdentifier:
        '''
        self.assertEqual(husk_object(fvk_ob_ct=(1, 2)), 1)
        self.assertEqual(husk_object(fvk_ob_ct=(3, 1)), 3)
