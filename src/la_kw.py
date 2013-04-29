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

def generate_one_file(xlwt, dfb, worker_class, table_name, output_file):
    dane_bazy = le_kw.dq_load_from_db(dfb, table_name)
    object_names = mu_kw.unique_sorted(dane_bazy, lc_kw.fq_account_qv)
    wbk = xlwt.Workbook()
    for nr, name in enumerate(object_names):
        tmp_format = 'name'; print 'Eval:', tmp_format, eval(tmp_format)
        sheet = wbk.add_sheet(mu_kw.dict_names[name])
        selected_data = filter(lambda x: x[lc_kw.fq_account_qv] == name, dane_bazy)
        all_dates = mu_kw.unique_sorted(selected_data, lc_kw.fq_m_date_qv)
        all_hours = mu_kw.unique_a_sorted(selected_data, lc_kw.fq_m_time_qv)
        mu_kw.generate_dates_vertically(sheet, all_dates)
        mu_kw.generate_hours_horizontally(sheet, all_hours)
        for my_data in selected_data:
            my_time = my_data[lc_kw.fq_m_time_qv][:5]
            row = all_dates.index(my_data[lc_kw.fq_m_date_qv]) + 1
            col = all_hours.index(my_time) + 1
            sheet.write(row, col, my_data[lc_kw.fq_m_value_qv])
    wbk.save(output_file)

def generate_excel_files(dfb):
    xlwt = mu_kw.new_module_for_writing_spreadsheet()
    mu_kw.generate_one_file(xlwt, dfb, fu_kw.EnergyReader, lc_kw.fq_uu_energy_qv, 'e.xls')
    mu_kw.generate_one_file(xlwt, dfb, mt_kw.PowerReader, lc_kw.fq_uu_power_qv, 'p.xls')

def analyze_excel_files(dfb, worker_class, filenames):
    xlrd = mu_kw.new_module_for_reading_spreadsheet()
    for single_file in filenames:
        print single_file
        obk = worker_class()
        obk.analyze_this_file(dfb, xlrd, single_file)
