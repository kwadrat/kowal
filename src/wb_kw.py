#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Zbitka przedziałów czasowych
'''

import unittest

import rq_kw
import dn_kw


class KlasaZbitki(object):
    def __init__(self, punkt_pocz, punkt_kon):
        '''
        KlasaZbitki:
        '''
        self.punkt_pocz = punkt_pocz
        self.punkt_kon = punkt_kon
        # Słownik zbitek (faktur o tym samym okresie) dla pasków
        # Zaczynamy od słownika z punktem początkowym, bez faktur
        # i punktem końcowym, bez faktur
        self.vz_zbitki = {
            self.punkt_pocz: [],
            self.punkt_kon: [],
            }

    def pokaz_zbitki(self):
        '''
        KlasaZbitki:
        '''
        if rq_kw.TymczasowoOgrWysw:
            if not rq_kw.TymczasowoPkzZbt:
                return
        print('Zbitka:')
        klucze = list(self.vz_zbitki.keys())
        klucze.sort()
        for klucz in klucze:
            print(dn_kw.NapisDnia(klucz), klucz, self.vz_zbitki[klucz])

    def keys(self):
        '''
        KlasaZbitki:
        '''
        return list(self.vz_zbitki.keys())

    def jh__getitem__(self, key):
        '''
        KlasaZbitki:
        '''
        return self.vz_zbitki[key]

    def dodaj_dla_paska(self, faktura):
        '''
        KlasaZbitki:
        '''
        # Pierwszy dzień okresu faktury i po okresie faktury
        fp, fk = faktura.podaj_klucz()
        # Przytnij czas faktury do rozmiaru szkieletu dat
        if fp < self.punkt_pocz:
            fp = self.punkt_pocz
        if fk > self.punkt_kon:
            fk = self.punkt_kon
        # Chcemy, aby faktura była w przedziale oraz miała przynajmniej
        # jeden dzień (fp < fk)
        if self.punkt_pocz <= fp < fk <= self.punkt_kon:
            # Dni już zaznaczone w słowniku poszczególnych okresów
            klucze = list(self.vz_zbitki.keys())
            # Chcemy, aby dzień początkowy i końcowy faktury był w słowniku
            for klucz in (fp, fk):
                if klucz not in klucze:
                    # Znajdź identyfikator przedziału, który trzeba rozciąć
                    poprz = self.punkt_pocz
                    # Znalezienie największego identyfikatora, który jest mniejszy
                    # od podanego klucza
                    for i in klucze:
                        if poprz < i < klucz:
                            poprz = i
                    # Kopiuj listę faktur do nowego przedziału
                    # Zmieniany jest zestaw kluczy, ale to nieistotne, jak długo
                    # fp jest różne od fk (spełniony powyższy warunek fp < fk)
                    self.vz_zbitki[klucz] = self.vz_zbitki[poprz][:]
            # Uzupełnij wszystkie interesujące nas przedziały o wstawianą fakturę
            # Korzystamy z uaktualnionej listy kluczy
            klucze = filter(lambda x: fp <= x < fk, self.vz_zbitki.keys())
            for klucz in klucze:
                self.vz_zbitki[klucz].append(faktura.lp_faktury)
        else:
            # raise RuntimeError('Faktura?: %s' % repr((fp, fk)))
            pass


class TestKlasyZbitki(unittest.TestCase):
    def test_klasy_zbitki(self):
        '''
        TestKlasyZbitki:
        '''
        obk = KlasaZbitki(15309, 15765)
        self.assertEqual(obk.punkt_pocz, 15309)
