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

class MojPodnajemca(object):
    def __init__(self, dane_osoby, data_pocz, data_kon, numer_nadlicznika=None):
        '''
        MojPodnajemca:
        '''
        self.dane_osoby = dane_osoby
        self.data_pocz = data_pocz
        self.data_kon = data_kon
        self.numer_nadlicznika = numer_nadlicznika

    def date_in_range(self, akt_data):
        '''
        MojPodnajemca:
        '''
        result = 0
        if self.data_pocz is None or self.data_pocz <= akt_data:
            if self.data_kon is None or akt_data <= self.data_kon:
                result = 1
        return result

class TestJednegoPodnajemcy(unittest.TestCase):
    def test_jednego_podnajemcy(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca('KOWALSKI JAN', '2014-02-25', None)

    def test_no_time_limits(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca('KOWALSKI JAN', None, None)
        self.assertEqual(obk.date_in_range('2014-02-25'), 1)

    def test_only_begin(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca('KOWALSKI JAN', '2014-02-25', None)
        self.assertEqual(obk.date_in_range('2014-02-24'), 0)
        self.assertEqual(obk.date_in_range('2014-02-25'), 1)

    def test_only_end(self):
        '''
        TestJednegoPodnajemcy:
        '''
        obk = MojPodnajemca('KOWALSKI JAN', None, '2014-02-27')
        self.assertEqual(obk.date_in_range('2014-02-27'), 1)
        self.assertEqual(obk.date_in_range('2014-02-28'), 0)
