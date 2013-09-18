#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def Poprzecinkuj(lista):
    '''Zwraca napisy połączone przecinkami
    '''
    return ','.join(lista)

def semicolon_join(lista):
    return ';'.join(lista)

def ladnie_przecinkami(lista):
    return ', '.join(lista)

def Pokoniuguj(lista):
    '''Zwraca napisy w koniunkcji logicznej
    '''
    return ' and\n'.join(lista)

def make_alternatives(lista):
    return ' OR '.join(lista)

def condition_kv(key, value):
    if value is None:
        status = "%(key)s is null" % dict(key=key)
    else:
        status = "%(key)s = '%(value)s'" % dict(key=key, value=value)
    return status

def conditions_separately(klucze, slownik, ignorowane_pola=None):
    lista = []
    for klucz in klucze:
        if ignorowane_pola is not None and klucz in ignorowane_pola:
            pass # Na żądanie użytkownika pomijamy ten klucz
        else:
            wartosc = slownik[klucz]
            lista.append(condition_kv(klucz, wartosc))
    return lista

def otocz_cudzyslowem(napis):
    return '"%s"' % napis

def ls_przec(*args):
    return ladnie_przecinkami(args)

def with_spaces(*args):
    return ' '.join(args)

def zamien_na_logiczne(wartosc):
    return not not wartosc

def przytnij_nazwe(nazwa_katalogu):
    return nazwa_katalogu.replace('/', '')

def wyznacz_litere_faktury(nr_faktury):
    return chr(ord('A') + nr_faktury)

def zakres_liter_faktury(liczba_faktur):
    return '(%s)' % '+'.join(map(wyznacz_litere_faktury, range(liczba_faktur)))

def letter_to_number(single_letter):
    return ord(single_letter.upper()) - ord('A')

def podpis_faktury(rest_of_txt):
    return 'fakt. ' + rest_of_txt

def significant_values_for_months(my_dict):
    return any(v for month, v in my_dict.iteritems() if 1 <= month <= 12)

def rcp_plus(list_of_terms):
    return '+'.join(list_of_terms)

def rcp_minus(first, second):
    return ''.join([first, '-', second])

def rcp_pion(wiersz_bazowy_miesiecy, kl_letter_of_col):
    return 'SUM(%(kl_letter_of_col)s%(mon_january)d:%(kl_letter_of_col)s%(mon_december)d)' % dict(
        mon_january=wiersz_bazowy_miesiecy + 2,
        mon_december=wiersz_bazowy_miesiecy + 13,
        kl_letter_of_col=kl_letter_of_col,
        )

def reverse_but_last(tmp_list):
    tmp_list.sort()
    start_ptr = 0
    end_ptr = len(tmp_list) - 2
    while start_ptr < end_ptr:
        tmp_list[start_ptr], tmp_list[end_ptr] = tmp_list[end_ptr], tmp_list[start_ptr]
        start_ptr += 1
        end_ptr -= 1

def wybierz_ze_slownikow(tmp_list, tmp_key):
    return map(lambda the_dict: the_dict[tmp_key], tmp_list)

def ogranicz_wartosci_umowne(tmp_list):
    without_zero = filter(None, tmp_list)
    without_duplicates = list(set(without_zero))
    return without_duplicates

class TestProcessingSQL(unittest.TestCase):
    def test_processing_sql(self):
        '''
        TestProcessingSQL:
        '''
        self.assertEqual(Poprzecinkuj(['a', 'b', 'c']), 'a,b,c')
        self.assertEqual(semicolon_join(['a', 'b', 'c']), 'a;b;c')
        self.assertEqual(conditions_separately(['a'], {'a': None}), ["a is null"])
        self.assertEqual(conditions_separately(['b'], {'b': 45}), ["b = '45'"])
        self.assertEqual(condition_kv('b', 45), "b = '45'")
        self.assertEqual(condition_kv('c', None), "c is null")
        self.assertEqual(make_alternatives(['a', 'b', 'c']), "a OR b OR c")
        self.assertEqual(ladnie_przecinkami(['a', 'b', 'c']), "a, b, c")
        self.assertEqual(ls_przec('a', 'b', 'c'), 'a, b, c')
        self.assertEqual(with_spaces('a', 'b', 'c'), 'a b c')
        self.assertEqual(zamien_na_logiczne('abc'), 1)
        self.assertEqual(zamien_na_logiczne([]), 0)
        self.assertEqual(przytnij_nazwe('abc'), 'abc')
        self.assertEqual(przytnij_nazwe('/abc/'), 'abc')
        self.assertEqual(wyznacz_litere_faktury(0), 'A')
        self.assertEqual(wyznacz_litere_faktury(1), 'B')
        self.assertEqual(wyznacz_litere_faktury(25), 'Z')
        self.assertEqual(zakres_liter_faktury(2), '(A+B)')
        self.assertEqual(letter_to_number('a'), 0)
        self.assertEqual(letter_to_number('Z'), 25)
        self.assertEqual(podpis_faktury('a'), 'fakt. a')
        self.assertEqual(significant_values_for_months({}), 0)
        self.assertEqual(significant_values_for_months({1:3}), 1)
        self.assertEqual(significant_values_for_months({1:0}), 0)
        self.assertEqual(significant_values_for_months({13:3}), 0)
        self.assertEqual(rcp_plus(['A1', 'B2', 'C3']), 'A1+B2+C3')
        self.assertEqual(rcp_pion(0, 'A'), 'SUM(A2:A13)')
        self.assertEqual(rcp_pion(1, 'A'), 'SUM(A3:A14)')
        self.assertEqual(rcp_pion(0, 'B'), 'SUM(B2:B13)')
        a = [1, 4, 2, 3]; reverse_but_last(a)
        self.assertEqual(a, [3, 2, 1, 4])
        self.assertEqual(wybierz_ze_slownikow([{'a': 1}], 'a'), [1])
        self.assertEqual(wybierz_ze_slownikow([{'a': 1, 'b': 2}], 'b'), [2])
        self.assertEqual(ogranicz_wartosci_umowne([0.0, 0.0, 36.0]), [36.0])
        self.assertEqual(ogranicz_wartosci_umowne([40.0, 40.0, 0.0]), [40.0])
        self.assertEqual(rcp_minus('A1', 'B1'), 'A1-B1')
