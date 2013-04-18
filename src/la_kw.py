#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import mu_kw
import mt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def generate_excel_files(dfb):
    xlwt = mu_kw.new_module_for_writing_spreadsheet()
    mt_kw.generate_one_file(xlwt, dfb, 'uu_energy', 'e.xls')
    mt_kw.generate_one_file(xlwt, dfb, 'uu_power', 'p.xls')
