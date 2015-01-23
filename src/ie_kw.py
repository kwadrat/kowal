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

class WaterCanalCorrection(object):
    def __init__(self,
            id_oryg,
            id_nowy,
            ile_wody,
            ile_sciekow,
            ):
        '''
        WaterCanalCorrection:
        '''
        self.id_oryg = id_oryg
        self.id_nowy = id_nowy
        self.ile_wody = ile_wody
        self.ile_sciekow = ile_sciekow

    def dokonaj_a_konwersji_pozycji(self, id_pozycji):
        '''
        WaterCanalCorrection:
        '''
        if id_pozycji == self.id_oryg:
            id_pozycji = self.id_nowy
        return id_pozycji

    def water_canal_amount(self, ilosc_tutejszej_wody, ilosc_tutejszych_sciekow):
        '''
        WaterCanalCorrection:
        '''
        exception_exists = (
            ilosc_tutejszej_wody == self.ile_wody and
            ilosc_tutejszych_sciekow == self.ile_sciekow
            )
        return exception_exists

qy_to_1_moj = WaterCanalCorrection(
    ('2012-07-25', '2012-08-01'),
    ('2012-07-03', '2012-08-01'),
    '20.860000',
    '3.42',
    )

qy_to_2_moj = WaterCanalCorrection(
    ('2012-06-29', '2012-06-29'),
    ('2012-06-15', '2012-06-29'),
    '14.592000',
    '1.64',
    )

class TestWatCanCor(unittest.TestCase):
    def test_water_canalization_correction(self):
        '''
        TestWatCanCor:
        '''
        self.assertEqual(qy_to_1_moj.dokonaj_a_konwersji_pozycji(('2012-07-25', '2012-08-01')), ('2012-07-03', '2012-08-01'))
        self.assertEqual(qy_to_2_moj.dokonaj_a_konwersji_pozycji(('2012-06-29', '2012-06-29')), ('2012-06-15', '2012-06-29'))
        self.assertEqual(qy_to_1_moj.water_canal_amount('2', '3'), 0)
        self.assertEqual(qy_to_1_moj.water_canal_amount('20.860000', '3.42'), 1)
