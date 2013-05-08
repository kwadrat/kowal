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

def dq_entry_already_inserted(dfb, n_table, key_object, row_date):
    db_statement = fz_kw.ptn_entry_already_inserted(n_table, key_object, row_date)
    return dfb.query_dct(db_statement)

def dq_load_from_db(dfb, table_name):
    db_statement = fz_kw.ptn_load_from_db(table_name)
    return dfb.query_dct(db_statement)

def dq_add_new_object_key(dfb, under_name):
    db_statement = fz_kw.ptn_add_new_object_key(under_name)
    return dfb.query_dct(db_statement)

def dq_insert_vector_of_samples(dfb, n_table, key_object, row_date, all_samples):
    db_statement = fz_kw.ptn_insert_vector_of_samples(n_table, key_object, row_date, all_samples)
    dfb.query_silent(db_statement)

def dq_update_vector_of_samples(dfb, n_table, sample_key, key_object, row_date, all_samples):
    db_statement = fz_kw.ptn_update_vector_of_samples(n_table, sample_key, key_object, row_date, all_samples)
    dfb.query_silent(db_statement)

def dq_load_one_vector_from_db(dfb, table_name, key_object, row_date):
    db_statement = fz_kw.ptn_load_one_vector_from_db(table_name, key_object, row_date)
    return dfb.query_dct(db_statement)

def dq_liczniki_poboru_w_roku(dfb):
    db_statement = fz_kw.ptn_liczniki_poboru_w_roku()
    return dfb.query_dct(db_statement)

def dq_jeden_licznik_poboru_w_roku(dfb):
    db_statement = fz_kw.ptn_jeden_licznik_poboru_w_roku()
    return dfb.query_dct(db_statement)
