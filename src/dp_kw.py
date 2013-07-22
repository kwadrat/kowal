#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Moduł pozwalający wybrać między bazą produkcyjną a bazą rozwojową
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

nazwa_prod = 'media'
nazwa_dev = 'kopia'
if rq_kw.Niebezpieczne_testowa_aplikacja_produkcyjna_baza:
    nazwa_dev = 'media'

def jaka_nazwa_bazy(system_prod_dev):
    if system_prod_dev:
        return nazwa_prod
    else:
        return nazwa_dev

class TestWyboruBazy(unittest.TestCase):
    def test_wyboru_bazy(self):
        '''
        TestWyboruBazy:
        '''
        self.assertEqual(jaka_nazwa_bazy(1), 'media')
        self.assertEqual(jaka_nazwa_bazy(0), 'kopia')
