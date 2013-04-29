#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import le_kw
import mu_kw
import mt_kw
import fu_kw
'''.splitlines()]

def new_module_for_writing_spreadsheet():
    import xlwt
    return xlwt

def check_module_dependencies_linux():
    mu_kw.new_module_for_reading_spreadsheet()
    new_module_for_writing_spreadsheet()

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def generate_excel_files(dfb):
    xlwt = new_module_for_writing_spreadsheet()
    fu_kw.EnergyReader().generate_one_file(xlwt, dfb, 'e.xls')
    mt_kw.PowerReader().generate_one_file(xlwt, dfb, 'p.xls')

def analyze_excel_files(dfb, worker_class, filenames):
    xlrd = mu_kw.new_module_for_reading_spreadsheet()
    for single_file in filenames:
        print single_file
        obk = worker_class()
        obk.analyze_this_file(dfb, xlrd, single_file)
