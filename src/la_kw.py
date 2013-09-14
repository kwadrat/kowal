#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
import dn_kw
import en_kw
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

numery_miesiecy = range(1, 12 + 1)

def new_module_for_reading_spreadsheet():
    import xlrd
    return xlrd

def new_module_for_writing_spreadsheet():
    import xlwt
    return xlwt

def check_module_dependencies_linux():
    new_module_for_reading_spreadsheet()
    new_module_for_writing_spreadsheet()

def analyze_excel_files(dfb, worker_class, filenames):
    xlrd = new_module_for_reading_spreadsheet()
    for single_file in filenames:
        print single_file
        obk = worker_class()
        obk.analyze_this_file(dfb, xlrd, single_file)

class WriterGateway(object):
    def __init__(self):
        '''
        WriterGateway:
        '''
        self.xlwt = new_module_for_writing_spreadsheet()

    def workbook_create(self):
        '''
        WriterGateway:
        '''
        self.wbk = self.xlwt.Workbook()

    def add_a_sheet(self, sheet_name):
        '''
        WriterGateway:
        '''
        self.sheet = self.wbk.add_sheet(sheet_name)

    def workbook_save(self, nazwa_docelowa):
        '''
        WriterGateway:
        '''
        self.wbk.save(nazwa_docelowa)
        self.wbk = None

    def zapisz_mi(self, akt_wiersz, akt_kolumna, napis):
        '''
        WriterGateway:
        '''
        self.sheet.write(akt_wiersz, akt_kolumna, en_kw.utf_to_unicode(napis))

    def zapisz_flt(self, akt_wiersz, akt_kolumna, liczba):
        '''
        WriterGateway:
        '''
        self.sheet.write(akt_wiersz, akt_kolumna, liczba)

    def zapisz_nazwe_miesiaca(self, akt_wiersz, nr_mies):
        '''
        WriterGateway:
        '''
        akt_kolumna = 0
        self.zapisz_mi(akt_wiersz, akt_kolumna, dn_kw.tab_miesiecy[nr_mies - 1])

    if rq_kw.DocelowoWirtualneKolumny:
        ##############################################################################
        pass
        ##############################################################################
    else:
        ##############################################################################
        def zapisz_pare(self, akt_wiersz, akt_kolumna, napis, litera_faktury):
            '''
            WriterGateway:
            '''
            self.zapisz_mi(akt_wiersz, akt_kolumna, napis)
            if litera_faktury is not None:
                self.zapisz_mi(akt_wiersz + 1, akt_kolumna, litera_faktury)
        ##############################################################################

def generate_excel_files(dfb, plik_energii, plik_mocy):
    xrg = WriterGateway()
    xlwt = new_module_for_writing_spreadsheet()
    fu_kw.EnergyReader().generate_one_file(xrg, xlwt, dfb, plik_energii)
    mt_kw.PowerReader().generate_one_file(xrg, xlwt, dfb, plik_mocy)
