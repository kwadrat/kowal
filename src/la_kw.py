#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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
        self.n1_style = self.xlwt.XFStyle()
        self.n1_style.num_format_str = '#,##0.00' # użyj separatora 1000
        self.n2_style = self.xlwt.XFStyle()
        self.n2_style.num_format_str = 'yyyy/mm/dd;@' # data RRRR-MM-DD
        align_on = self.xlwt.Alignment()
        align_on.wrap = 1
        self.n3_style = self.xlwt.XFStyle()
        self.n3_style.alignment = align_on # Zawijaj tekst
        self.n4_style = self.xlwt.XFStyle()
        self.n4_style.num_format_str = '[Red]#,##0.00_ ;-#,##0.00 ' # Liczby nieujemne na czerwono, użyj separatora 1000
        self.n5_style = self.xlwt.XFStyle() # Arial 14 pt
        n5_font = self.xlwt.Font()
        n5_font.height = 14 * 20
        self.n5_style.font = n5_font

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

    def zapisz_polaczone_komorki(self, akt_wiersz, akt_kolumna, napis):
        '''
        WriterGateway:
        '''
        ile_w_poziomie = 10
        r1 = akt_wiersz
        r2 = akt_wiersz
        c1 = akt_kolumna
        c2 = akt_kolumna + ile_w_poziomie
        self.sheet.write_merge(r1, r2, c1, c2, en_kw.utf_to_unicode(napis))

    def zapisz_stylowe_polaczone_komorki(self, akt_wiersz, akt_kolumna, napis, style):
        '''
        WriterGateway:
        '''
        ile_w_poziomie = 10
        r1 = akt_wiersz
        r2 = akt_wiersz
        c1 = akt_kolumna
        c2 = akt_kolumna + ile_w_poziomie
        self.sheet.write_merge(r1, r2, c1, c2, en_kw.utf_to_unicode(napis), style=style)

    def zapisz_zawijane(self, akt_wiersz, akt_kolumna, napis):
        '''
        WriterGateway:
        '''
        self.sheet.write(akt_wiersz, akt_kolumna, en_kw.utf_to_unicode(napis), self.n3_style)

    def zapisz_direct(self, akt_wiersz, akt_kolumna, liczba):
        '''
        WriterGateway:
        '''
        self.sheet.write(akt_wiersz, akt_kolumna, liczba)

    def zapisz_ze_stylem(self, akt_wiersz, akt_kolumna, liczba, style):
        '''
        WriterGateway:
        '''
        self.sheet.write(akt_wiersz, akt_kolumna, liczba, style)

    def zapisz_flt(self, akt_wiersz, akt_kolumna, liczba):
        '''
        WriterGateway:
        '''
        self.zapisz_ze_stylem(akt_wiersz, akt_kolumna, liczba, self.n1_style)

    def zapisz_date(self, akt_wiersz, akt_kolumna, liczba):
        '''
        WriterGateway:
        '''
        self.zapisz_ze_stylem(akt_wiersz, akt_kolumna, liczba, self.n2_style)

    def zapisz_stylowy_wzor(self, akt_wiersz, akt_kolumna, tekst_wzoru, the_style):
        '''
        WriterGateway:
        '''
        self.sheet.write(akt_wiersz, akt_kolumna, self.xlwt.Formula(tekst_wzoru), the_style)

    def zapisz_wzor(self, akt_wiersz, akt_kolumna, tekst_wzoru):
        '''
        WriterGateway:
        '''
        self.zapisz_stylowy_wzor(akt_wiersz, akt_kolumna, tekst_wzoru, self.n1_style)

    def zapisz_odwrotny_czerwony_wzor(self, akt_wiersz, akt_kolumna, tekst_wzoru):
        '''
        WriterGateway:
        '''
        self.zapisz_stylowy_wzor(akt_wiersz, akt_kolumna, tekst_wzoru, self.n4_style)

    def zapisz_nazwe_miesiaca(self, akt_wiersz, nr_mies):
        '''
        WriterGateway:
        '''
        akt_kolumna = 0
        self.zapisz_mi(akt_wiersz, akt_kolumna, dn_kw.tab_miesiecy[nr_mies - 1])

def generate_excel_files(dfb, plik_energii, plik_mocy):
    xrg = WriterGateway()
    fu_kw.EnergyReader().generate_one_file(xrg, dfb, plik_energii)
    mt_kw.PowerReader().generate_one_file(xrg, dfb, plik_mocy)
