#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fz_kw

def dq_object_key(dfb, under_name):
    db_statement = fz_kw.ptn_object_key(under_name)
    return dfb.query_dct(db_statement)

def dq_entry_already_inserted(dfb, n_table, key_object, row_date):
    db_statement = fz_kw.ptn_entry_already_inserted(n_table, key_object, row_date)
    return dfb.query_dct(db_statement)

def dq_load_from_db(dfb, table_name, id_obiekt=None, my_start_date=None, my_end_date=None):
    db_statement = fz_kw.ptn_load_from_db(
        table_name,
        id_obiekt=id_obiekt,
        my_start_date=my_start_date,
        my_end_date=my_end_date,
        )
    return dfb.query_dct(db_statement)

def dq_add_new_object_key(dfb, under_name):
    db_statement = fz_kw.ptn_add_new_object_key(under_name)
    return dfb.query_dct(db_statement)

def dq_insert_vector_of_samples(dfb, n_table, key_object, row_date, all_samples, v_none, v_zero, v_sum):
    db_statement = fz_kw.ptn_insert_vector_of_samples(n_table, key_object, row_date, all_samples, v_none, v_zero, v_sum)
    dfb.query_silent(db_statement)

def dq_update_vector_of_samples(dfb, n_table, key_object, row_date, all_samples, v_none, v_zero, v_sum, sample_key):
    db_statement = fz_kw.ptn_update_vector_of_samples(n_table, key_object, row_date, all_samples, v_none, v_zero, v_sum, sample_key)
    dfb.query_silent(db_statement)

def dq_update_stats_of_samples(dfb, n_table, v_none, v_zero, v_sum, sample_key):
    db_statement = fz_kw.ptn_update_stats_of_samples(n_table, v_none, v_zero, v_sum, sample_key)
    dfb.query_silent(db_statement)

def dq_liczniki_poboru_w_dniu(dfb, table_name, id_obiekt, tvk_data):
    db_statement = fz_kw.ptn_liczniki_poboru_w_dniu(table_name, id_obiekt, tvk_data)
    return dfb.query_dct(db_statement)

def dq_liczniki_poboru_w_miesiacu(dfb, table_name, id_obiekt, my_start_date, my_end_date):
    db_statement = fz_kw.ptn_liczniki_poboru_w_miesiacu(table_name, id_obiekt, my_start_date, my_end_date)
    return dfb.query_dct(db_statement)

def dq_dane_jednego_obiektu(dfb, table_name, key_object):
    db_statement = fz_kw.ptn_dane_jednego_obiektu(table_name, key_object)
    return dfb.query_dct(db_statement)

def dq_liczniki_poboru_w_roku(dfb, table_name, id_obiekt, my_start_year):
    db_statement = fz_kw.ptn_liczniki_poboru_w_roku(table_name, id_obiekt, my_start_year)
    return dfb.query_dct(db_statement)

def dq_for_statistics(dfb, table_name):
    db_statement = fz_kw.ptn_for_statistics(table_name)
    return dfb.query_dct(db_statement)

def dq_get_ordered_objects(dfb):
    db_statement = fz_kw.ptn_get_ordered_objects()
    return dfb.query_dct(db_statement)
