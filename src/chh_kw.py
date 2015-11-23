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

MozliweLataDlaARok = [rq_kw.PoleWszystko] + dn_kw.MozliweLataZuzyc
MozliweLataDlaBRok = dn_kw.MozliweLataZuzyc
MozliweLataDlaWybranyRok = dn_kw.MozliweLataZuzyc + [rq_kw.PoleWszystko]
