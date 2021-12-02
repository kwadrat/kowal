#!/usr/bin/python
# -*- coding: UTF-8 -*-

import locale
import operator


def UstawienieLocale():
    NazwaLocale = "pl_PL.UTF-8"
    locale.setlocale(locale.LC_COLLATE, NazwaLocale)
    locale.setlocale(locale.LC_CTYPE, NazwaLocale)


def poukladaj_wedlug_drugiego(przedzialy):
    przedzialy.sort(key=operator.itemgetter(1), reverse=False)
