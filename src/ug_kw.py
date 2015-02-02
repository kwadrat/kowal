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

    def split_fields(self, line, quoting=0):
        '''
        FieldSplitter:
        '''
        t = []
        inside_quote = 0
        cur_ptr = 0 # Wskaźnik na aktualny analizowany znak linii
        ln_len = len(line) # Długość linii
        first_char = 1 # Znacznik - analizujemy pierwszy znak pola wiersza
        work_flag = 1
        while work_flag:
            if first_char:
                first_char = 0
                if quoting and cur_ptr < ln_len and line[cur_ptr] == quotechar:
                    inside_quote = 1
                    cur_ptr += 1 # Pomiń cudzysłów
                else:
                    inside_quote = 0
                strt_pos = cur_ptr # To jest pierwszy znak pola do zapamiętania
            if inside_quote:
                # Szukamy zamykającego cudzysłowu
                if cur_ptr >= ln_len:
                    raise RuntimeError, "Wychodzimy poza linię o treści:\n" + line
                elif quoting and line[cur_ptr] == quotechar:
                    if cur_ptr + 1 < ln_len and line[cur_ptr + 1] == quotechar: # Pominiemy, jeśli cudzysłów jest podwójny
                        cur_ptr += 2
                    else:
                        # Pojedynczy cudzysłów - koniec napisu
                        t.append(line[strt_pos:cur_ptr].replace(PodwZnkSepTekstu, quotechar))
                        cur_ptr += 1
                        # Tu czekamy na przecinek
                        if cur_ptr < ln_len and line[cur_ptr] == delimiter:
                            cur_ptr += 1
                            first_char = 1 # Znowu zaczynamy analizę od pierwszego znaku pola
                        else:
                            # Nie było przecinka - koniec analizy
                            work_flag = 0
                else:
                    cur_ptr += 1 # Szukamy następnego znaku
            else: # Nie mamy cudzysłowu - szukamy do następnego przecinka lub końca
                if cur_ptr >= ln_len or line[cur_ptr] in znaki_konczace_pole_tekstowe:
                    t.append(line[strt_pos:cur_ptr])
                    if cur_ptr < ln_len and line[cur_ptr] == delimiter:
                        cur_ptr += 1 # Będzie kolejne pole
                        first_char = 1
                    else:
                        work_flag = 0 # Koniec analizy - był Enter
                else: # Zwykły znak - przesuwamy się dalej
                    cur_ptr += 1
        return t

def rozbij_na_pola(line, quoting=0):
    t = []
    inside_quote = 0
    cur_ptr = 0 # Wskaźnik na aktualny analizowany znak linii
    ln_len = len(line) # Długość linii
    first_char = 1 # Znacznik - analizujemy pierwszy znak pola wiersza
    work_flag = 1
    while work_flag:
        if first_char:
            first_char = 0
            if quoting and cur_ptr < ln_len and line[cur_ptr] == quotechar:
                inside_quote = 1
                cur_ptr += 1 # Pomiń cudzysłów
            else:
                inside_quote = 0
            strt_pos = cur_ptr # To jest pierwszy znak pola do zapamiętania
        if inside_quote:
            # Szukamy zamykającego cudzysłowu
            if cur_ptr >= ln_len:
                raise RuntimeError, "Wychodzimy poza linię o treści:\n" + line
            elif quoting and line[cur_ptr] == quotechar:
                if cur_ptr + 1 < ln_len and line[cur_ptr + 1] == quotechar: # Pominiemy, jeśli cudzysłów jest podwójny
                    cur_ptr += 2
                else:
                    # Pojedynczy cudzysłów - koniec napisu
                    t.append(line[strt_pos:cur_ptr].replace(PodwZnkSepTekstu, quotechar))
                    cur_ptr += 1
                    # Tu czekamy na przecinek
                    if cur_ptr < ln_len and line[cur_ptr] == delimiter:
                        cur_ptr += 1
                        first_char = 1 # Znowu zaczynamy analizę od pierwszego znaku pola
                    else:
                        # Nie było przecinka - koniec analizy
                        work_flag = 0
            else:
                cur_ptr += 1 # Szukamy następnego znaku
        else: # Nie mamy cudzysłowu - szukamy do następnego przecinka lub końca
            if cur_ptr >= ln_len or line[cur_ptr] in znaki_konczace_pole_tekstowe:
                t.append(line[strt_pos:cur_ptr])
                if cur_ptr < ln_len and line[cur_ptr] == delimiter:
                    cur_ptr += 1 # Będzie kolejne pole
                    first_char = 1
                else:
                    work_flag = 0 # Koniec analizy - był Enter
            else: # Zwykły znak - przesuwamy się dalej
                cur_ptr += 1
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
