#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import le_kw
import mu_kw
import mt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
    dane_bazy = le_kw.dq_load_from_db(dfb, table_name)
    object_names = mt_kw.unique_sorted(dane_bazy, 'account')
    wbk = xlwt.Workbook()
    for nr, name in enumerate(object_names):
        tmp_format = 'name'; print 'Eval:', tmp_format, eval(tmp_format)
        sheet = wbk.add_sheet(mt_kw.dict_names[name])
        selected_data = filter(lambda x: x['account'] == name, dane_bazy)
        all_dates = mt_kw.unique_sorted(selected_data, 'm_date')
        all_hours = mt_kw.unique_a_sorted(selected_data, 'm_time')
        generate_dates_vertically(sheet, all_dates)
        generate_hours_horizontally(sheet, all_hours)
        for my_data in selected_data:
            my_time = my_data['m_time'][:5]
            row = all_dates.index(my_data['m_date']) + 1
            col = all_hours.index(my_time) + 1
            sheet.write(row, col, my_data['m_value'])
    wbk.save(output_file)

def generate_excel_files(dfb):
    xlwt = mu_kw.new_module_for_writing_spreadsheet()
    generate_one_file(xlwt, dfb, lc_kw.fq_uu_energy_qv, 'e.xls')
    generate_one_file(xlwt, dfb, lc_kw.fq_uu_power_qv, 'p.xls')
