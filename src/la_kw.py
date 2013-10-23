#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import to_kw
import gv_kw
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

NMF_1_above_red = -1
NMF_2_percent = -2

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

def calculate_style(style):
    dc_style = {}
    if style is not None:
        dc_style['style'] = style
    return dc_style

class WriterGateway(object):
    def prepare_cell(self, size=None, bold=None, num_format_str=None, wrap=None, vert=None, horz=None, colour=None, borders=None):
        '''
        WriterGateway:
        '''
        the_style = self.xlwt.XFStyle()
        if borders is not None:
            the_borders = the_style.borders
            the_borders.left = the_borders.right = the_borders.top = the_borders.bottom = the_borders.THIN
        needed_wrap = wrap is not None
        needed_vert = vert is not None
        needed_horz = horz is not None
        if needed_wrap or needed_vert or needed_horz:
            the_align = self.xlwt.Alignment()
            if needed_wrap:
                the_align.wrap = wrap
            if needed_vert:
                the_align.vert = vert
            if needed_horz:
                the_align.horz = horz
            the_style.alignment = the_align
        needed_size = size is not None
        needed_bold = bold is not None
        needed_colour = colour is not None
        if needed_size or needed_bold or needed_colour:
            the_font = self.xlwt.Font()
            if needed_size:
                the_font.height = size * 20 # Arial "size" pt
            if needed_bold:
                the_font.bold = bold
            if needed_colour:
                the_font.colour_index = colour
            the_style.font = the_font
        if num_format_str is not None:
            the_style.num_format_str = num_format_str
        return the_style

    def get_or_generate_style(self, kl_miejsc, rn_colour, bold, size):
        '''
        WriterGateway:
        '''
        the_key = (kl_miejsc, rn_colour, bold, size)
        the_style = self.generated_style_cache.get(the_key)
        if the_style is None:
            dc_params = {}
            if rn_colour is not None:
                colour = self.xlwt.Style.colour_map[rn_colour]
                dc_params['colour'] = colour
            if bold is not None:
                dc_params['bold'] = bold
            if size is not None:
                dc_params['size'] = size
            the_style = self.prepare_cell(
                num_format_str=self.format_map[kl_miejsc],
                vert=self.xlwt.Alignment.VERT_CENTER,
                horz=self.xlwt.Alignment.HORZ_CENTER,
                **dc_params
                )
            self.generated_style_cache[the_key] = the_style
        return the_style

    def __init__(self):
        '''
        WriterGateway:
        '''
        self.generated_style_cache = {}
        self.format_map = {
            0: 'General', # Liczby całkowite bez przecinka, center
            2: '#,##0.00', # użyj separatora 1000, 2 miejsca po przecinku
            3: '#,##0.000', # użyj separatora 1000, 3 miejsca po przecinku
            NMF_1_above_red: '[Red]#,##0.00_ ;-#,##0.00 ',
            NMF_2_percent: '0.00%',
            }
        self.xlwt = new_module_for_writing_spreadsheet()
        self.n1_style = self.get_or_generate_style(2, rn_colour=None, bold=None, size=None)
        self.n2_style = self.prepare_cell(
            num_format_str='yyyy/mm/dd;@' # data RRRR-MM-DD
            )
        self.n3_style = self.prepare_cell(
            vert=self.xlwt.Alignment.VERT_CENTER,
            horz=self.xlwt.Alignment.HORZ_CENTER,
            wrap=1,
            ) # Zawijaj tekst, wycentruj
        # Liczby nieujemne na czerwono, użyj separatora 1000
        self.n4_style = self.get_or_generate_style(NMF_1_above_red, rn_colour=None, bold=None, size=None)
        self.n5_style = self.prepare_cell(14) # Arial 14 pt
        self.n6_style = self.prepare_cell(12, bold=1) # Arial 12 pt, bold
        self.n7_style = self.prepare_cell(
            vert=self.xlwt.Alignment.VERT_CENTER,
            horz=self.xlwt.Alignment.HORZ_CENTER,
            ) # Center vertically, center horizontally
        self.n8_style = self.get_or_generate_style(3, rn_colour=None, bold=None, size=None)
        self.n9_style = self.get_or_generate_style(0, rn_colour=None, bold=None, size=None)
        self.n10_style = self.prepare_cell(
            16,
            vert=self.xlwt.Alignment.VERT_CENTER,
            colour=self.xlwt.Style.colour_map[gv_kw.ECR_sea_green],
            )
        self.n11_style = self.prepare_cell(
            12,
            vert=self.xlwt.Alignment.VERT_CENTER,
            colour=self.xlwt.Style.colour_map[gv_kw.ECR_sea_green],
            bold=1,
            )
        self.n12_style = self.prepare_cell(
            12,
            vert=self.xlwt.Alignment.VERT_CENTER,
            colour=self.xlwt.Style.colour_map[gv_kw.ECR_sea_green],
            )
        self.n13_style = self.prepare_cell(
            12,
            vert=self.xlwt.Alignment.VERT_CENTER,
            horz=self.xlwt.Alignment.HORZ_CENTER,
            bold=1,
            )
        self.n14_style = self.prepare_cell(
            12,
            vert=self.xlwt.Alignment.VERT_CENTER,
            colour=self.xlwt.Style.colour_map[gv_kw.ECR_red],
            )
        self.n15_style = self.prepare_cell(
            12,
            vert=self.xlwt.Alignment.VERT_CENTER,
            colour=self.xlwt.Style.colour_map[gv_kw.ECR_indigo],
            )
        self.n16_style = self.get_or_generate_style(NMF_2_percent, rn_colour=None, bold=None, size=None)
        self.decimal_digits = {
            0: self.n9_style,
            2: self.n1_style,
            3: self.n8_style,
            NMF_2_percent: self.n16_style,
            }

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

    def write_co_single(self, the_content, m_coor, style=None):
        '''
        WriterGateway:
        '''
        akt_wiersz, akt_kolumna = m_coor.wyznacz_dwa()
        dc_style = calculate_style(style)
        self.sheet.write(akt_wiersz, akt_kolumna, the_content, **dc_style)

    def write_single(self, akt_wiersz, akt_kolumna, liczba, style=None):
        '''
        WriterGateway:
        '''
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna)
        akt_wiersz, akt_kolumna = m_coor.wyznacz_dwa()
        dc_style = calculate_style(style)
        self.sheet.write(akt_wiersz, akt_kolumna, liczba, **dc_style)

    def zapisz_surowe_polaczone_komorki(self, the_content, m_coor, style=None):
        '''
        WriterGateway:
        '''
        r1, r2, c1, c2 = m_coor.wyznacz_cztery()
        dc_style = calculate_style(style)
        self.sheet.write_merge(r1, r2, c1, c2, the_content, **dc_style)

    def zapisz_stylowy_wzor(self, akt_wiersz, akt_kolumna, the_content, the_style, liczba_kolumn=1):
        '''
        WriterGateway:
        '''
        if liczba_kolumn == 1:
            self.write_single(akt_wiersz, akt_kolumna, the_content, the_style)
        else:
            m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna, liczba_kolumn)
            self.zapisz_surowe_polaczone_komorki(the_content, m_coor, the_style)

    def zapisz_mi(self, akt_wiersz, akt_kolumna, napis, style=None, liczba_wierszy=1):
        '''
        WriterGateway:
        '''
        the_content = en_kw.utf_to_unicode(napis)
        if liczba_wierszy == 1:
            self.write_single(akt_wiersz, akt_kolumna, the_content, style)
        else:
            m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna, liczba_wierszy=liczba_wierszy)
            self.zapisz_surowe_polaczone_komorki(the_content, m_coor, style)

    def zapisz_swobodne_polaczone_komorki(self, napis, m_coor, style=None):
        '''
        WriterGateway:
        '''
        self.zapisz_surowe_polaczone_komorki(en_kw.utf_to_unicode(napis), m_coor, style=style)

    def zapisz_polaczone_komorki(self, akt_wiersz, akt_kolumna, napis, style, liczba_kolumn):
        '''
        WriterGateway:
        '''
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna, liczba_kolumn)
        self.zapisz_swobodne_polaczone_komorki(napis, m_coor, style)

    def zapisz_rozmiar_14_komorki(self, akt_wiersz, akt_kolumna, napis, liczba_kolumn=8):
        '''
        WriterGateway:
        '''
        self.zapisz_polaczone_komorki(akt_wiersz, akt_kolumna, napis, style=self.n5_style, liczba_kolumn=liczba_kolumn)

    def zapisz_bold_rozmiar_12_komorki(self, akt_wiersz, akt_kolumna, napis, liczba_kolumn=1):
        '''
        WriterGateway:
        '''
        self.zapisz_polaczone_komorki(akt_wiersz, akt_kolumna, napis, style=self.n6_style, liczba_kolumn=liczba_kolumn)

    def zapisz_flt(self, akt_wiersz, akt_kolumna, liczba, kl_miejsc=2):
        '''
        WriterGateway:
        '''
        the_style = self.decimal_digits[kl_miejsc]
        self.write_single(akt_wiersz, akt_kolumna, liczba, the_style)

    def zapisz_rn_flt(self, akt_wiersz, akt_kolumna, rn_liczba):
        '''
        WriterGateway:
        '''
        liczba = rn_liczba.rn_value
        kl_miejsc = rn_liczba.rn_after
        bold = 0
        size = None
        the_style = self.get_or_generate_style(kl_miejsc, rn_liczba.rn_colour, bold, size)
        self.write_single(akt_wiersz, akt_kolumna, liczba, the_style)

    def zapisz_date(self, akt_wiersz, akt_kolumna, liczba):
        '''
        WriterGateway:
        '''
        self.write_single(akt_wiersz, akt_kolumna, liczba, self.n2_style)

    def zapisz_wzor(self, akt_wiersz, akt_kolumna, tekst_wzoru, kl_miejsc=2, liczba_kolumn=1):
        '''
        WriterGateway:
        '''
        if 1:
            ##############################################################################
            gv_kw.RichFormula(liczba_kolumn=liczba_kolumn, rn_after=kl_miejsc)
            the_style = self.decimal_digits[kl_miejsc]
            the_content = self.xlwt.Formula(tekst_wzoru)
            self.zapisz_stylowy_wzor(akt_wiersz, akt_kolumna, the_content, the_style, liczba_kolumn=liczba_kolumn)
            ##############################################################################
        else:
            ##############################################################################
            the_style = self.decimal_digits[kl_miejsc]
            the_content = self.xlwt.Formula(tekst_wzoru)
            self.zapisz_stylowy_wzor(akt_wiersz, akt_kolumna, the_content, the_style, liczba_kolumn=liczba_kolumn)
            ##############################################################################

    def zapisz_odwrotny_czerwony_wzor(self, akt_wiersz, akt_kolumna, tekst_wzoru):
        '''
        WriterGateway:
        '''
        the_content = self.xlwt.Formula(tekst_wzoru)
        self.zapisz_stylowy_wzor(akt_wiersz, akt_kolumna, the_content, self.n4_style)

    def zapisz_nazwe_miesiaca(self, akt_wiersz, nr_mies):
        '''
        WriterGateway:
        '''
        akt_kolumna = 0
        self.zapisz_mi(akt_wiersz, akt_kolumna, dn_kw.tab_miesiecy[nr_mies - 1])

    def ustaw_sam_styl(self, akt_wiersz, akt_kolumna, kl_miejsc=2, rn_colour=None, bold=0, size=None, tresc_napisu=None):
        '''
        WriterGateway:
        '''
        the_style = self.get_or_generate_style(kl_miejsc, rn_colour, bold, size)
        self.write_single(akt_wiersz, akt_kolumna, tresc_napisu, style=the_style)

    def wymus_szerokosci(self, lista_rozmiarow):
        '''
        WriterGateway:
        '''
        for nr_kol, szer_kol in enumerate(lista_rozmiarow):
            skalowana_szerokosc = lista_rozmiarow[nr_kol]
            self.sheet.col(nr_kol).width = skalowana_szerokosc

def generate_excel_files(dfb, plik_energii, plik_mocy):
    xwg = WriterGateway()
    fu_kw.EnergyReader().generate_one_file(xwg, dfb, plik_energii)
    mt_kw.PowerReader().generate_one_file(xwg, dfb, plik_mocy)

class TestArkuszowy(unittest.TestCase):
    def test_arkuszowy(self):
        '''
        TestArkuszowy:
        '''
        self.assertEqual(calculate_style(None), {})
        self.assertEqual(calculate_style(1), {'style':1})
