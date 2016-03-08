#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Obsługa opcjonalnej wartości'''

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

class WartoscOpcjonalna(object):
    def __init__(self, podalem_jednego, wartosc):
        '''
        WartoscOpcjonalna:
        '''
        self.podalem_jednego = podalem_jednego
        self.wartosc = wartosc

    def mt_wybrany(self, id_wybranego):
        '''
        WartoscOpcjonalna:
        '''
        return self.podalem_jednego and id_wybranego == self.wartosc

    def mt_iterowany(self, nr_enum, id_wybranego):
        '''
        WartoscOpcjonalna:
        '''
        if self.podalem_jednego:
            lokalny_warunek = id_wybranego == self.wartosc
        else:
            lokalny_warunek = not nr_enum
        return lokalny_warunek

    def get_opt_value(self):
        '''
        WartoscOpcjonalna:
        '''
        return self.wartosc

class TestWartosciOpcjonalnej(unittest.TestCase):
    def test_wartosci_opcjonalnej(self):
        '''
        TestWartosciOpcjonalnej:
        '''
        obk = WartoscOpcjonalna(0, None)
        self.assertEqual(obk.get_opt_value(), None)

    def test_a_wartosci_opcjonalnej(self):
        '''
        TestWartosciOpcjonalnej:
        '''
        obk = WartoscOpcjonalna(0, 7)
        self.assertEqual(obk.get_opt_value(), 7)
