#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def dodaj_z_listy(lista_slownikow, lista_kluczy):
    suma_dzl = lm_kw.wartosc_zero_globalna
    for lokalny_slownik in lista_slownikow:
        dodatkowa_kwota = lm_kw.decimal_suma_wybranych_wpisow_slownika(lokalny_slownik, lista_kluczy)
        suma_dzl += dodatkowa_kwota
    return suma_dzl
