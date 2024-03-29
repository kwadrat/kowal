#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Moduł do konwersji kodowania (Unicode, UTF-8, CP-852)
'''

import ckd_kw

import pickle
import binascii
import unittest


en_cod_cp_win = 'cp1250'
en_cod_cp_u_eig = 'utf-8'
en_cod_cp_i_two = 'iso-8859-2'
en_cod_cp_ibm_two = 'cp852'


def utf_to_unicode(napis_utf):
    if not ckd_kw.three_or_more:
        napis_utf = napis_utf.decode(en_cod_cp_u_eig)
    return napis_utf


def pwd_to_unicode(napis_utf):
    if ckd_kw.three_or_more:
        result = napis_utf
    else:
        result = utf_to_unicode(napis_utf)
    return result


def unicode_to_string(napis_uncd):
    if not ckd_kw.three_or_more:
        napis_uncd = napis_uncd.encode(en_cod_cp_u_eig)
    return napis_uncd


def str_to_bt(in_str):
    if ckd_kw.three_or_more and type(in_str) is str:
        in_str = in_str.encode(en_cod_cp_u_eig)
    return in_str


def bt_to_string(in_txt):
    if ckd_kw.three_or_more and type(in_txt) is bytes:
        in_txt = in_txt.decode(en_cod_cp_u_eig)
    return in_txt


def win_cp_to_unicode(napis_win):
    return napis_win.decode(en_cod_cp_win)


def win_cp_to_string(napis_win):
    napis_uncd = napis_win.decode(en_cod_cp_win)
    return unicode_to_string(napis_uncd)


def pobierz_z_napisu(napis):
    return pickle.loads(napis)


def zamien_na_napis(przedmiot):
    return pickle.dumps(przedmiot)


def zakoduj_jako_napis(slownik):
    a = zamien_na_napis(slownik)
    a = binascii.b2a_hex(a)
    return a


def odkoduj_z_napisu(napis):
    a = binascii.a2b_hex(napis)
    slownik = pobierz_z_napisu(a)
    return slownik


def upgrade_bytes_to_unicode(value):
    if (type(value) is str) != ckd_kw.three_or_more:
        value = win_cp_to_unicode(value)
    return value


def through_latin_two(one_strng):
    uncd_vrsn = utf_to_unicode(one_strng)
    result = uncd_vrsn.encode(en_cod_cp_i_two)
    return result


def through_cp_for_plsh_win(one_strng):
    uncd_vrsn = utf_to_unicode(one_strng)
    result = uncd_vrsn.encode(en_cod_cp_win)
    return result


class TestEncoding(unittest.TestCase):
    '''
    Testowanie funkcji zmieniających kodowanie napisów
    '''

    def test_konwersja_unicode(self):
        '''
        TestEncoding:
        '''
        self.assertEqual(utf_to_unicode('ąćęłńóśżźĄĆĘŁŃÓŚŻŹ'), u'ąćęłńóśżźĄĆĘŁŃÓŚŻŹ')
        self.assertEqual(unicode_to_string(u'ąćęłńóśżźĄĆĘŁŃÓŚŻŹ'), 'ąćęłńóśżźĄĆĘŁŃÓŚŻŹ')
        self.assertEqual(win_cp_to_unicode(b'\xb9\x9c\x9f'), u'ąśź')
        self.assertEqual(win_cp_to_string(b'\xb9\x9c\x9f'), 'ąśź')
        self.assertEqual(upgrade_bytes_to_unicode(b'\xb9\x9c\x9f'), u'ąśź')
        self.assertEqual(upgrade_bytes_to_unicode(u'ą'), u'ą')
        self.assertEqual(en_cod_cp_win, 'cp1250')
        self.assertEqual(en_cod_cp_u_eig, 'utf-8')
        self.assertEqual(en_cod_cp_i_two, 'iso-8859-2')
        self.assertEqual(en_cod_cp_ibm_two, 'cp852')
