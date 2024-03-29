#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ckc_kw
import sn_kw
import uv_kw


def przygotuj_podnajemcow(lista_podnajemcow):
    wykaz_podnajemcow = {}
    for numer_nadlicznika, moj_punkt_poboru, data_pocz, data_kon, dane_osoby in lista_podnajemcow:
        wykaz_podnajemcow[moj_punkt_poboru] = uv_kw.MojPodnajemca(numer_nadlicznika, dane_osoby, data_pocz, data_kon)
    return wykaz_podnajemcow


class DanePodnajemcow(object):
    def __init__(self, lista_podnajemcow):
        '''
        DanePodnajemcow:
        '''
        self.wykaz_podnajemcow = przygotuj_podnajemcow(lista_podnajemcow)
        self.wykaz_nazw_podnajemcow = []
        for klucz, jeden_podnajemca in ckc_kw.iteritems(self.wykaz_podnajemcow):
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
        lista_spinek = list(filter(
            lambda x: x.spinkowe_miejsce in self.wykaz_podnajemcow,
            lista_spinek))
        return lista_spinek

    def usun_klucze_podnajemcow(self, lista_spinek):
        '''
        DanePodnajemcow:
        '''
        lista_spinek = list(filter(
            lambda x: x.spinkowe_miejsce not in self.wykaz_podnajemcow,
            lista_spinek))
        return lista_spinek

    def invoice_for_other(self, numer_nadlicznika, dane_osoby):
        '''
        DanePodnajemcow:
        '''
        for jeden_podnajemca in self.wykaz_podnajemcow.values():
            if jeden_podnajemca.counter_person_matches(numer_nadlicznika, dane_osoby):
                result = 1
                break
        else:
            result = 0
        return result


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
        self.assertEqual(dane_podnajemcow.dla_podnajemcy('OTHER PERSON'), 0)
        lista_spinek = [sn_kw.KonstrukcjaSpinki(('11111-001', '2014-04-11'))]
        self.assertEqual(dane_podnajemcow.pozostaw_klucze_podnajemcow(lista_spinek), [])
        self.assertEqual(dane_podnajemcow.usun_klucze_podnajemcow(lista_spinek), lista_spinek)
        self.assertEqual(dane_podnajemcow.invoice_for_other('19191-919', 'OTHER PERSON'), 0)
        self.assertEqual(dane_podnajemcow.invoice_for_other('00003-001', 'NOWAK ADAM'), 1)
        self.assertEqual(dane_podnajemcow.invoice_for_other('00003-001', 'THE BUILDING'), 0)
