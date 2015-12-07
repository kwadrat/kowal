#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import gv_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

zerowa_fraza = ' AS '
zerowe_pole = '0' + zerowa_fraza
suffix_comma_separated = '.csv'
suffix_semicolon_separated = '.txt'

def zeruj_dla_tabeli(tabela_wzorcowa, tabela_aktualna, nazwa_pola):
    if tabela_wzorcowa == tabela_aktualna:
        result = zerowe_pole + nazwa_pola
    else:
        result = nazwa_pola
    return result

def zeruj_dla_kilku(lista_wzorcowych, tabela_aktualna, nazwa_pola):
    if tabela_aktualna in lista_wzorcowych:
        result = zerowe_pole + nazwa_pola
    else:
        result = nazwa_pola
    return result

def zeruj_z_podmiana(dc_changes, tabela_aktualna, nazwa_pola):
    oryg_nazwa = dc_changes.get(tabela_aktualna)
    if oryg_nazwa:
        result = ''.join([oryg_nazwa, zerowa_fraza, nazwa_pola])
    else:
        result = nazwa_pola
    return result

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

def make_conjunction(lista):
    return ' AND '.join(lista)

def fx_jn(*elements):
    return ''.join(elements)

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
    return any(v.rn_value for month, v in my_dict.iteritems() if 1 <= month <= 12)

def rcp_plus(list_of_terms):
    return '+'.join(list_of_terms)

def rcp_minus(first, second):
    return ''.join([first, '-', second])

def rcp_dziel(first, second):
    return ''.join([first, '/', second])

def rcp_mnoz(first, second):
    return ''.join([first, '*', second])

def rcp_vertical_sum(first_row, row_cnt, kl_letter_of_col):
    return 'SUM(%(kl_letter_of_col)s%(label_first)d:%(kl_letter_of_col)s%(label_last)d)' % dict(
        label_first=first_row,
        label_last=first_row + row_cnt - 1,
        kl_letter_of_col=kl_letter_of_col,
        )

def rcp_pion(wiersz_bazowy_miesiecy, kl_letter_of_col):
    return rcp_vertical_sum(wiersz_bazowy_miesiecy + 2, 12, kl_letter_of_col)

def rcp_wspolne(command, etk_a, etk_b, trzeci=''):
    return '%(command)s(%(etk_a)s:%(etk_b)s%(trzeci)s)' % dict(
        command=command,
        etk_a=etk_a,
        etk_b=etk_b,
        trzeci=trzeci,
        )

def rcp_poziom(etk_a, etk_b):
    return rcp_wspolne('SUM', etk_a, etk_b)

def rcp_sred(etk_a, etk_b):
    return rcp_wspolne('AVERAGE', etk_a, etk_b)

def rcp_emax(etk_a, etk_b):
    return rcp_wspolne('MAX', etk_a, etk_b)

def rcp_diff_max(etk_a, etk_b):
    return 'MAX(0,%s-%s)' % (etk_a, etk_b)

def rcp_emin(etk_a, etk_b):
    return rcp_wspolne('MIN', etk_a, etk_b)

def rcp_maxk(etk_a, etk_b, the_order):
    trzeci = ',%d' % (the_order + 1)
    return rcp_wspolne('LARGE', etk_a, etk_b, trzeci)

def reverse_but_last(tmp_list):
    tmp_list.sort()
    start_ptr = 0
    end_ptr = len(tmp_list) - 2
    while start_ptr < end_ptr:
        tmp_list[start_ptr], tmp_list[end_ptr] = tmp_list[end_ptr], tmp_list[start_ptr]
        start_ptr += 1
        end_ptr -= 1

def ogranicz_wartosci_umowne(tmp_list):
    without_zero = filter(None, tmp_list)
    without_duplicates = list(set(without_zero))
    return without_duplicates

def rc_rozszczep(the_label):
    the_index = None
    for the_index, the_sign in enumerate(the_label):
        if the_sign.isdigit():
            break
    else:
        raise RuntimeError('The label?: %s' % repr(the_label))
    the_letters = the_label[:the_index]
    the_number = int(the_label[the_index:])
    return the_letters, the_number

def md_fn(modul, funkcja):
    return '%s.%s' % (modul, funkcja)

def md_vt(value, year):
    if year > 2010:
        multiplier = '1.23'
    else:
        multiplier = '1.22'
    result = fx_jn(value, '*', multiplier)
    return result

def remove_nones(elements):
    return filter(lambda x: x is not None, elements)

def wybierz_najwiekszy(elems):
    value = None
    selected_elements = remove_nones(elems)
    if selected_elements:
        value = max(selected_elements)
    return value

def wybierz_powyzej_progu(local_maximum, local_treshold):
    return local_maximum

def tekstowe_indeksy(lista):
    return map(lambda x: (str(x[0]), x[1]), lista)

def make_hl(url, label):
    return 'HYPERLINK("%(url)s";"%(label)s")' % dict(
        url=url,
        label=label,
        )

def hlp_assume_one(id_obkt, wynik, etykieta):
    assert len(wynik) == 1, id_obkt
    return wynik[0][etykieta]

def zrob_wersje_posrednia(nazwa):
    return 'gen_%s.txt' % nazwa

def nazwa_filtrowanego(indeks_testu):
    return 'gen_filtered_%d%s' % (indeks_testu, suffix_comma_separated)

def space_two(first, second):
    return '%s %s' % (first, second)

def chop_go(elements):
    return elements[:2]

if sys.version.split()[0] == '2.5.1':
    def enum_one(text):
        all_lines = text.splitlines()
        nr = 1
        for one_line in all_lines:
            yield nr, one_line
            nr += 1
else:
    def enum_one(text):
        all_lines = text.splitlines()
        return enumerate(all_lines, start=1)

class TestProcessingSQL(unittest.TestCase):
    def test_processing_sql(self):
        '''
        TestProcessingSQL:
        '''
        self.assertEqual(zerowa_fraza, ' AS ')
        self.assertEqual(zerowe_pole, '0 AS ')
        self.assertEqual(zeruj_dla_tabeli('a', 'b', 'pole'), 'pole')
        self.assertEqual(zeruj_dla_tabeli('a', 'a', 'pole'), '0 AS pole')
        self.assertEqual(zeruj_dla_kilku(['a', 'b'], 'a', 'pole'), '0 AS pole')
        self.assertEqual(zeruj_dla_kilku(['a', 'b'], 'b', 'pole'), '0 AS pole')
        self.assertEqual(zeruj_z_podmiana({}, 't1', 'pole'), 'pole')
        self.assertEqual(zeruj_z_podmiana({'t1': 'a'}, 't1', 'pole'), 'a AS pole')
        self.assertEqual(zeruj_z_podmiana({'t2': '0'}, 't2', 'field'), '0 AS field')
        self.assertEqual(Poprzecinkuj(['a', 'b', 'c']), 'a,b,c')
        self.assertEqual(semicolon_join(['a', 'b', 'c']), 'a;b;c')
        self.assertEqual(conditions_separately(['a'], {'a': None}), ["a is null"])
        self.assertEqual(conditions_separately(['b'], {'b': 45}), ["b = '45'"])
        self.assertEqual(condition_kv('b', 45), "b = '45'")
        self.assertEqual(condition_kv('c', None), "c is null")
        self.assertEqual(make_alternatives(['a', 'b', 'c']), "a OR b OR c")
        self.assertEqual(make_conjunction(['a', 'b', 'c']), "a AND b AND c")
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
        self.assertEqual(significant_values_for_months({1:gv_kw.RichNumber(3)}), 1)
        self.assertEqual(significant_values_for_months({1:gv_kw.RichNumber(0)}), 0)
        self.assertEqual(significant_values_for_months({13:gv_kw.RichNumber(3)}), 0)
        self.assertEqual(rcp_plus(['A1', 'B2', 'C3']), 'A1+B2+C3')
        self.assertEqual(rcp_vertical_sum(2, 12, 'A'), 'SUM(A2:A13)')
        self.assertEqual(rcp_pion(0, 'A'), 'SUM(A2:A13)')
        self.assertEqual(rcp_pion(1, 'A'), 'SUM(A3:A14)')
        self.assertEqual(rcp_pion(0, 'B'), 'SUM(B2:B13)')
        self.assertEqual(rcp_poziom('E23', 'G23'), 'SUM(E23:G23)')
        self.assertEqual(rcp_sred('E23', 'G23'), 'AVERAGE(E23:G23)')
        self.assertEqual(rcp_emax('E23', 'G23'), 'MAX(E23:G23)')
        self.assertEqual(rcp_emin('E23', 'G23'), 'MIN(E23:G23)')
        self.assertEqual(rcp_maxk('C2', 'CT31', 0), 'LARGE(C2:CT31,1)')
        self.assertEqual(rcp_maxk('C2', 'CT31', 1), 'LARGE(C2:CT31,2)')
        self.assertEqual(rcp_diff_max('E23', 'G23'), 'MAX(0,E23-G23)')
        a = [1, 4, 2, 3]; reverse_but_last(a)
        self.assertEqual(a, [3, 2, 1, 4])
        self.assertEqual(ogranicz_wartosci_umowne([0.0, 0.0, 36.0]), [36.0])
        self.assertEqual(ogranicz_wartosci_umowne([40.0, 40.0, 0.0]), [40.0])
        self.assertEqual(rcp_minus('A1', 'B1'), 'A1-B1')
        self.assertEqual(rcp_dziel('A1', 'B1'), 'A1/B1')
        self.assertEqual(rcp_mnoz('A1', 'B1'), 'A1*B1')
        self.assertEqual(rc_rozszczep('A1'), ('A', 1))
        self.assertEqual(rc_rozszczep('B1'), ('B', 1))
        self.assertEqual(rc_rozszczep('B2'), ('B', 2))
        self.assertEqual(rc_rozszczep('AB234'), ('AB', 234))
        self.assertRaises(RuntimeError, rc_rozszczep, 'A')
        self.assertEqual(md_fn('a', 'b'), 'a.b')
        self.assertEqual(md_vt('a', year=2011), 'a*1.23')
        self.assertEqual(md_vt('a', year=2010), 'a*1.22')
        self.assertEqual(wybierz_najwiekszy([]), None)
        self.assertEqual(wybierz_najwiekszy([1]), 1)
        self.assertEqual(wybierz_najwiekszy([2, 1]), 2)
        self.assertEqual(wybierz_powyzej_progu(None, 0), None)
        self.assertEqual(wybierz_powyzej_progu(1, 0), 1)
        self.assertEqual(fx_jn('a', 'b', 'cd'), 'abcd')
        self.assertEqual(tekstowe_indeksy([(1, 'a', 'ignored_go')]), [('1', 'a')])
        self.assertEqual(make_hl('http://www.example.com', 'Text'), 'HYPERLINK("http://www.example.com";"Text")')
        self.assertRaises(AssertionError, hlp_assume_one, None, [], None)
        self.assertRaises(AssertionError, hlp_assume_one, None, [1, 2], None)
        self.assertEqual(hlp_assume_one(1, [{'e': 'value'}], 'e'), 'value')
        self.assertEqual(zrob_wersje_posrednia('a'), 'gen_a.txt')
        self.assertEqual(suffix_comma_separated, '.csv')
        self.assertEqual(suffix_semicolon_separated, '.txt')
        self.assertEqual(nazwa_filtrowanego(4), 'gen_filtered_4.csv')
        self.assertEqual(space_two('a', 'b'), 'a b')
        self.assertEqual(list(enum_one('a\nb')), [(1, 'a'), (2, 'b')])
        self.assertEqual(list(enum_one('a\nb\nc')), [(1, 'a'), (2, 'b'), (3, 'c')])
        self.assertEqual(chop_go(['id', 'name', 'go']), ['id', 'name'])

