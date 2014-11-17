#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dv_kw
import ux_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def tassertEqual(self, odp, wzor):
    if odp != wzor:
        dv_kw.zapisz_dla_diagnostyki(odp, wzor)
    self.assertTrue(odp == wzor)

def jdn_ogol_ltra(fnc_x, *args, **kwargs):
    lnc_x = ux_kw.LancOgolOgniw()
    fnc_x(lnc_x, *args, **kwargs)
    return lnc_x.polaczona_tresc()

def nassertEqual(self, fnc_a, wzor, *args, **kwargs):
    odp = jdn_ogol_ltra(fnc_a, *args, **kwargs)
    if odp != wzor:
        dv_kw.zapisz_dla_diagnostyki(odp, wzor)
    self.assertTrue(odp == wzor)
