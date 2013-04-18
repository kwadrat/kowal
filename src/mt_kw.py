#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
import fx_kw
import lc_kw
import le_kw
import en_kw
import mu_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

CommonReader = mu_kw.CommonReader

class DataReader(CommonReader):
    def __init__(self):
        '''
        DataReader:
        '''
        CommonReader.__init__(self)

    def vx_th_date(self, my_col, my_row):
        '''
        DataReader:
        '''
        value = self.vx_date(my_col, my_row)
        size = len(value)
        if size == 6:
            last = value[5]
            if last == 0:
                my_point = datetime.datetime(*value) - datetime.timedelta(seconds=15*60)
                my_date = my_point.strftime('%Y.%m.%d')
                my_time = my_point.strftime('%H:%M')
                return my_date, my_time
            else:
                raise RuntimeError('last = %s' % repr(last))
        else:
            raise RuntimeError('size = %d' % size)

    def detect_sheet_header(self):
        '''
        DataReader:
        '''
        self.check_for_constant_string('B', 2, u'TAURON Dystrybucja S.A. Oddział Gliwice - Raport 15-minutowy')
        self.check_for_constant_string('B', 3, u'Name')
        self.check_for_constant_string('B', 4, u'Account')
        self.check_for_constant_string('B', 5, u'Address')
        self.check_for_constant_string('B', 6, u'Start Time')
        self.check_for_constant_string('B', 7, u'End Time ')
        self.check_for_constant_string('B', 8, u'Report Time')
        self.check_for_constant_string('C', 12, u'kW')
        under_name = self.vx_peek('C', 10)
        tmp_format = 'under_name'; print 'Eval:', tmp_format, eval(tmp_format)
        return under_name

    def detect_data_rows(self):
        '''
        DataReader:
        '''
        nrows = self.sheet.nrows
        self.check_for_constant_string('B', 10, u'Data')
        self.check_for_constant_string('B', 12, u'rrrr-mm-dd hh:mm')
        self.check_for_constant_string('B', nrows - 2, u'Energy')
        self.check_for_constant_string('B', nrows - 1, u'Max')
        self.check_for_constant_string('B', nrows, u'Time Max')
        return xrange(13, nrows - 2)

    def fetch_field(self, dfb, key_object, single_row, duo_date):
        '''
        DataReader:
        '''
        row_date, my_hour = duo_date
        if not le_kw.dq_entry_already_inserted(dfb, lc_kw.fq_uu_power_qv, key_object, row_date, my_hour):
            value = self.vx_peek('C', single_row)
            le_kw.dq_insert_energy_entry(dfb, lc_kw.fq_uu_power_qv, key_object, row_date, my_hour, value)

    def enter_data(self, dfb, key_object, data_rows):
        '''
        DataReader:
        '''
        for single_row in data_rows:
            duo_date = self.vx_th_date('B', single_row)
            self.fetch_field(dfb, key_object, single_row, duo_date)

    def analyze_this_sheet(self, dfb):
        '''
        DataReader:
        '''
        under_name = self.detect_sheet_header()
        key_object = mu_kw.locate_object_key(dfb, under_name)
        data_rows = self.detect_data_rows()
        self.enter_data(dfb, key_object, data_rows)
        print data_rows

    def analyze_this_file(self, dfb, xlrd, single_file):
        '''
        DataReader:
        '''
        self.xlrd = xlrd
        self.book = self.xlrd.open_workbook(single_file)
        numer_of_sheets = self.book.nsheets
        if numer_of_sheets == 1:
            self.sheet = self.book.sheet_by_name(u'Report')
            self.analyze_this_sheet(dfb)
        else:
            raise RuntimeError('numer_of_sheets = %d' % numer_of_sheets)

def analyze_excel_files(dfb, filenames):
    xlrd = mu_kw.new_module_for_reading_spreadsheet()
    for single_file in filenames:
        obk = DataReader()
        obk.analyze_this_file(dfb, xlrd, single_file)

def unique_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field], dane_bazy)))
    object_names.sort()
    return object_names
