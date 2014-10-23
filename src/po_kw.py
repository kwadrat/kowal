#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import us_kw
import li_kw
import ll_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

licznik_inst_slownikow = li_kw.LicznikInstancji('slownik')

ListaLubSlownikOgolnie = ll_kw.ListaLubSlownikOgolnie

class PozycjeOgolne(ListaLubSlownikOgolnie):
    def __init__(self, etykieta, slownik_poczatkowy=None):
        '''
        PozycjeOgolne:
        '''
        ListaLubSlownikOgolnie.__init__(self, licznik_inst_slownikow, etykieta)
        self.poz_slownik = {}
        self.krkt_slownik = {} # Słownik z poprawionymi polami faktur pochodnych (z korektami)
        self.moge_zmieniac_sie = True
        if slownik_poczatkowy != None:
            self.aktualizuj_pary(slownik_poczatkowy)

    def sprawdz_zmienianie(self):
        '''
        PozycjeOgolne:
        '''
        if not self.moge_zmieniac_sie:
            raise RuntimeError("Zmiana niedozwolona")

    def aktualizuj_pary(self, slownik_poczatkowy):
        '''
        PozycjeOgolne:
        '''
        self.sprawdz_zmienianie()
        if type(slownik_poczatkowy) is dict:
            slownik_poprawiony = slownik_poczatkowy
        elif hasattr(slownik_poczatkowy, 'pobierz_pary'):
            slownik_poprawiony = slownik_poczatkowy.pobierz_pary()
        else:
            raise RuntimeError("Nieznany typ obiektu: %s" % repr(type(slownik_poczatkowy)))
        self.poz_slownik.update(slownik_poprawiony)

    def pobierz_pary(self):
        '''
        PozycjeOgolne:
        '''
        return self.poz_slownik

    def posiadam_klucz(self, klucz):
        '''
        PozycjeOgolne:
        '''
        return klucz in self.poz_slownik

    def pobierz_element(self, klucz):
        '''
        PozycjeOgolne:
        '''
        try:
            wartosc = self.poz_slownik[klucz]
        except KeyError:
            print 'Identyfikacja pozycji:', self.wzorzec_repr('awaryjna_ident')
            tmp_format = 'self.poz_slownik'; print tmp_format, eval(tmp_format)
            tmp_format = 'klucz'; print tmp_format, eval(tmp_format)
            raise
        return wartosc

    def pobierz_krkt_element(self, klucz):
        '''
        PozycjeOgolne:
        '''
        if klucz in self.krkt_slownik:
            wartosc = self.krkt_slownik[klucz]
        else:
            wartosc = self.poz_slownik[klucz]
        return wartosc

    def ustaw_element(self, klucz, wartosc):
        '''
        PozycjeOgolne:
        '''
        self.sprawdz_zmienianie()
        self.poz_slownik[klucz] = wartosc

    def ustaw_krkt_element(self, klucz, wartosc):
        '''
        PozycjeOgolne:
        '''
        self.sprawdz_zmienianie()
        self.krkt_slownik[klucz] = wartosc

    def pobierz_gdy_istnieje(self, klucz):
        '''
        PozycjeOgolne:
        '''
        if self.posiadam_klucz(klucz):
            wynik = self.pobierz_element(klucz)
        else:
            wynik = None
        return wynik

    def inkrementuj_element(self, klucz):
        '''
        PozycjeOgolne:
        '''
        self.sprawdz_zmienianie()
        self.poz_slownik[klucz] += 1

    def ustaw_i_zwroc_element(self, klucz, wartosc):
        '''
        PozycjeOgolne:
        '''
        self.sprawdz_zmienianie()
        self.ustaw_element(klucz, wartosc)
        self.poz_slownik[klucz] = wartosc
        return self.pobierz_element(klucz)

    def dla_iteracji(self):
        '''
        PozycjeOgolne:
        Podobne do dla_listy_kluczy, ale ma zwracać coś iterowalnego, dla "for".
        '''
        return self.poz_slownik.keys()

    def zwroc_klucz_wartosc(self):
        '''
        PozycjeOgolne:
        Dla iterowania jednocześnie po kluczach i wartościach
        '''
        return self.poz_slownik.items()

    def dla_listy_kluczy(self):
        '''
        PozycjeOgolne:
        Podobne do dla_iteracji, ale ma zwracać listę, aby dało się ją posortować.
        '''
        return self.poz_slownik.keys()

    def klucze_chronologicznie(self):
        '''
        PozycjeOgolne:
        '''
        klucze_dat = self.dla_listy_kluczy()
        klucze_dat.sort()
        return klucze_dat

    def podaj_dlugosc(self):
        '''
        PozycjeOgolne:
        '''
        return len(self.poz_slownik)

    def zbior_z_kluczy(self):
        '''
        PozycjeOgolne:
        '''
        return set(self.poz_slownik.keys())

    def zablokuj_zmienianie(self):
        '''
        PozycjeOgolne:
        '''
        self.moge_zmieniac_sie = False

    def anihiluj_element(self, klucz):
        '''
        PozycjeOgolne:
        '''
        del self.poz_slownik[klucz]

    def __eq__(self, other):
        '''
        PozycjeOgolne:
        '''
        wynik = self.poz_slownik == other.poz_slownik
        if us_kw.TymczasowoWizualizacjaZestawuFaktur:
            tmp_format = 'self.poz_slownik'; print tmp_format, eval(tmp_format)
            tmp_format = 'other.poz_slownik'; print tmp_format, eval(tmp_format)
            tmp_format = 'wynik'; print tmp_format, eval(tmp_format)
        return wynik

    def przetwarzaj_pozycje(self, poprz_pozycje, wrnt_typowy):
        '''
        PozycjeOgolne:
        '''
        klucze_poprz = poprz_pozycje.zbior_z_kluczy()
        klucze_akt = self.zbior_z_kluczy()
        assert klucze_poprz == klucze_akt
        for klucz in klucze_akt:
            sl_poprz = poprz_pozycje.pobierz_element(klucz)
            sl_akt = self.pobierz_element(klucz)
            sl_akt.przetwarzaj_slownik(sl_poprz, wrnt_typowy)

class TestPozycjiOgolnych(unittest.TestCase):
    def test_pozycji_ogolnych(self):
        '''
        TestPozycjiOgolnych:
        '''
        obk = PozycjeOgolne('abc')
