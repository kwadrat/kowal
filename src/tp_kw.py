#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import mt_kw
import fu_kw
import la_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def generate_excel_files(dfb, plik_energii, plik_mocy, slownik_mocy):
    xwg = la_kw.WriterGateway()
    fu_kw.EnergyWriter().generate_one_file(xwg, dfb, plik_energii)
    mt_kw.PowerWriter().generate_one_file(xwg, dfb, plik_mocy)
