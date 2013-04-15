#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def vx_porz(litera):
    return ord(litera.upper()) - ord('A') + 1

def vx_litera(liczba):
    if 1 <= liczba <= 26:
        return chr(ord('A') + liczba - 1)
    else:
        raise RuntimeError('Poza zakresem?: %s' % repr(liczba))
