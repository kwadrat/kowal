#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Import danych sztywnych (ręcznie wpisanych do arkusza), aby
móc ich potem użyć do generowania raportów
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import gu_kw
import la_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def get_name(sheet):
    return sheet.name

def przetworz_arkusz(sheet):
    ark_name = repr(get_name(sheet))
    print ark_name

def generate_stiff_data(filename):
    pass

class TestTheStiffValues(unittest.TestCase):
    def test_stiff_data(self):
        '''
        TestTheStiffValues:
        '''
