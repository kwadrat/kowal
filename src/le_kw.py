#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fz_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def dq_object_key(dfb, under_name):
    db_statement = fz_kw.ptn_object_key(under_name)
    return dfb.query_dct(db_statement)

def dq_entry_already_inserted(dfb, n_table, key_object, row_date, my_hour):
    db_statement = fz_kw.ptn_entry_already_inserted(n_table, key_object, row_date)
    return dfb.query_dct(db_statement)

def dq_insert_energy_entry(dfb, n_table, key_object, row_date, my_hour, value):
    db_statement = fz_kw.ptn_insert_energy_entry(n_table, key_object, row_date, my_hour, value)
    dfb.query_silent(db_statement)

def dq_load_from_db(dfb, table_name):
    db_statement = fz_kw.ptn_load_from_db(table_name)
    return dfb.query_dct(db_statement)

def dq_add_new_object_key(dfb, under_name):
    db_statement = fz_kw.ptn_add_new_object_key(under_name)
    return dfb.query_dct(db_statement)

def dq_insert_vector_of_samples(dfb, n_table, key_object, row_date, all_samples):
    db_statement = fz_kw.ptn_insert_vector_of_samples(n_table, key_object, row_date, all_samples)
    dfb.query_silent(db_statement)
