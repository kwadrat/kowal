#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lw_kw
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

def generate_raport_file(dfb, nazwa_pliku, uu_maper, krt_pobor, id_obiekt):
    xwg = la_kw.WriterGateway()
    if krt_pobor.tvk_pobor == lw_kw.Dn_Energy:
        obk = fu_kw.EnergyWriter()
    else:
        assert krt_pobor.tvk_pobor == lw_kw.Dn_Power
        obk = mt_kw.PowerWriter()
    obk.generate_one_file(xwg, dfb, nazwa_pliku, uu_maper, id_obiekt=id_obiekt)

def generate_excel_files(dfb, plik_energii, plik_mocy, uu_maper):
    xwg = la_kw.WriterGateway()
    fu_kw.EnergyWriter().generate_one_file(xwg, dfb, plik_energii, uu_maper)
    mt_kw.PowerWriter().generate_one_file(xwg, dfb, plik_mocy, uu_maper)
