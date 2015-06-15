#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def map_document_ident(input_tuple):
    (value,) = input_tuple
    if value == 14061083:
        value = 14025187
    output_tuple = (value,)
    return output_tuple

class TestDocumentIdentMapping(unittest.TestCase):
    def test_document_ident_mapping(self):
        '''
        TestDocumentIdentMapping:
        '''
        self.assertEqual(map_document_ident((1,)), (1,))
        self.assertEqual(map_document_ident((14061083,)), (14025187,))
