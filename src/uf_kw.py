#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import sn_kw
import uv_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def przygotuj_podnajemcow(lista_podnajemcow):
    wykaz_podnajemcow = {}
    for numer_nadlicznika, moj_punkt_poboru, data_pocz, data_kon, dane_osoby in lista_podnajemcow:
        wykaz_podnajemcow[moj_punkt_poboru] = uv_kw.MojPodnajemca(dane_osoby, data_pocz, data_kon, numer_nadlicznika)
    return wykaz_podnajemcow

class DanePodnajemcow(object):
    def __init__(self, lista_podnajemcow):
        '''
        DanePodnajemcow:
        '''
        self.wykaz_podnajemcow = przygotuj_podnajemcow(lista_podnajemcow)
        self.wykaz_nazw_podnajemcow = []
        for klucz, jeden_podnajemca in self.wykaz_podnajemcow.iteritems():
            self.wykaz_nazw_podnajemcow.append(jeden_podnajemca.dane_osoby)
        self.wykaz_nazw_podnajemcow = frozenset(self.wykaz_nazw_podnajemcow)

    def oddzielny_podnajemca(self, moj_punkt_poboru):
        '''
        DanePodnajemcow:
        '''
        return moj_punkt_poboru in self.wykaz_podnajemcow

    def dla_podnajemcy(self, dane_osoby):
        '''
        DanePodnajemcow:
        '''
        return dane_osoby in self.wykaz_nazw_podnajemcow

    def pozostaw_klucze_podnajemcow(self, lista_spinek):
        '''
        DanePodnajemcow:
        '''
        lista_spinek = filter(
            lambda x: x.spinkowe_miejsce in self.wykaz_podnajemcow,
            lista_spinek)
        return lista_spinek

lista_testowa_podnajemcow = [
    ('00002-001', '22222-001', '2014-01-01', None, 'BRZĘCZYSZCZYKIEWICZ GRZEGORZ'),
    ('00003-001', '33333-001', '2014-01-01', None, 'NOWAK ADAM'),
    ]

class TestPodnajemcy(unittest.TestCase):
    def test_klasy_podnajemcy(self):
        '''
        TestPodnajemcy:
        '''
        dane_podnajemcow = DanePodnajemcow(lista_testowa_podnajemcow)
        self.assertEqual(dane_podnajemcow.oddzielny_podnajemca('22222-001'), 1)
        self.assertEqual(dane_podnajemcow.oddzielny_podnajemca('10101-909'), 0)
        self.assertEqual(dane_podnajemcow.dla_podnajemcy('NOWAK ADAM'), 1)
        lista_spinek = [sn_kw.KonstrukcjaSpinki(('11111-001', '2014-04-11'))]
        self.assertEqual(dane_podnajemcow.pozostaw_klucze_podnajemcow(lista_spinek), [])
