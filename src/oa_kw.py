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

# Każdy dzień będzie jako 2 punkty - wtedy 365 dni w roku
# zmieści się w poziomie na ekranie 1024x768
sk_pelny_obraz = 1250

def poziomo_dla_dni(min_domain, akt, max_domain, min_pixels, max_pixels):
    return int(
        min_pixels
        +
        (akt - min_domain)
        *
        (max_pixels - min_pixels)
        /
        (max_domain - min_domain)
        )

def zaokraglij_mi(all_points, small_part):
    return all_points - (all_points % small_part)

class TestRozmiaruObrazu(unittest.TestCase):
    def test_rozmiaru_obrazu(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(sk_pelny_obraz, 1250)

    def test_szkieletowego_datownika(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(poziomo_dla_dni(1, 4, 4, 0, 3), 3)
        self.assertEqual(poziomo_dla_dni(0, 0, 4, 1, 3), 1)
        self.assertEqual(poziomo_dla_dni(0, 31 + 365 + 31 + 29, 31 + 365 + 31 + 29, 0, sk_pelny_obraz), sk_pelny_obraz)

    def test_szkieletowego_zaokraglenia(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(zaokraglij_mi(96, 96), 96)
        self.assertEqual(zaokraglij_mi(96 + 95, 96), 96)
        self.assertEqual(zaokraglij_mi(96 + 96, 96), 192)
