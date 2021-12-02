#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import rq_kw

class AxisY(object):
    def __init__(self, MinY, MaxY):
        '''
        AxisY:
        '''
        self.MinY = MinY
        self.MaxY = MaxY

    if rq_kw.Docelowo_psyco_nie_pygresql:
        ##############################################################################
        def wyznacz_gorna_wartosc(self, Wartosc):
            '''
            AxisY:
            '''
            gora_slupka = (Wartosc - self.MinY) / (self.MaxY - self.MinY)
            return gora_slupka
        ##############################################################################
    else:
        ##############################################################################
        def wyznacz_gorna_wartosc(self, Wartosc):
            '''
            AxisY:
            '''
            gora_slupka = float(Wartosc - self.MinY) / float(self.MaxY - self.MinY)
            return gora_slupka
        ##############################################################################

    def zbyt_niski_wykres(self):
        '''
        AxisY:
        '''
        if self.MinY >= self.MaxY: # Omijamy wykresy bez zróżnicowanych danych
            napis = ('Za malo roznicy w skali y, MinY = %(MinY)s, MaxY = %(MaxY)s' %
              dict(
                MinY = str(self.MinY),
                MaxY = str(self.MaxY),
              )
            )
        else:
            napis = None
        return napis

class TestAxisVertical(unittest.TestCase):
    def test_axis_vertical(self):
        '''
        TestAxisVertical:
        '''
        MinY = 10
        MaxY = 110
        obk = AxisY(MinY, MaxY)
        self.assertEqual(obk.MinY, 10)
        self.assertEqual(obk.MaxY, 110)

    def test_funkcji_liczacej(self):
        '''
        TestAxisVertical:
        '''
        self.assertEqual(AxisY(0, 1).wyznacz_gorna_wartosc(1), 1.0)
        self.assertEqual(AxisY(0, 2.0).wyznacz_gorna_wartosc(1), 0.5)
        self.assertEqual(AxisY(1, 5.0).wyznacz_gorna_wartosc(2), 0.25)
        self.assertEqual(
            AxisY(5, 5).zbyt_niski_wykres(),
            'Za malo roznicy w skali y, MinY = 5, MaxY = 5'
            )
        self.assertEqual(AxisY(0, 1).zbyt_niski_wykres(), None)
