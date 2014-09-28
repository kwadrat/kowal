#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import um_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class TxtBook(object):
    def __init__(self, single_file):
        '''
        TxtBook:
        '''
        self.single_file = single_file
        self.datemode = None

    def text_sheet(self):
        '''
        TxtBook:
        '''
        sheet = um_kw.TxtSheet(self.single_file)
        return sheet

class TestTextBook(unittest.TestCase):
    def test_text_book(self):
        '''
        TestTextBook:
        '''
        obk = TxtBook(single_file=None)
        obk.text_sheet()
        self.assertEqual(obk.datemode, None)
