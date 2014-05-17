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

# JavaScript potrzebuje krótkiego, jednoznakowego ampersanda
AMP_JS = 0
AMP_HTML = 1
AMP_NONE = 2

MHG_LAMP = '&amp;' # Łączący ampersand, zakodowany
MHG_SAMP = '&' # Łączący ampersand, jako pojedynczy znak

slownik_wyznacz_spinacz = {
    AMP_JS: MHG_SAMP,
    AMP_HTML: MHG_LAMP,
    AMP_NONE: '',
    }
