#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def pokaz_na_czerwono(napis, czy_na_stderr):
    if czy_na_stderr:
        plik = sys.stderr
    else:
        plik = sys.stdout
    if plik.isatty():
        ZnakEscape = chr(27)
        return '%(escape)s[31m%(napis)s%(escape)s[0m' % { 'escape': ZnakEscape, 'napis': napis }
    else:
        return napis
