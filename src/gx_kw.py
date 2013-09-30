#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Przydziela wiersze w arkuszu kalkulacyjnym poszczególnym tabelom
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

class Wierszownik(object):
    def __init__(self, wiersz_do_dyspozycji):
        '''
        Wierszownik:
        '''
        self.wiersz_do_dyspozycji = wiersz_do_dyspozycji

    def zabierz_wiersze(self, ile_do_wziecia):
        '''
        Wierszownik:
        '''
        current_value = self.wiersz_do_dyspozycji
        self.wiersz_do_dyspozycji += ile_do_wziecia
        return current_value

class TestPrzydzialuWierszy(unittest.TestCase):
    def test_przydzialu_wierszy(self):
        '''
        TestPrzydzialuWierszy:
        '''
        obk = Wierszownik(20)
        self.assertEqual(obk.wiersz_do_dyspozycji, 20)
        self.assertEqual(obk.zabierz_wiersze(10), 20)
        self.assertEqual(obk.wiersz_do_dyspozycji, 30)
