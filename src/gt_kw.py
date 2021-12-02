#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ciw_kw
import lc_kw
import gv_kw
import lm_kw


class OgOpDaneDlaMiesiaca(object):
    def __init__(self):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        self.faktury_w_miesiacu = []
        self.jednorazowe_wartosci = {}
        self.sztywna_wartosc = {}

    def nadpisz_sume_w_miesiacu(self, tmp_key, sztywna_wartosc):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        self.sztywna_wartosc[tmp_key] = sztywna_wartosc

    def wstaw_a_informacje_o_fakturze(self, dane_faktury):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        self.faktury_w_miesiacu.append(dane_faktury)

    def faktur_w_miesiacu(self):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        return len(self.faktury_w_miesiacu)

    def wybierz_ze_slownikow(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        return ciw_kw.dict_ls_key_mapper(tmp_key, self.faktury_w_miesiacu)

    def oblicz_jednorazowo(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = lm_kw.wartosc_zero_z_bazy
        for jedna_faktura in self.faktury_w_miesiacu:
            moja_wartosc = jedna_faktura.get(tmp_key)
            if moja_wartosc is not None:
                moja_suma += float(moja_wartosc)
        return moja_suma

    def oblicz_moc_jednorazowo(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        result_power = lm_kw.wartosc_zero_z_bazy
        for jedna_faktura in self.faktury_w_miesiacu:
            tmp_power = jedna_faktura.get(tmp_key)
            if tmp_power is not None:
                result_power = max(tmp_power, result_power)
        return result_power

    def oblicz_pierwsze_z_brzegu(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        jedna_faktura = self.faktury_w_miesiacu[0]
        moja_wartosc = jedna_faktura.get(tmp_key)
        return moja_wartosc

    def wyznacz_pracowicie_sume_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = self.jednorazowe_wartosci.get(tmp_key)
        if moja_suma is None:
            moja_suma = self.oblicz_jednorazowo(tmp_key)
            self.jednorazowe_wartosci[tmp_key] = moja_suma
        return moja_suma

    def wyznacz_pracowicie_moc_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = self.jednorazowe_wartosci.get(tmp_key)
        if moja_suma is None:
            moja_suma = self.oblicz_moc_jednorazowo(tmp_key)
            self.jednorazowe_wartosci[tmp_key] = moja_suma
        return moja_suma

    def wyznacz_pracowicie_pierwsza_z_brzegu(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = self.jednorazowe_wartosci.get(tmp_key)
        if moja_suma is None:
            moja_suma = self.oblicz_pierwsze_z_brzegu(tmp_key)
            self.jednorazowe_wartosci[tmp_key] = moja_suma
        return moja_suma

    def podano_sztywna_wartosc(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        return tmp_key in self.sztywna_wartosc

    def wyznacz_sume_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        if self.podano_sztywna_wartosc(tmp_key):
            moja_suma = self.sztywna_wartosc[tmp_key]
        else:
            moja_suma = self.wyznacz_pracowicie_sume_faktur(tmp_key)
        return moja_suma

    def wyznacz_moc_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        if self.podano_sztywna_wartosc(tmp_key):
            moja_suma = self.sztywna_wartosc[tmp_key]
        else:
            moja_suma = self.wyznacz_pracowicie_moc_faktur(tmp_key)
        return moja_suma

    def wyznacz_pierwsza_z_brzegu(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        if self.podano_sztywna_wartosc(tmp_key):
            moja_wartosc = self.sztywna_wartosc[tmp_key]
        else:
            moja_wartosc = self.wyznacz_pracowicie_pierwsza_z_brzegu(tmp_key)
        return moja_wartosc

    def wyznacz_rn_sume_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = self.wyznacz_sume_faktur(tmp_key)
        rn_liczba = gv_kw.RichNumber(moja_suma)
        if self.podano_sztywna_wartosc(tmp_key):
            rn_liczba.update_colour(gv_kw.ECR_indigo)
        return rn_liczba

    def wyznacz_rn_moc_faktur(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        moja_suma = self.wyznacz_moc_faktur(tmp_key)
        rn_liczba = gv_kw.RichNumber(moja_suma)
        if self.podano_sztywna_wartosc(tmp_key):
            rn_liczba.update_colour(gv_kw.ECR_indigo)
        return rn_liczba

    def wyznacz_rn_sume_z_przekroczeniem(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        rn_liczba = self.wyznacz_rn_sume_faktur(tmp_key)
        umowna_suma = self.wyznacz_sume_faktur(lc_kw.fq_moc_umowna_qv)
        if rn_liczba.rn_value > umowna_suma:
            rn_liczba.update_colour(gv_kw.ECR_red)
        return rn_liczba

    def wyznacz_rn_moc_z_przekroczeniem(self, tmp_key):
        '''
        OgOpDaneDlaMiesiaca:
        '''
        rn_liczba = self.wyznacz_rn_moc_faktur(tmp_key)
        umowna_suma = self.wyznacz_moc_faktur(lc_kw.fq_moc_umowna_qv)
        if rn_liczba.rn_value > umowna_suma:
            rn_liczba.update_colour(gv_kw.ECR_red)
        return rn_liczba


class TestMiesiacaGazu(unittest.TestCase):
    def test_miesiaca_gazu(self):
        '''
        TestMiesiacaGazu:
        '''
        obk = OgOpDaneDlaMiesiaca()
        self.assertEqual(obk.faktur_w_miesiacu(), 0)
        obk.wstaw_a_informacje_o_fakturze({'a': 1})
        self.assertEqual(obk.faktur_w_miesiacu(), 1)
        self.assertEqual(obk.wybierz_ze_slownikow('a'), [1])
        self.assertEqual(obk.wyznacz_sume_faktur('a'), 1)
        obk.nadpisz_sume_w_miesiacu('a', 5)
        self.assertEqual(obk.wyznacz_sume_faktur('a'), 5)
        self.assertEqual(obk.wyznacz_sume_faktur('b'), 0)

    def test_2_miesiaca_gazu(self):
        '''
        TestMiesiacaGazu:
        '''
        obk = OgOpDaneDlaMiesiaca()
        obk.wstaw_a_informacje_o_fakturze({'a': 1, 'b': 2})
        self.assertEqual(obk.wybierz_ze_slownikow('b'), [2])
