#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''Zawiera listę list faktur, zgromadzonych dla różnych obiektów, mediów i liczników'''

# (default: 0) Pozwala na dołączanie nieistotnych (pustych) list faktur
DolaczPusteListy = 0

class WynikoweListy(object):
    '''
    Wynikowe listy faktur
    - self.listy_roznych - lista list faktur różnego pochodzenia
    '''
    def __init__(self):
        '''
        WynikoweListy:
        '''
        self.listy_roznych = []

    def doklej_elem(self, element):
        '''
        WynikoweListy:
        '''
        if DolaczPusteListy or element.liczba_faktur_listy(): # Doklej tylko niepuste listy
            self.listy_roznych.append(element)

    def daj_iter(self):
        '''
        WynikoweListy:
        '''
        return self.listy_roznych

    def daj_enum(self):
        '''
        WynikoweListy:
        '''
        return enumerate(self.listy_roznych)

    def liczba_zgromadzonych_faktur(self):
        '''
        WynikoweListy:
        Zwraca liczbę faktur szeregu - suma poszczególnych długości list faktur
        '''
        return sum(
          map(
            lambda l_l: l_l.liczba_faktur_listy(), self.listy_roznych
          )
        )
