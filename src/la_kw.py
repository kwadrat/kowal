#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import le_kw
import mu_kw
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
    'LICEUM_OGOLNOKSZT_NR_1_RYBNIK': 'ZS-1',
    'II_LO_RYBNIK_MIKOLOWSKA': 'ZS-2',
    'IV_LICEUM_OGOLNOKSZTALCACE_W_RYBNIKU': 'IV-LO',
    'SZKOLA_PODSTAWOWA_NR34_RYBNIK_REYMONTA': 'SP-34',
    'SZKOLA_PODSTAWOWA_NR_35_RYBNIK_SLASKA': 'SP-35',
    'URZAD_MIASTA_RYBNIK_SEK1': 'UM-S1',
    'URZAD_MIASTA_RYBNIK_SEK2': 'UM-S2',
    'URZAD_MIASTA_RYBNIK_ZAMKOWA': 'UM-Z',
    'ZESPOL_SZKOL_RYBNIK_SWIERKLANSKA': 'ZSB',
    }

def unique_a_sorted(dane_bazy, field):
    object_names = list(set(map(lambda x: x[field][:5], dane_bazy)))
    object_names.sort()
    return object_names

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

def generate_one_file(xlwt, dfb, worker_class, table_name, output_file):
    dane_bazy = le_kw.dq_load_from_db(dfb, table_name)
    object_names = mu_kw.unique_sorted(dane_bazy, lc_kw.fq_account_qv)
    wbk = xlwt.Workbook()
    for nr, name in enumerate(object_names):
        tmp_format = 'name'; print 'Eval:', tmp_format, eval(tmp_format)
        sheet = wbk.add_sheet(dict_names[name])
        selected_data = filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy)
        all_dates = mu_kw.unique_sorted(selected_data, lc_kw.fq_m_date_qv)
        all_hours = unique_a_sorted(selected_data, lc_kw.fq_m_time_qv)
        generate_dates_vertically(sheet, all_dates)
        generate_hours_horizontally(sheet, all_hours)
        for my_data in selected_data:
            my_time = my_data[lc_kw.fq_m_time_qv][:5]
            row = all_dates.index(my_data[lc_kw.fq_m_date_qv]) + 1
            col = all_hours.index(my_time) + 1
            sheet.write(row, col, my_data[lc_kw.fq_m_value_qv])
    wbk.save(output_file)

def generate_excel_files(dfb):
    xlwt = mu_kw.new_module_for_writing_spreadsheet()
    generate_one_file(xlwt, dfb, fu_kw.EnergyReader, lc_kw.fq_uu_energy_qv, 'e.xls')
    generate_one_file(xlwt, dfb, mt_kw.PowerReader, lc_kw.fq_uu_power_qv, 'p.xls')

def analyze_excel_files(dfb, worker_class, filenames):
    xlrd = mu_kw.new_module_for_reading_spreadsheet()
    for single_file in filenames:
        print single_file
        obk = worker_class()
        obk.analyze_this_file(dfb, xlrd, single_file)
