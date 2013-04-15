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
        return self.sheet.cell(my_row - 1, my_col).value

    def check_for_constant_string(self, my_col, my_row, expected):
        '''
        DataReader:
        '''
        tmp_text = self.sheet.cell(my_row - 1, my_col).value
        if tmp_text != expected:
            raise RuntimeError('tmp_text = %s' % repr(tmp_text))

    def analyze_this_sheet(self):
        '''
        DataReader:
        '''
        nrows = self.sheet.nrows
        header_col = fv_kw.vx_zero.vx_lt('A')
        self.check_for_constant_string(header_col, nrows, u'Suma')
        self.check_for_constant_string(header_col, nrows - 1, u'Data')
        self.check_for_constant_string(header_col, nrows - 2, u'Maksimum')
        self.check_for_constant_string(header_col, 6, u'Data')
        data_rows = xrange(7, nrows - 2)
        print data_rows

    def analyze_this_file(self, xlrd, single_file):
        '''
        DataReader:
        '''
        book = xlrd.open_workbook(single_file)
        numer_of_sheets = book.nsheets
        if numer_of_sheets == 1:
            self.sheet = book.sheet_by_name(u'Report')
            self.analyze_this_sheet()
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

def analyze_excel_files(filenames):
    xlrd = new_module_for_reading_spreadsheet()
    for single_file in filenames:
        obk = DataReader()
        obk.analyze_this_file(xlrd, single_file)
