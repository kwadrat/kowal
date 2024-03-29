#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import fy_kw
import gv_kw
import ckc_kw

mapping_as = ' AS '
db_zero_value = '0'
db_strange_value = '44200'
suffix_comma_separated = '.csv'
suffix_semicolon_separated = '.txt'


def make_mapping(oryg_nazwa, nazwa_pola):
    return ''.join([oryg_nazwa, mapping_as, nazwa_pola])


def substitute_if_needed(dc_changes, tabela_aktualna, nazwa_pola):
    oryg_nazwa = dc_changes.get(tabela_aktualna)
    if oryg_nazwa:
        result = make_mapping(oryg_nazwa, nazwa_pola)
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


def make_where(lista):
    return fy_kw.lxa_23_inst + make_conjunction(lista)


def sql_in(one_field, value_ls):
    return ''.join([
        one_field,
        ' IN ',
        value_ls,
        ])


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
            pass  # Na żądanie użytkownika pomijamy ten klucz
        else:
            wartosc = slownik[klucz]
            lista.append(condition_kv(klucz, wartosc))
    return lista


def otocz_cudzyslowem(napis):
    return '"%s"' % napis


def otocz_apostrofem(napis):
    return "'%s'" % napis


def otocz_nawiasami(napis):
    return '(%s)' % napis


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
    return any(v.rn_value for month, v in ckc_kw.iteritems(my_dict) if 1 <= month <= 12)


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
    without_zero = list(filter(None, tmp_list))
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
    return list(filter(lambda x: x is not None, elements))


def wybierz_najwiekszy(elems):
    value = None
    selected_elements = remove_nones(elems)
    if selected_elements:
        value = max(selected_elements)
    return value


def wybierz_powyzej_progu(local_maximum, local_treshold):
    return local_maximum


def tekstowe_indeksy(lista):
    return list(map(lambda x: (str(x[0]), x[1]), lista))


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


def nazwa_filtrowanego(indeks_testu, diff_letter=None):
    if diff_letter is None:
        diff_letter = ''
    return 'gen_filtered_%d%s%s' % (
        indeks_testu,
        diff_letter,
        suffix_comma_separated,
        )


def space_two(first, second):
    return '%s %s' % (first, second)


def full_field(first, second):
    return ''.join([
        first,
        '.',
        second,
        ])


def chop_go(elements):
    return elements[:2]


def op_hd(title):
    if 1:
        result = title
    else:
        result = None
    return result


def date_greater_or_equal(date_label, date_value):
    return ''.join([
        date_label,
        " >= ",
        date_value,
        ])


def fields_equal(label, another):
    return ''.join([
        label,
        " = ",
        another,
        ])


def netto_from_brutto(brutto, vat_rate):
    return ''.join([
        "(",
        brutto,
        " * 100.0 / (100.0 + ",
        vat_rate,
        "))",
        ])


def enum_one(text):
    all_lines = text.splitlines()
    return enumerate(all_lines, start=1)


def labels_to_indexes(some_labels, all_labels):
    return list(map(lambda x: all_labels.index(x), some_labels))


def remove_duplicates(one_ls):
    return sorted(set(one_ls))


def make_cast(one_value, one_type):
    inside = make_mapping(one_value, one_type)
    return 'CAST' + otocz_nawiasami(inside)


class TestProcessingSQL(unittest.TestCase):
    def test_processing_sql(self):
        '''
        TestProcessingSQL:
        '''
        self.assertEqual(mapping_as, ' AS ')
        self.assertEqual(make_mapping('a', 'pole'), 'a AS pole')
        self.assertEqual(db_zero_value, '0')
        self.assertEqual(db_strange_value, '44200')
        self.assertEqual(substitute_if_needed({}, 't1', 'pole'), 'pole')
        self.assertEqual(substitute_if_needed({'t1': 'a'}, 't1', 'pole'), 'a AS pole')
        self.assertEqual(substitute_if_needed({'t2': '0'}, 't2', 'field'), '0 AS field')
        self.assertEqual(Poprzecinkuj(['a', 'b', 'c']), 'a,b,c')
        self.assertEqual(semicolon_join(['a', 'b', 'c']), 'a;b;c')
        self.assertEqual(conditions_separately(['a'], {'a': None}), ["a is null"])
        self.assertEqual(conditions_separately(['b'], {'b': 45}), ["b = '45'"])
        self.assertEqual(condition_kv('b', 45), "b = '45'")
        self.assertEqual(condition_kv('c', None), "c is null")
        self.assertEqual(make_alternatives(['a', 'b', 'c']), "a OR b OR c")
        self.assertEqual(make_conjunction(['a', 'b', 'c']), "a AND b AND c")
        self.assertEqual(make_where(['a', 'b']), " WHERE a AND b")
        self.assertEqual(ladnie_przecinkami(['a', 'b', 'c']), "a, b, c")
        self.assertEqual(sql_in('a', 'b'), "a IN b")
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
        self.assertEqual(significant_values_for_months({1: gv_kw.RichNumber(3)}), 1)
        self.assertEqual(significant_values_for_months({1: gv_kw.RichNumber(0)}), 0)
        self.assertEqual(significant_values_for_months({13: gv_kw.RichNumber(3)}), 0)
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
        a = [1, 4, 2, 3]
        reverse_but_last(a)
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
        self.assertEqual(md_vt('b', year=2010), 'b*1.22')
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
        self.assertEqual(nazwa_filtrowanego(5, 'a'), 'gen_filtered_5a.csv')
        self.assertEqual(space_two('a', 'b'), 'a b')
        self.assertEqual(list(enum_one('a\nb')), [(1, 'a'), (2, 'b')])
        self.assertEqual(list(enum_one('a\nb\nc')), [(1, 'a'), (2, 'b'), (3, 'c')])
        self.assertEqual(chop_go(['id', 'name', 'go']), ['id', 'name'])
        self.assertEqual(otocz_nawiasami('a'), '(a)')
        self.assertEqual(otocz_nawiasami('bc'), '(bc)')
        self.assertEqual(otocz_cudzyslowem('bc'), '"bc"')
        self.assertEqual(otocz_apostrofem('bc'), "'bc'")
        self.assertEqual(op_hd('bc'), 'bc')
        self.assertEqual(full_field('table', 'field'), 'table.field')
        self.assertEqual(date_greater_or_equal('label', "'2017-01-25'"), "label >= '2017-01-25'")
        self.assertEqual(fields_equal('label', 'another'), "label = another")
        self.assertEqual(netto_from_brutto('brutto', 'vat_rate'), "(brutto * 100.0 / (100.0 + vat_rate))")
        self.assertEqual(labels_to_indexes('a c'.split(), 'a b c d'.split()), [0, 2])
        self.assertEqual(labels_to_indexes('a c'.split(), 'e a b c d'.split()), [1, 3])
        self.assertEqual(remove_duplicates('b a a'.split()), 'a b'.split())
        self.assertEqual(remove_duplicates('d a b c a b a'.split()), 'a b c d'.split())
        self.assertEqual(make_cast('data_value', 'data_type'), 'CAST(data_value AS data_type)')
        self.assertEqual(make_cast('other', 'type_b'), 'CAST(other AS type_b)')
