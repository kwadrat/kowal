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
    import xlrd
    return xlrd

def check_module_dependencies_linux():
    new_module_for_reading_spreadsheet()

def verify_for_equal(tmp_text, expected):
    if tmp_text != expected:
        raise RuntimeError('tmp_text = %s' % repr(tmp_text))

def locate_object_key(dfb, under_name):
    key_object = dfb.query_dct("select k_object from uu_object where account='%(under_name)s';" % dict(
        under_name=under_name,
        ))
    if not key_object:
        key_object = dfb.query_dct("insert into uu_object (account) values ('%(under_name)s') returning k_object;" % dict(
            under_name=under_name,
            ))
    ret_size = len(key_object)
    if ret_size == 1:
        key_object = key_object[0]['k_object'];
    else:
        raise RuntimeError('ret_size = %d' % ret_size)
    return key_object

def entry_already_inserted(dfb, n_table, key_object, row_date, my_hour):
    return dfb.query_dct("select * from %(n_table)s where f_object=%(f_object)d and m_date='%(m_date)s' and m_time='%(m_time)s';" % dict(
        n_table=n_table,
        f_object=key_object,
        m_date=row_date,
        m_time=my_hour,
        ))

def insert_energy_entry(dfb, n_table, key_object, row_date, my_hour, value):
    dfb.query_silent("insert into %(n_table)s (f_object, m_date, m_time, m_value) values (%(f_object)d, '%(m_date)s', '%(m_time)s', %(m_value)f);" % dict(
        n_table=n_table,
        f_object=key_object,
        m_date=row_date,
        m_time=my_hour,
        m_value=value,
        ))

class CommonReader:
    pass
