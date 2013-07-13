#!/usr/bin/python
# -*- coding: UTF-8 -*-

Moje_przypadki = (
  Klient_mieszany,
  Klient_nasz,
  Klient_obcy,
  Klient_zapomniany,
) = (
  'mieszany',
  'nasz',
  'obcy',
  'nieznany',
)

Sensowne_przypadki = set([Klient_nasz, Klient_obcy])

class NaszaAnkieta(object):
    '''
    Określenie, czy nadlicznik przechowuje dane nasze, czy inne
    '''

    def __init__(self):
        '''
        NaszaAnkieta:
        '''
        self.jestem_bialy = 0 # Liczba linii informujących o poprawnym, naszym kliencie
        self.jestem_czarny = 0 # Liczba linii o obcym kliencie

    def zaznacz_kolor(self, nasz_klient):
        '''
        NaszaAnkieta:
        '''
        if nasz_klient:
            self.jestem_bialy += 1 # Dostaliśmy informację o naszym kliencie
        else:
            self.jestem_czarny += 1 # Dostaliśmy informację o obcym kliencie

    def sprawdz_poprawnosc(self):
        '''
        NaszaAnkieta:
        '''
        if self.jestem_bialy:
            przypadek = Moje_przypadki[:2]
        else:
            przypadek = Moje_przypadki[2:]
        if self.jestem_czarny:
            odpowiedz = przypadek[0]
        else:
            odpowiedz = przypadek[1]
        return odpowiedz
