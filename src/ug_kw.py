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

delimiter = ';'
quotechar = '"'
PodwZnkSepTekstu = quotechar + quotechar
znaki_konczace_pole_tekstowe = set([delimiter, chr(13), chr(10)])

class FieldSplitter(object):
    def __init__(self):
        '''
        FieldSplitter:
        '''

    def split_fields(self, line):
        '''
        FieldSplitter:
        '''
        return line.split(delimiter)

def rozbij_na_pola(line, quoting=0):
    t = []
    w_cudzyslowie = 0
    wsk = 0 # Wskaźnik na aktualny analizowany znak linii
    DlLinii = len(line) # Długość linii
    first_char = 1 # Znacznik - analizujemy pierwszy znak pola wiersza
    pracuj = 1
    while pracuj:
        if first_char:
            first_char = 0
            if quoting and wsk < DlLinii and line[wsk] == quotechar:
                w_cudzyslowie = 1
                wsk += 1 # Pomiń cudzysłów
            else:
                w_cudzyslowie = 0
            pocz = wsk # To jest pierwszy znak pola do zapamiętania
        if w_cudzyslowie:
            # Szukamy zamykającego cudzysłowu
            if wsk >= DlLinii:
                raise RuntimeError, "Wychodzimy poza linię o treści:\n" + line
            elif quoting and line[wsk] == quotechar:
                if wsk + 1 < DlLinii and line[wsk + 1] == quotechar: # Pominiemy, jeśli cudzysłów jest podwójny
                    wsk += 2
                else:
                    # Pojedynczy cudzysłów - koniec napisu
                    t.append(line[pocz:wsk].replace(PodwZnkSepTekstu, quotechar))
                    wsk += 1
                    # Tu czekamy na przecinek
                    if wsk < DlLinii and line[wsk] == delimiter:
                        wsk += 1
                        first_char = 1 # Znowu zaczynamy analizę od pierwszego znaku pola
                    else:
                        # Nie było przecinka - koniec analizy
                        pracuj = 0
            else:
                wsk += 1 # Szukamy następnego znaku
        else: # Nie mamy cudzysłowu - szukamy do następnego przecinka lub końca
            if wsk >= DlLinii or line[wsk] in znaki_konczace_pole_tekstowe:
                t.append(line[pocz:wsk])
                if wsk < DlLinii and line[wsk] == delimiter:
                    wsk += 1 # Będzie kolejne pole
                    first_char = 1
                else:
                    pracuj = 0 # Koniec analizy - był Enter
            else: # Zwykły znak - przesuwamy się dalej
                wsk += 1
    return t

class TestRozbijaniaCSV(unittest.TestCase):
    def test_rozbijania_csv(self):
        '''
        TestRozbijaniaCSV:
        '''
        self.assertEqual(rozbij_na_pola(''), [''])
        self.assertEqual(rozbij_na_pola('a'), ['a'])
        self.assertEqual(rozbij_na_pola('a;b'), ['a', 'b'])
        self.assertEqual(rozbij_na_pola('"a"'), ['"a"'])

    def test_object_csv(self):
        '''
        TestRozbijaniaCSV:
        '''
        obk = FieldSplitter()
        self.assertEqual(obk.split_fields(''), [''])
        self.assertEqual(obk.split_fields('a'), ['a'])
        self.assertEqual(obk.split_fields('a;b'), ['a', 'b'])
