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

class StiffData(object):
    def __init__(self, wbk):
        '''
        StiffData:
        '''
        self.wbk = wbk

    def przetworz_arkusz(self, sheet, klm_ads):
        '''
        StiffData:
        '''
        ark_name = repr(get_name(sheet))
        print ark_name
        klm_ads.set_ka_base_address('B22')
        wiersz = klm_ads.wiersz_bazowy_miesiecy
        kolumna = klm_ads.kl_assigned_col
        tmp_format = 'sheet.cell(wiersz, kolumna)'; print 'Eval:', tmp_format, eval(tmp_format)
        for fvk_miesiac in la_kw.numery_miesiecy:
            my_xf_index = sheet.cell(wiersz + fvk_miesiac, kolumna)
            tmp_format = 'my_xf_index'; print 'Eval:', tmp_format, eval(tmp_format)

def generate_stiff_data(filename):
    xlrd = la_kw.new_module_for_reading_spreadsheet()
    wbk = xlrd.open_workbook(filename, formatting_info=True)
    klm_ads = gu_kw.KolumnowyAdresator()
    stiff_data = StiffData(wbk)
    for sheet in wbk.sheets():
        stiff_data.przetworz_arkusz(sheet, klm_ads)

class TestTheStiffValues(unittest.TestCase):
    def test_stiff_data(self):
        '''
        TestTheStiffValues:
        '''
