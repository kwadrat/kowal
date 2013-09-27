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

def wyznacz_mi_kolor(wbk, my_xf_index):
    the_font = wbk.xf_list[my_xf_index]
    my_font_index = the_font.font_index
    the_font = wbk.font_list[my_font_index]
    the_colour_index = the_font.colour_index
    return the_colour_index

class StiffForSheet(object):
    def __init__(self, wbk, sheet):
        '''
        StiffForSheet:
        '''
        self.wbk = wbk
        self.sheet = sheet

    def przetworz_arkusz(self):
        '''
        StiffForSheet:
        '''
        ark_name = repr(get_name(self.sheet))
        print ark_name
        klm_ads = gu_kw.KolumnowyAdresator()
        klm_ads.set_ka_base_address('B22')
        wiersz = klm_ads.wiersz_bazowy_miesiecy
        kolumna = klm_ads.kl_assigned_col
        tmp_format = 'self.sheet.cell(wiersz, kolumna)'; print 'Eval:', tmp_format, eval(tmp_format)
        for fvk_miesiac in la_kw.numery_miesiecy:
            my_xf_value = self.sheet.cell(wiersz + fvk_miesiac, kolumna)
            tmp_format = 'my_xf_value'; print 'Eval:', tmp_format, eval(tmp_format)

class StiffGeneral(object):
    def __init__(self, wbk):
        '''
        StiffGeneral:
        '''
        self.wbk = wbk

    def wykonaj_operacje(self):
        '''
        StiffGeneral:
        '''
        for sheet in self.wbk.sheets():
            stiff_for_sheet = StiffForSheet(wbk, sheet)
            stiff_for_sheet.przetworz_arkusz(sheet)

def generate_stiff_data(filename):
    xlrd = la_kw.new_module_for_reading_spreadsheet()
    wbk = xlrd.open_workbook(filename, formatting_info=True)
    stiff_data = StiffGeneral(wbk)
    stiff_data.wykonaj_operacje()

class TestTheStiffValues(unittest.TestCase):
    def test_stiff_data(self):
        '''
        TestTheStiffValues:
        '''
