#!/usr/bin/python
# -*- coding: UTF-8 -*-

DocelowoZwiekszLicznikObiektow = 1

class LicznikInstancji:
    def __init__(self, rodzaj):
        '''
        LicznikInstancji:
        '''
        self.rodzaj = rodzaj
        self.mamy_obiektow = 0

    def nowy_licznik(self):
        '''
        LicznikInstancji:
        '''
        wartosc_zwrotna = '%s%s' % (self.rodzaj, self.mamy_obiektow)
        if DocelowoZwiekszLicznikObiektow:
            self.mamy_obiektow += 1
        return wartosc_zwrotna

    def jaki_to_rodzaj(self):
        '''
        LicznikInstancji:
        '''
        return self.rodzaj
