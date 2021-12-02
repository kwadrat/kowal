#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

TymczasowoF = 0
nazwa_aplikacji = 'Excel'
sciezka_sterow_xcl = nazwa_aplikacji + '.Application'


def porownaj_wielkosc_i_kilkubajtowe_roznice(dane_programu, dane_rozpakowane):
    ilea = len(dane_programu)
    ileb = len(dane_rozpakowane)
    if ilea == ileb:
        liczba_roznic = 0
        for i in xrange(ilea):
            if dane_programu[i] != dane_rozpakowane[i]:
                liczba_roznic += 1
        if TymczasowoF:
            tmp_format = "liczba_roznic"; print 'Eval:', tmp_format, repr(eval(tmp_format))
        if liczba_roznic > 10: # Zdarzały się 5-bajtowe różnice
            return 1
        else:
            return 0
    else:
        return 1


def zwroc_pywin32():
    '''
    http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
    pywin32-218.win32-py2.7.exe
    '''
    import win32com.client as win32
    return win32


def NowyXL():
    win32 = zwroc_pywin32()
    return win32.gencache.EnsureDispatch(sciezka_sterow_xcl)


class TestDG(unittest.TestCase):
    def test_napisow(self):
        '''
        TestDG:
        '''
        self.assertEqual(sciezka_sterow_xcl, 'Excel.Application')
