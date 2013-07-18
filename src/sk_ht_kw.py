#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Klasa bazowa skrawka HTML
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ze_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def mam_pojedyn_wartosci(lista):
    return type(lista[0]) is str

def ListWyboruOgolna(tgk, nazwa, lista):
    w = []
    if len(lista) > 0:
        w.append(ze_kw.op_30_sbf(nazwa))
        Wybrana = tgk.qparam.get(nazwa, None)
        if mam_pojedyn_wartosci(lista):
            Podwojne = 0
        else:
            Podwojne = 1 # Lista zawiera etykietę oraz tekstowy opis
        for opcja in lista:
            if Podwojne:
                opcja, etykieta = opcja
            else:
                etykieta = opcja

            w.append(ze_kw.op_option(
              etykieta,
              opcja,
              opcja == Wybrana))
        w.append(ze_kw.formularz_1c_kon_slct)
    return ''.join(w)

class Skrawek(object):
    '''Klasa opisująca skrawek formularza:
    wartosc - przechowywana wartość wyboru lub None (nic nie wybrano)
    moje_pole - nazwa interesującego nas pola
    '''

    def __init__(self):
        '''
        Skrawek:
        Na początku nie mamy żadnej wartości
        '''
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
        self.wartosc = tgk.qparam.get(self.moje_pole, None)
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
        napis = '''<input name="%s" type="hidden" value="%s">\n'''
        return napis % (self.moje_pole, self.wartosc)

class TestPodstSkrawka(unittest.TestCase):
    def test_podstawowego_skrawka(self):
        '''
        TestPodstSkrawka:
        '''
        self.assertEqual(mam_pojedyn_wartosci([('a', 'opis A'), ('b', 'opis B')]), 0)
        self.assertEqual(mam_pojedyn_wartosci(('a', 'b')), 1)
