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

class JednoPoleGrzewcze(object):
    def __init__(self, label, label_nr=None, liczba_wierszy=2):
        '''
        JednoPoleGrzewcze:
        '''
        self.label = label
        self.label_nr = label_nr
        self.liczba_wierszy = liczba_wierszy

class TestPolaGrzewczego(unittest.TestCase):
    def test_pola_grzewczego(self):
        '''
        TestPolaGrzewczego:
        '''
        obk = JednoPoleGrzewcze('abc', liczba_wierszy=1)
