#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Klasa bazowa skrawka HTML
'''

import unittest

import uz_kw
import ib_kw
import ze_kw


class Skrawek(object):
    '''Klasa opisująca skrawek formularza
    '''

    def __init__(self, fs_prefix=None):
        '''
        Skrawek:
        '''
        self.fs_prefix = fs_prefix
        self.wartosc = None
        self.wyzeruj_nowy_skr()

    def wyzeruj_nowy_skr(self):
        '''
        Skrawek:
        '''
        self.skh_okres(None)
        self.skh_prez(None)

    def skh_okres(self, prm_okres):
        '''
        Skrawek:
        '''
        self.prm_okres = prm_okres

    def skh_prez(self, elem_prez):
        '''
        Skrawek:
        '''
        self.elem_prez = elem_prez

    def skh_grupa(self, prm_grupa):
        '''
        Skrawek:
        '''
        self.prm_grupa = prm_grupa

    def analiza_parametrow(self, tgk, dfb):
        '''
        Skrawek:
        Przyjmujemy:
        - None, gdy nie ma wartości w słowniku
        - konkretną wartość, jeśli ona jest w słowniku
        Wartość zwrotna:
        - True - poprawnie pobrano wszystkie dane z formularza
        - False - nie znaleźliśmy danych w formularzu, nie
        można go w całości poprawnie przeanalizować
        '''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            self.wartosc = tgk.qparam.get(self.moje_pole, None)
            ##############################################################################
        else:
            ##############################################################################
            self.wartosc = tgk.qparam.get(self.moje_pole, None)
            ##############################################################################
        return self.wartosc != None

    def pobierz_wartosc(self, tgk):
        '''
        Skrawek:
        '''
        return self.wartosc

    def wartosc_ukryta(self):
        '''
        Skrawek:
        '''
        napis = '''<input name="%s" type="%s" value="%s">\n'''
        if ib_kw.AimToObjectFieldName:
            ##############################################################################
            return napis % (self.moje_pole, ze_kw.frm_hdn_pst, self.wartosc)
            ##############################################################################
        else:
            ##############################################################################
            return napis % (self.moje_pole, ze_kw.frm_hdn_pst, self.wartosc)
            ##############################################################################


class TestPrzeniesSkrawka(unittest.TestCase):
    def test_przeniesionego_skrawka(self):
        '''
        TestPrzeniesSkrawka:
        '''
        obk = Skrawek()
        obk.moje_pole = '4dSAQztTX'
        obk.wartosc = 'g8zLn'
        self.assertEqual(obk.wartosc_ukryta(), uz_kw.wzor_167_inst)
