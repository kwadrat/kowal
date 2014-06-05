#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
import np_kw
import ne_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def generate_raport_file(dfb, nazwa_pliku, uu_maper, krt_pobor, id_obiekt):
    if krt_pobor.tvk_pobor == lw_kw.Dm_Energy:
        obk = ne_kw.EnergyWriter()
    else:
        assert krt_pobor.tvk_pobor == lw_kw.Dn_Power
        obk = np_kw.PowerWriter()
    obk.generate_one_file(dfb, nazwa_pliku, uu_maper, id_obiekt=id_obiekt)
