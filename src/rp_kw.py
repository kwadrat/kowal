#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lk_kw
import oa_kw
import pt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

KlasaObrazu = pt_kw.KlasaObrazu

class WykresRaportu(KlasaObrazu):
    def __init__(self, tgk, aqr, dwk, dnw, linii):
        KlasaObrazu.__init__(self, tgk, aqr, dnw, lk_kw.LITERA_WYKRES)
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz
        self.szerokosc_wykresu = self.szerokosc_obrazu - 10
        self.wysokosc_obrazu = 200
        self.wysokosc_linii = 12
        self.wysokosc_obrazu = linii * self.wysokosc_linii + 10
