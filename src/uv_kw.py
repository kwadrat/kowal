#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


class MojPodnajemca(object):
    def __init__(self, numer_nadlicznika, dane_osoby, data_pocz, data_kon):
        '''
        MojPodnajemca:
        '''
        self.numer_nadlicznika = numer_nadlicznika
        self.dane_osoby = dane_osoby
        self.data_pocz = data_pocz
        self.data_kon = data_kon

    def date_in_range(self, akt_data):
        '''
        MojPodnajemca:
        '''
        result = 0
        if self.data_pocz is None or self.data_pocz <= akt_data:
            if self.data_kon is None or akt_data <= self.data_kon:
                result = 1
        return result

    def counter_person_matches(self, numer_nadlicznika, dane_osoby):
        '''
        MojPodnajemca:
        '''
        if self.numer_nadlicznika == numer_nadlicznika and self.dane_osoby == dane_osoby:
            result = 1
        else:
            result = 0
        return result


class TestJednegoPodnajemcy(unittest.TestCase):
    def test_jednego_podnajemcy(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca(None, 'KOWALSKI JAN', '2014-02-25', None)

    def test_no_time_limits(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca(None, 'KOWALSKI JAN', None, None)
        self.assertEqual(obk.date_in_range('2014-02-25'), 1)

    def test_only_begin(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca(None, 'KOWALSKI JAN', '2014-02-25', None)
        self.assertEqual(obk.date_in_range('2014-02-24'), 0)
        self.assertEqual(obk.date_in_range('2014-02-25'), 1)

    def test_only_end(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca(None, 'KOWALSKI JAN', None, '2014-02-27')
        self.assertEqual(obk.date_in_range('2014-02-27'), 1)
        self.assertEqual(obk.date_in_range('2014-02-28'), 0)

    def test_other_person_invoice(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca('00003-001', 'NOWAK ADAM', None, None)
        self.assertEqual(obk.counter_person_matches('00003-001', 'THE BUILDING'), 0)
        self.assertEqual(obk.counter_person_matches('00003-001', 'NOWAK ADAM'), 1)
        self.assertEqual(obk.counter_person_matches('19191-919', 'NOWAK ADAM'), 0)
