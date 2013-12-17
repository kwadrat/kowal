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

def elementy_sas(lista, element):
    if len(lista) > 1:
        try:
            pozycja = lista.index(element)
            if pozycja == 0:
                wynik = [None, lista[pozycja + 1]]
            elif pozycja == len(lista) - 1:
                wynik = [lista[pozycja - 1], None]
            else:
                wynik = [lista[pozycja - 1], lista[pozycja + 1]]
        except ValueError:
            wynik = None
    else:
        wynik = None
    return wynik

class TestZnajdowaniaSasiadow(unittest.TestCase):
    def test_znajdowania_sasiadow(self):
        '''
        TestZnajdowaniaSasiadow:
        '''
        self.assertEqual(elementy_sas([680, 647, 618, 570, 569], 647), [680, 618])
        self.assertEqual(elementy_sas([680, 647, 618, 570, 569], 618), [647, 570])
        self.assertEqual(elementy_sas([680, 647, 618, 570, 569], 680), [None, 647])
        self.assertEqual(elementy_sas([680, 647, 618, 570, 569], 569), [570, None])
        self.assertEqual(elementy_sas([680, 647, 618, 570, 569], 123), None)
        self.assertEqual(elementy_sas([647], 647), None)
