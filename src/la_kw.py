#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ng_kw
import nf_kw
import to_kw
import gv_kw
import dn_kw
import en_kw
import np_kw
import ne_kw
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
NMF_3_date = -3

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
        obk.analyze_this_file(xlrd, single_file)
        obk.analyze_data_in_grid(dfb)

def calculate_style(style):
    dc_style = {}
    if style is not None:
        dc_style['style'] = style
    return dc_style

class WriterGateway(object):
    '''
    Obsługa:
    - liczba
    - napis
    - wzór
    - None - puste pole, które ma formatowanie
    '''
    def prepare_cell(self, size=None, bold=None, num_format_str=None, wrap=None, vert=None, horz=None, colour=None, borders=None, italic=None, fore_colour=None):
        '''
        WriterGateway:
        '''
        the_style = self.xlwt.XFStyle()
        if borders is not None:
            borders.force_borders(the_style)
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
        needed_italic = italic is not None
        needed_fore_colour = fore_colour is not None
        if needed_size or needed_bold or needed_colour or needed_italic:
            the_font = self.xlwt.Font()
            if needed_size:
                the_font.height = size * 20 # Arial "size" pt
            if needed_bold:
                the_font.bold = bold
            if needed_italic:
                the_font.italic = italic
            if needed_colour:
                the_font.colour_index = colour
            the_style.font = the_font
        if needed_fore_colour:
            pattern = self.xlwt.Pattern()
            if needed_fore_colour:
                pattern.pattern_fore_colour = fore_colour
            pattern.pattern = self.xlwt.Pattern.SOLID_PATTERN
            the_style.pattern = pattern
        if num_format_str is not None:
            the_style.num_format_str = num_format_str
        return the_style

    def get_or_generate_style(self, rn_colour=None, bold=None, size=None, wrap=None, middle=None, kl_none=None, italic=None, borders=None, fore_colour=None):
        '''
        WriterGateway:
        '''
        if kl_none:
            the_style = None
        else:
            the_key = (rn_colour, bold, size, wrap, middle, italic, borders)
            the_style = self.generated_string_style_cache.get(the_key)
            if the_style is None:
                dc_params = {}
                if rn_colour is not None:
                    colour = self.xlwt.Style.colour_map[rn_colour]
                    dc_params['colour'] = colour
                if bold is not None:
                    dc_params['bold'] = bold
                if size is not None:
                    dc_params['size'] = size
                if wrap is not None:
                    dc_params['wrap'] = wrap
                if borders is not None:
                    dc_params['borders'] = borders
                if italic is not None:
                    dc_params['italic'] = italic
                if middle:
                    dc_params['vert'] = self.xlwt.Alignment.VERT_CENTER
                    dc_params['horz'] = self.xlwt.Alignment.HORZ_CENTER
                if fore_colour is not None:
                    colour = self.xlwt.Style.colour_map[fore_colour]
                    dc_params['fore_colour'] = colour
                the_style = self.prepare_cell(**dc_params)
                self.generated_string_style_cache[the_key] = the_style
        return the_style

    def get_or_generate_number_style(self, kl_miejsc=2, rn_colour=None, bold=None, size=None, middle=1, borders=None, italic=None, fore_colour=None):
        '''
        WriterGateway:
        '''
        the_key = (kl_miejsc, rn_colour, bold, size, middle, borders, italic, fore_colour)
        the_style = self.generated_number_style_cache.get(the_key)
        if the_style is None:
            dc_params = {}
            if rn_colour is not None:
                colour = self.xlwt.Style.colour_map[rn_colour]
                dc_params['colour'] = colour
            if bold is not None:
                dc_params['bold'] = bold
            if size is not None:
                dc_params['size'] = size
            if borders is not None:
                dc_params['borders'] = borders
            if italic is not None:
                dc_params['italic'] = italic
            if fore_colour is not None:
                colour = self.xlwt.Style.colour_map[fore_colour]
                dc_params['fore_colour'] = colour
            if middle:
                dc_params['vert'] = self.xlwt.Alignment.VERT_CENTER
                dc_params['horz'] = self.xlwt.Alignment.HORZ_CENTER
            the_style = self.prepare_cell(
                num_format_str=self.format_map[kl_miejsc],
                **dc_params
                )
            self.generated_number_style_cache[the_key] = the_style
        return the_style

    def __init__(self):
        '''
        WriterGateway:
        '''
        self.generated_string_style_cache = {}
        self.generated_number_style_cache = {}
        self.format_map = {
            0: 'General', # Liczby całkowite bez przecinka, center
            2: '#,##0.00', # użyj separatora 1000, 2 miejsca po przecinku
            3: '#,##0.000', # użyj separatora 1000, 3 miejsca po przecinku
            NMF_1_above_red: '[Red]#,##0.00_ ;-#,##0.00 ',
            NMF_2_percent: '0.00%',
            NMF_3_date: 'yyyy/mm/dd;@', # data RRRR-MM-DD
            }
        self.xlwt = new_module_for_writing_spreadsheet()
        self.n3_style = self.prepare_cell(
            vert=self.xlwt.Alignment.VERT_CENTER,
            horz=self.xlwt.Alignment.HORZ_CENTER,
            wrap=1,
            ) # Zawijaj tekst, wycentruj
        # Liczby nieujemne na czerwono, użyj separatora 1000
        self.n5_style = self.prepare_cell(14) # Arial 14 pt
        self.n6_style = self.prepare_cell(12, bold=1) # Arial 12 pt, bold
        self.n7_style = self.prepare_cell(
            vert=self.xlwt.Alignment.VERT_CENTER,
            horz=self.xlwt.Alignment.HORZ_CENTER,
            ) # Center vertically, center horizontally
        self.n8_style = self.prepare_cell(
            vert=self.xlwt.Alignment.VERT_CENTER,
            horz=self.xlwt.Alignment.HORZ_CENTER,
            borders=nf_kw.brd_1_obk,
            ) # Center vertically, center horizontally, simple borders
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
        self.style_map = {
            ng_kw.NVB_3_STYLE: self.n3_style,
            ng_kw.NVB_6_STYLE: self.n6_style,
            ng_kw.NVB_7_STYLE: self.n7_style,
            ng_kw.NVB_8_STYLE: self.n8_style,
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

    def write_unicode(self, m_coor, the_content, style=None):
        '''
        WriterGateway:
        '''
        dc_style = calculate_style(style)
        if m_coor.is_one():
            r1, c1 = m_coor.wyznacz_dwa()
            self.sheet.write(r1, c1, the_content, **dc_style)
        else:
            r1, r2, c1, c2 = m_coor.wyznacz_cztery()
            self.sheet.write_merge(r1, r2, c1, c2, the_content, **dc_style)

    def convert_from_sel(self, style_sel):
        '''
        WriterGateway:
        '''
        return self.style_map[style_sel]

    def write_l_unicode(self, m_coor, the_content, style_sel):
        '''
        WriterGateway:
        '''
        style = self.convert_from_sel(style_sel)
        self.write_unicode(m_coor, the_content, style)

    def write_utf(self, m_coor, napis, style=None):
        '''
        WriterGateway:
        '''
        the_content = en_kw.utf_to_unicode(napis)
        self.write_unicode(m_coor, the_content, style)

    def write_l_utf(self, m_coor, napis, style_sel):
        '''
        WriterGateway:
        '''
        style = self.convert_from_sel(style_sel)
        self.write_utf(m_coor, napis, style)

    def zapisz_polaczone_komorki(self, akt_wiersz, akt_kolumna, napis, style, liczba_kolumn=1):
        '''
        WriterGateway:
        '''
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna, liczba_kolumn)
        self.write_utf(m_coor, napis, style)

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

    def zapisz_co_flt(self, m_coor, the_content, kl_miejsc=2, size=None, bold=None, rn_colour=None, borders=None, italic=None, fore_colour=None):
        '''
        WriterGateway:
        '''
        the_style = self.get_or_generate_number_style(kl_miejsc=kl_miejsc, bold=bold, size=size, rn_colour=rn_colour, borders=borders, italic=italic, fore_colour=fore_colour)
        self.write_unicode(m_coor, the_content, the_style)

    def zapisz_rn_flt(self, akt_wiersz, akt_kolumna, rn_liczba):
        '''
        WriterGateway:
        '''
        liczba = rn_liczba.rn_value
        kl_miejsc = rn_liczba.rn_after
        bold = 0
        size = None
        the_style = self.get_or_generate_number_style(kl_miejsc=kl_miejsc, rn_colour=rn_liczba.rn_colour, bold=bold, size=size)
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna)
        self.write_unicode(m_coor, liczba, the_style)

    def zapisz_date(self, akt_wiersz, akt_kolumna, liczba, italic=None, fore_colour=None):
        '''
        WriterGateway:
        '''
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna)
        the_style = self.get_or_generate_number_style(kl_miejsc=NMF_3_date, italic=italic, fore_colour=fore_colour)
        self.write_unicode(m_coor, liczba, the_style)

    def zapisz_wzor(self, m_coor, tekst_wzoru, kl_miejsc=2, size=None, bold=None, rn_colour=None, borders=None):
        '''
        WriterGateway:
        '''
        the_content = self.xlwt.Formula(tekst_wzoru)
        self.zapisz_co_flt(m_coor, the_content, kl_miejsc, size, bold, rn_colour=rn_colour, borders=borders)

    def zapisz_nazwe_miesiaca(self, akt_wiersz, nr_mies):
        '''
        WriterGateway:
        '''
        akt_kolumna = 0
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna, liczba_wierszy=liczba_wierszy)
        self.write_utf(m_coor, dn_kw.tab_miesiecy[nr_mies - 1])

    def ustaw_sam_styl(self, akt_wiersz, akt_kolumna, kl_miejsc=2, rn_colour=None, bold=0, size=None, tresc_napisu=None):
        '''
        WriterGateway:
        '''
        the_style = self.get_or_generate_number_style(kl_miejsc=kl_miejsc, rn_colour=rn_colour, bold=bold, size=size)
        m_coor = to_kw.MergedCoords(akt_wiersz, akt_kolumna)
        self.write_unicode(m_coor, tresc_napisu, style=the_style)

    def napis_ze_stylem(self, m_coor, tresc_napisu=None, rn_colour=None, bold=0, size=None, wrap=None, middle=None, kl_none=None, italic=None, fore_colour=None):
        '''
        WriterGateway:
        '''
        the_style = self.get_or_generate_style(rn_colour, bold, size, wrap, middle, kl_none, italic=italic, fore_colour=fore_colour)
        self.write_utf(m_coor, tresc_napisu, style=the_style)

    def napis_ze_wsp(self, row, col, tresc_napisu=None, bold=None, rn_colour=None, italic=None, fore_colour=None, middle=None):
        '''
        WriterGateway:
        '''
        m_coor = to_kw.MergedCoords(row, col)
        self.napis_ze_stylem(m_coor, tresc_napisu, bold=bold, rn_colour=rn_colour, italic=italic, fore_colour=fore_colour, middle=middle)

    def wymus_szerokosci(self, lista_rozmiarow):
        '''
        WriterGateway:
        '''
        for nr_kol, szer_kol in enumerate(lista_rozmiarow):
            skalowana_szerokosc = lista_rozmiarow[nr_kol]
            self.sheet.col(nr_kol).width = skalowana_szerokosc

    def szerokosc_kolumn_kosztow_energii(self):
        '''
        WriterGateway:
        '''
        lista_rozmiarow = (
            [2740 # 10
            ] + 3 * [2902 # 10,57
            ] + 11 * [3255 # 12
            ]) # Rozmiary podawane przez MS Excel
        self.wymus_szerokosci(lista_rozmiarow)

class TestArkuszowy(unittest.TestCase):
    def test_arkuszowy(self):
        '''
        TestArkuszowy:
        '''
        self.assertEqual(calculate_style(None), {})
        self.assertEqual(calculate_style(1), {'style':1})
