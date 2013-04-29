#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import le_kw
import mu_kw
import mt_kw
import fu_kw
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
    mu_kw.generate_one_file(xlwt, dfb, fu_kw.EnergyReader, lc_kw.fq_uu_energy_qv, 'e.xls')
    mu_kw.generate_one_file(xlwt, dfb, mt_kw.PowerReader, lc_kw.fq_uu_power_qv, 'p.xls')

def analyze_excel_files(dfb, worker_class, filenames):
    xlrd = mu_kw.new_module_for_reading_spreadsheet()
    for single_file in filenames:
        print single_file
        obk = worker_class()
        obk.analyze_this_file(dfb, xlrd, single_file)
