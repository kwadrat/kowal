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

ZnakSeparatoraPol = ';'
ZnakSeparatoraTekstu = '"'
PodwZnkSepTekstu = ZnakSeparatoraTekstu + ZnakSeparatoraTekstu
znaki_konczace_pole_tekstowe = set([ZnakSeparatoraPol, chr(13), chr(10)])

def rozbij_na_pola(linia, quoting=0):
    t = []
    w_cudzyslowie = 0
    wsk = 0 # Wskaźnik na aktualny analizowany znak linii
    DlLinii = len(linia) # Długość linii
    pierwszy = 1 # Znacznik - analizujemy pierwszy znak pola wiersza
    pracuj = 1
    while pracuj:
        if pierwszy:
            pierwszy = 0
            if quoting and wsk < DlLinii and linia[wsk] == ZnakSeparatoraTekstu:
                w_cudzyslowie = 1
                wsk += 1 # Pomiń cudzysłów
            else:
                w_cudzyslowie = 0
            pocz = wsk # To jest pierwszy znak pola do zapamiętania
        if w_cudzyslowie:
            # Szukamy zamykającego cudzysłowu
            if wsk >= DlLinii:
                raise RuntimeError, "Wychodzimy poza linię o treści:\n" + linia
            elif quoting and linia[wsk] == ZnakSeparatoraTekstu:
                if wsk + 1 < DlLinii and linia[wsk + 1] == ZnakSeparatoraTekstu: # Pominiemy, jeśli cudzysłów jest podwójny
                    wsk += 2
                else:
                    # Pojedynczy cudzysłów - koniec napisu
                    t.append(linia[pocz:wsk].replace(PodwZnkSepTekstu, ZnakSeparatoraTekstu))
                    wsk += 1
                    # Tu czekamy na przecinek
                    if wsk < DlLinii and linia[wsk] == ZnakSeparatoraPol:
                        wsk += 1
                        pierwszy = 1 # Znowu zaczynamy analizę od pierwszego znaku pola
                    else:
                        # Nie było przecinka - koniec analizy
                        pracuj = 0
            else:
                wsk += 1 # Szukamy następnego znaku
        else: # Nie mamy cudzysłowu - szukamy do następnego przecinka lub końca
            if wsk >= DlLinii or linia[wsk] in znaki_konczace_pole_tekstowe:
                t.append(linia[pocz:wsk])
                if wsk < DlLinii and linia[wsk] == ZnakSeparatoraPol:
                    wsk += 1 # Będzie kolejne pole
                    pierwszy = 1
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
