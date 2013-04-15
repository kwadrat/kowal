#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def new_module_for_reading_spreadsheet():
    '''
    '''
    import xlrd
    return xlrd

def check_module_dependencies_linux():
    new_module_for_reading_spreadsheet()

def analyze_this_file(single_file):
    xlrd = new_module_for_reading_spreadsheet()
    book = xlrd.open_workbook(single_file)
    numer_of_sheets = book.nsheets
    if numer_of_sheets == 1:
        pass
    else:
        raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

def analyze_excel_files(filenames):
    for single_file in filenames:
        analyze_this_file(single_file)
