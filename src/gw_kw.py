#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Import danych sztywnych (ręcznie wpisanych do arkusza), aby
móc ich potem użyć do generowania raportów
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import gu_kw
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

def get_name(sheet):
    return sheet.name

def przetworz_arkusz(sheet):
    ark_name = repr(get_name(sheet))
    print ark_name

def generate_stiff_data(filename):
    xlrd = la_kw.new_module_for_reading_spreadsheet()
    wbk = xlrd.open_workbook(filename, formatting_info=True)
    klm_ads = gu_kw.KolumnowyAdresator()
    for sheet in wbk.sheets():
        przetworz_arkusz(sheet)

class TestTheStiffValues(unittest.TestCase):
    def test_stiff_data(self):
        '''
        TestTheStiffValues:
        '''
