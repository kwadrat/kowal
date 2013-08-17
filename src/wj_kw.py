#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Nakładka przedziałów czasowych
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import wn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class KlasaNakladki(object):
    def __init__(self):
        '''
        KlasaNakladki:
        '''
        # Słownik nakładek z agregacją faktur (zmienna tymczasowa):
        #   (pocz, kon): [kwota, {lp miejsca: [lista lp faktur]}]
        self.vz_nakladki = {}

    def keys(self):
        '''
        KlasaNakladki:
        '''
        return self.vz_nakladki.keys()

    def jh__getitem__(self, key):
        '''
        KlasaNakladki:
        '''
        return self.vz_nakladki[key]

    def zwroc_odcinek_lub_utworz(self, pk_przedzial):
        '''
        KlasaNakladki:
        '''
        slownik_qm = self.vz_nakladki.get(pk_przedzial)
        if slownik_qm is None:
            slownik_qm = wn_kw.KlasaSlownika()
            self.vz_nakladki[pk_przedzial] = slownik_qm
        return slownik_qm

    def przedzialy_czasowe_dla_nakladek(self):
        '''
        KlasaNakladki:
        '''
        przedzialy = self.vz_nakladki.keys()
        przedzialy.sort()
        for pk_przedzial in przedzialy:
            slownik_qm = self.vz_nakladki[pk_przedzial]
            print pk_przedzial, slownik_qm

class TestKlasyNakladki(unittest.TestCase):
    def test_klasy_nakladki(self):
        '''
        TestKlasyNakladki:
        '''
        obk = KlasaNakladki()
