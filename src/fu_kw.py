#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
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

class DataReader:
    def vx_peek(self, my_col, my_row):
        '''
        DataReader:
        '''
        header_col = fv_kw.vx_zero.vx_lt(my_col)
        return self.sheet.cell_value(my_row - 1, header_col)

    def check_for_constant_string(self, my_col, my_row, expected):
        '''
        DataReader:
        '''
        tmp_text = self.vx_peek(my_col, my_row)
        if tmp_text != expected:
            raise RuntimeError('tmp_text = %s' % repr(tmp_text))

    def detect_sheet_header(self):
        '''
        DataReader:
        '''
        self.check_for_constant_string('B', 2, u'Raport energii godzinowej dla ')
        under_name = self.vx_peek('E', 2)
        tmp_format = 'under_name'; print 'Eval:', tmp_format, eval(tmp_format)
        period_start = self.vx_peek('E', 3)
        tmp_format = 'period_start'; print 'Eval:', tmp_format, eval(tmp_format)
        period_end = self.vx_peek('H', 3)
        tmp_format = 'period_end'; print 'Eval:', tmp_format, eval(tmp_format)
        self.check_for_constant_string('M', 2, u'kWh')
        self.check_for_constant_string('B', 3, u'Za okres')
        self.check_for_constant_string('D', 3, u'od')
        self.check_for_constant_string('G', 3, u'do ')

    def detect_data_rows(self):
        '''
        DataReader:
        '''
        nrows = self.sheet.nrows
        self.check_for_constant_string('A', 6, u'Data')
        self.check_for_constant_string('A', nrows - 2, u'Maksimum')
        self.check_for_constant_string('A', nrows - 1, u'Data')
        self.check_for_constant_string('A', nrows, u'Suma')
        return xrange(7, nrows - 2)

    def analyze_this_sheet(self):
        '''
        DataReader:
        '''
        self.detect_sheet_header()
        data_rows = self.detect_data_rows()
        print data_rows

    def analyze_this_file(self, xlrd, single_file):
        '''
        DataReader:
        '''
        self.book = xlrd.open_workbook(single_file)
        numer_of_sheets = self.book.nsheets
        if numer_of_sheets == 1:
            self.sheet = self.book.sheet_by_name(u'Report')
            self.analyze_this_sheet()
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

def analyze_excel_files(filenames):
    xlrd = new_module_for_reading_spreadsheet()
    for single_file in filenames:
        obk = DataReader()
        obk.analyze_this_file(xlrd, single_file)
