#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
import fx_kw
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

def insert_energy_entry(dfb, key_object, row_date, my_hour, value):
    dfb.query_silent("insert into uu_power (f_object, m_date, m_time, m_value) values (%(f_object)d, '%(m_date)s', '%(m_time)s', %(m_value)f);" % dict(
        f_object=key_object,
        m_date=row_date,
        m_time=my_hour,
        m_value=value,
        ))

class DataReader:
    def __init__(self):
        '''
        DataReader:
        '''
        self.vx_zero = fv_kw.vx_zero
        self.day_zero = (0, 0, 0)

    def vx_num_peek(self, my_col, my_row):
        '''
        DataReader:
        '''
        return self.sheet.cell_value(my_row - 1, my_col)

    def vx_letter_num(self, my_col):
        '''
        DataReader:
        '''
        return self.vx_zero.vx_lt(my_col)

    def vx_peek(self, my_col, my_row):
        '''
        DataReader:
        '''
        header_col = self.vx_letter_num(my_col)
        return self.vx_num_peek(header_col, my_row)

    def vx_date(self, my_col, my_row):
        '''
        DataReader:
        '''
        value = self.vx_peek(my_col, my_row)
        return self.xlrd.xldate_as_tuple(value, self.book.datemode)

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

    def vx_num_time(self, my_col, my_row):
        '''
        DataReader:
        '''
        value = self.vx_num_peek(my_col, my_row)
        time_tuple = self.xlrd.xldate_as_tuple(value, self.book.datemode)
        day_part = time_tuple[:3]
        time_part = time_tuple[3:]
        mu_kw.verify_for_equal(day_part, self.day_zero)
        return datetime.time(*time_part).strftime('%H:%M')

    def check_for_constant_string(self, my_col, my_row, expected):
        '''
        DataReader:
        '''
        tmp_text = self.vx_peek(my_col, my_row)
        mu_kw.verify_for_equal(tmp_text, expected)

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
        if not mu_kw.entry_already_inserted(dfb, 'uu_power', key_object, row_date, my_hour):
            value = self.vx_peek('C', single_row)
            insert_energy_entry(dfb, key_object, row_date, my_hour, value)

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

def load_from_db(dfb, table_name):
    return dfb.query_dct("select uu_object.account,m_date,m_time,m_value from %(table_name)s,uu_object where %(table_name)s.f_object=uu_object.k_object;" % dict(
        table_name=table_name,
        ))

def unique_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field], dane_bazy)))
    object_names.sort()
    return object_names

def unique_a_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field][:5], dane_bazy)))
    object_names.sort()
    return object_names

dict_names = {
    'GIMNAZJUM_NR_7_RYBNIK_SZTOLNIOWA': 'G-7',
    'SZKOLA_PODST_NR_11_RYBNIK_HIBNERA': 'SP-11',
    'SZKOLA_PODSTAWOWA_NR_13_CHWALOWICE': 'SP-13',
    'SZKOLA_PODSTAWOWA_NR_20_RYBNIK_ZIOLOWA': 'SP-20',
    'SZKOLA_PODSTAWOWA_NR_28_RYBNIK_SZEWCZYKA': 'SP-28',
    'SZKOLA_PODST_NR_3_RYBNIK_WOLNA': 'SP-3',
    'SZKOLA_PODSTAWOWA_NR_37_RYBNIK': 'SP-37',
    'ZESPOL_SZKOL_EKON_USLUG_RYBNIK': 'ZSE-U',
    'ZESPOL_SZKOL_TECHNICZNYCH_RYBNIK_KOSCIUSZKI': 'ZST',
    'ZESPOL_SZKOLNO_PRZEDSZK_WIELOPOLE': 'ZSz-P W.',
    'SZKOLA_MUZYCZNA_RYBNIK': 'PSM',
    }

def generate_dates_vertically(sheet, all_dates):
    for nr, one_date in enumerate(all_dates):
        row = nr + 1
        col = 0
        sheet.write(row, col, one_date)

def generate_hours_horizontally(sheet, all_hours):
    for nr, one_hour in enumerate(all_hours):
        row = 0
        col = nr + 1
        sheet.write(row, col, one_hour)

def generate_one_file(xlwt, dfb, table_name, output_file):
    dane_bazy = load_from_db(dfb, table_name)
    object_names = unique_sorted(dane_bazy, 'account')
    wbk = xlwt.Workbook()
    for nr, name in enumerate(object_names):
        tmp_format = 'name'; print 'Eval:', tmp_format, eval(tmp_format)
        sheet = wbk.add_sheet(dict_names[name])
        selected_data = filter(lambda x: x['account'] == name, dane_bazy)
        all_dates = unique_sorted(selected_data, 'm_date')
        all_hours = unique_a_sorted(selected_data, 'm_time')
        generate_dates_vertically(sheet, all_dates)
        generate_hours_horizontally(sheet, all_hours)
        for my_data in selected_data:
            my_time = my_data['m_time'][:5]
            row = all_dates.index(my_data['m_date']) + 1
            col = all_hours.index(my_time) + 1
            sheet.write(row, col, my_data['m_value'])
    wbk.save(output_file)

def generate_excel_files(dfb):
    import xlwt
    generate_one_file(xlwt, dfb, 'uu_energy', 'e.xls')
    generate_one_file(xlwt, dfb, 'uu_power', 'p.xls')
