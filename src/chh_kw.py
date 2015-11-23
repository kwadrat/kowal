#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

MozliweLataZuzyc = map(str, dn_kw.ListaLatZuzyc)
MozliweLataDlaARok = [rq_kw.PoleWszystko] + MozliweLataZuzyc
MozliweLataDlaBRok = MozliweLataZuzyc
MozliweLataDlaWybranyRok = MozliweLataZuzyc + [rq_kw.PoleWszystko]
