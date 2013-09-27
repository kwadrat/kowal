#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Import danych sztywnych (ręcznie wpisanych do arkusza), aby
móc ich potem użyć do generowania raportów
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

class StiffData(object):
    def __init__(self):
        '''
        StiffData:
        '''

class TestTheStiffValues(unittest.TestCase):
    def test_stiff_data(self):
        '''
        TestTheStiffValues:
        '''
        obk = StiffData()
