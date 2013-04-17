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
    import xlrd
    return xlrd

def check_module_dependencies_linux():
    new_module_for_reading_spreadsheet()

def verify_for_equal(tmp_text, expected):
    if tmp_text != expected:
        raise RuntimeError('tmp_text = %s' % repr(tmp_text))
