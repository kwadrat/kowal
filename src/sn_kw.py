#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ust_iw_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KonstrukcjaSpinki(object):
    def __init__(self, moj_klucz):
        '''
        KonstrukcjaSpinki:
        '''
        self.spinkowe_miejsce, self.spinkowa_data = moj_klucz

    def __repr__(self):
        '''
        KonstrukcjaSpinki:
        '''
        return 'SPN(%s,%s)' % (self.spinkowe_miejsce, self.spinkowa_data)

    def __eq__(self, other):
        '''
        KonstrukcjaSpinki:
        '''
        wynik = self.odspinkuj() == other.odspinkuj()
        if ust_iw_kw.TymczasowoWizualizacjaZestawuFaktur:
            tmp_format = 'self.odspinkuj()'; print tmp_format, eval(tmp_format)
            tmp_format = 'other.odspinkuj()'; print tmp_format, eval(tmp_format)
            tmp_format = 'wynik'; print tmp_format, eval(tmp_format)
        return wynik

    def odspinkuj(self):
        '''
        KonstrukcjaSpinki:
        '''
        return self.spinkowe_miejsce, self.spinkowa_data

    def spinkowe_kiedy(self):
        '''
        KonstrukcjaSpinki:
        '''
        return self.spinkowa_data

    def spinkowe_gdzie(self):
        '''
        KonstrukcjaSpinki:
        '''
        return self.spinkowe_miejsce

class TestSpinki(unittest.TestCase):
    def test_spinki(self):
        '''
        TestSpinki:
        '''
        krotka = ('62437-001', '2014-04-28')
        obk = KonstrukcjaSpinki(krotka)
