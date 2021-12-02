#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import civ_kw

quotechar = '"'
PodwZnkSepTekstu = quotechar + quotechar


class FieldSplitter(object):
    def inter_col(self, one_char):
        '''
        FieldSplitter:
        '''
        return one_char == self.internal_sep

    def __init__(self):
        '''
        FieldSplitter:
        '''
        self.solid_a = 'CENTRUM REKREACJI i REHABILITACJI "BUSHIDO"'
        self.len_a = len(self.solid_a)
        self.solid_b = '"AL-DUE" ZAKŁAD PRODUKCYJNO-USŁUGOWO-HANDLOWY'
        self.len_b = len(self.solid_b)

    def split_fields(self, line, quoting=0):
        '''
        FieldSplitter:
        '''
        if line.count(civ_kw.xs_semicolon_ql) >= 30:
            self.internal_sep = civ_kw.xs_semicolon_ql
        else:
            self.internal_sep = civ_kw.xs_comma_ql
        self.znaki_konczace_pole_tekstowe = set([
            self.internal_sep,
            chr(13),
            chr(10),
            ])
        t = []
        inside_quote = 0
        cur_ptr = 0 # Wskaźnik na aktualny analizowany znak linii
        ln_len = len(line) # Długość linii
        first_char = 1 # Znacznik - analizujemy pierwszy znak pola wiersza
        work_flag = 1
        while work_flag:
            if first_char:
                first_char = 0
                if line[cur_ptr:cur_ptr + self.len_b] == self.solid_b:
                    strt_pos = cur_ptr
                    cur_ptr += self.len_b
                elif quoting and cur_ptr < ln_len and line[cur_ptr] == quotechar:
                    inside_quote = 1
                    cur_ptr += 1 # Pomiń cudzysłów
                    strt_pos = cur_ptr
                else:
                    inside_quote = 0
                    strt_pos = cur_ptr
                if line[cur_ptr:cur_ptr + self.len_a] == self.solid_a:
                    cur_ptr += self.len_a
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
                        if cur_ptr < ln_len and self.inter_col(line[cur_ptr]):
                            cur_ptr += 1
                            first_char = 1 # Znowu zaczynamy analizę od pierwszego znaku pola
                        else:
                            # Nie było przecinka - koniec analizy
                            work_flag = 0
                else:
                    cur_ptr += 1 # Szukamy następnego znaku
            else: # Nie mamy cudzysłowu - szukamy do następnego przecinka lub końca
                if cur_ptr >= ln_len or line[cur_ptr] in self.znaki_konczace_pole_tekstowe:
                    t.append(line[strt_pos:cur_ptr])
                    if cur_ptr < ln_len and self.inter_col(line[cur_ptr]):
                        cur_ptr += 1 # Będzie kolejne pole
                        first_char = 1
                    else:
                        work_flag = 0 # Koniec analizy - był Enter
                else: # Zwykły znak - przesuwamy się dalej
                    cur_ptr += 1
        return t

local_splitter = FieldSplitter()

def rozbij_na_pola(line, quoting=0):
   return local_splitter.split_fields(line, quoting=quoting)

class TestRozbijaniaCommaSV(unittest.TestCase):
    def test_rozbijania_csv(self):
        '''
        TestRozbijaniaCommaSV:
        '''
        self.assertEqual(rozbij_na_pola(''), [''])
        self.assertEqual(rozbij_na_pola('a'), ['a'])
        self.assertEqual(rozbij_na_pola('a,b'), ['a', 'b'])
        self.assertEqual(rozbij_na_pola('"a"'), ['"a"'])

    def test_object_csv(self):
        '''
        TestRozbijaniaCommaSV:
        '''
        obk = FieldSplitter()
        self.assertEqual(obk.split_fields(''), [''])
        self.assertEqual(obk.split_fields('a'), ['a'])
        self.assertEqual(obk.split_fields('a,b'), ['a', 'b'])
        self.assertEqual(obk.split_fields(
            '"T","CENTRUM REKREACJI i REHABILITACJI "BUSHIDO"","11/11111/2014"', quoting=1),
            ['T', 'CENTRUM REKREACJI i REHABILITACJI "BUSHIDO"', '11/11111/2014'])
        self.assertEqual(obk.split_fields(
            'T,"AL-DUE" ZAKŁAD PRODUKCYJNO-USŁUGOWO-HANDLOWY,22/22222/2014', quoting=1),
            ['T', '"AL-DUE" ZAKŁAD PRODUKCYJNO-USŁUGOWO-HANDLOWY', '22/22222/2014'])
