#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import dv_kw
import ln_kw
import dn_kw
import lr_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def concatenate_index_name(table, field):
    return '%(table)s_%(field)s_index' % dict(
        table=table,
        field=field,
        )

def index_create(name, table, field):
    return fy_kw.lxa_4_inst % dict(
        name=name,
        table=table,
        field=field,
        )

def index_drop(name):
    return fy_kw.lxa_6_inst % dict(
        name=name,
        )

def process_indices(table, field_names, create_flag):
    if field_names:
        for single_field in field_names:
            compound_name = concatenate_index_name(table, single_field)
            if create_flag:
                result = index_create(compound_name, table, single_field)
            else:
                result = index_drop(compound_name)
            print result

def ptn_object_key(under_name):
    return fy_kw.lxa_8_inst % dict(
        under_name=under_name,
        k_object=lc_kw.fq_k_object_qv,
        uu_object=lc_kw.fq_uu_object_qv,
        account=lc_kw.fq_account_qv,
        )

def ptn_entry_already_inserted(table_name, id_obiekt, tvk_data):
    obk = lr_kw.GeneratorUU(table_name)
    obk.set_object(id_obiekt)
    obk.set_exact_date(tvk_data)
    returned_fields = [
        lc_kw.fq_k_sample_qv,
        lc_kw.fq_f_object_qv,
        lc_kw.fq_m_date_qv,
        lc_kw.fq_m_samples_qv,
        ]
    return obk.prepare_shape(returned_fields)

def ptn_load_from_db(table_name, id_obiekt=None, my_start_date=None, my_end_date=None):
    if id_obiekt is None:
        wstawka_obkt = ''
    else:
        wstawka_obkt = ' AND %(uu_object)s.%(k_object)s=%(id_obiekt)d' % dict(
            uu_object=lc_kw.fq_uu_object_qv,
            k_object=lc_kw.fq_k_object_qv,
            id_obiekt=id_obiekt,
            )
    if my_start_date is None:
        wstawka_start = ''
    else:
        wstawka_start = " AND %(table_name)s.%(e_date)s >= '%(my_start_date)s'" % dict(
            table_name=table_name,
            e_date=lc_kw.fq_m_date_qv,
            my_start_date=my_start_date,
            )
    if my_end_date is None:
        wstawka_end = ''
    else:
        wstawka_end = " AND %(table_name)s.%(e_date)s < '%(my_end_date)s'" % dict(
            table_name=table_name,
            e_date=lc_kw.fq_m_date_qv,
            my_end_date=my_end_date,
            )
    return fy_kw.lxa_14_inst % dict(
        table_name=table_name,
        uu_object=lc_kw.fq_uu_object_qv,
        account=lc_kw.fq_account_qv,
        e_date=lc_kw.fq_m_date_qv,
        e_samples=lc_kw.fq_m_samples_qv,
        e_object=lc_kw.fq_f_object_qv,
        k_object=lc_kw.fq_k_object_qv,
        wstawka_obkt=wstawka_obkt,
        wstawka_start=wstawka_start,
        wstawka_end=wstawka_end,
        )

def ptn_add_new_object_key(under_name):
    return fy_kw.lxa_16_inst % dict(
        under_name=under_name,
        uu_object=lc_kw.fq_uu_object_qv,
        account=lc_kw.fq_account_qv,
        k_object=lc_kw.fq_k_object_qv,
        )

def ptn_insert_vector_of_samples(n_table, key_object, row_date, all_samples, v_none, v_zero, v_sum):
    return fy_kw.lxa_18_inst % dict(
        n_table=n_table,
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        e_date=lc_kw.fq_m_date_qv,
        m_date=row_date,
        e_samples=lc_kw.fq_m_samples_qv,
        m_samples=ln_kw.convert_all(all_samples),
        e_none=lc_kw.fq_m_none_qv,
        v_none=v_none,
        e_zero=lc_kw.fq_m_zero_qv,
        v_zero=v_zero,
        e_sum=lc_kw.fq_m_sum_qv,
        v_sum=v_sum,
        )

def ptn_update_vector_of_samples(n_table, key_object, row_date, all_samples, v_none, v_zero, v_sum, sample_key):
    return fy_kw.lxa_22_inst % dict(
        n_table=n_table,
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        e_date=lc_kw.fq_m_date_qv,
        m_date=row_date,
        e_samples=lc_kw.fq_m_samples_qv,
        m_samples=ln_kw.convert_all(all_samples),
        e_none=lc_kw.fq_m_none_qv,
        v_none=v_none,
        e_zero=lc_kw.fq_m_zero_qv,
        v_zero=v_zero,
        e_sum=lc_kw.fq_m_sum_qv,
        v_sum=v_sum,
        e_key_sample=lc_kw.fq_k_sample_qv,
        k_sample=sample_key,
        )

def ptn_update_stats_of_samples(n_table, v_none, v_zero, v_sum, sample_key):
    return fy_kw.lxa_51_inst % dict(
        n_table=n_table,
        e_none=lc_kw.fq_m_none_qv,
        v_none=v_none,
        e_zero=lc_kw.fq_m_zero_qv,
        v_zero=v_zero,
        e_sum=lc_kw.fq_m_sum_qv,
        v_sum=v_sum,
        e_key_sample=lc_kw.fq_k_sample_qv,
        k_sample=sample_key,
        )

def ptn_liczniki_poboru_w_dniu(table_name, id_obiekt, tvk_data):
    obk = lr_kw.GeneratorUU(table_name)
    obk.set_object(id_obiekt)
    obk.set_exact_date(tvk_data)
    return obk.final_shape()

def ptn_liczniki_poboru_w_miesiacu(table_name, id_obiekt, my_start_date, my_end_date):
    obk = lr_kw.GeneratorUU(table_name)
    obk.set_object(id_obiekt)
    obk.set_start_date(my_start_date)
    obk.set_end_date(my_end_date)
    return obk.cons_couple()

def ptn_liczniki_poboru_w_roku(table_name, id_obiekt, my_start_year):
    obk = lr_kw.GeneratorUU(table_name)
    obk.set_object(id_obiekt)
    my_start_day, my_end_day = dn_kw.ZakresRoku(my_start_year)
    my_start_date = dn_kw.NapisDnia(my_start_day)
    my_end_date = dn_kw.NapisDnia(my_end_day)
    obk.set_start_date(my_start_date)
    obk.set_end_date(my_end_date)
    return obk.cons_couple()

def ptn_dane_jednego_obiektu(table_name, key_object):
    obk = lr_kw.GeneratorUU(table_name)
    obk.set_object(key_object)
    return obk.cons_question()

def ptn_for_statistics(table_name):
    obk = lr_kw.GeneratorUU(table_name)
    return obk.samples_for_recalculating()

def ptn_get_ordered_objects():
    return fy_kw.lxa_65_inst % dict(
        k_object=lc_kw.fq_k_object_qv,
        account=lc_kw.fq_account_qv,
        uu_object=lc_kw.fq_uu_object_qv,
        )

class TestVariousPatterns(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual
    def test_various_patterns(self):
        '''
        TestVariousPatterns:
        '''
        self.assertEqual(concatenate_index_name('t', 'f'), fy_kw.lxa_2_inst)
        self.assertEqual(index_create('a', 't', 'f'), fy_kw.lxa_3_inst)
        self.assertEqual(index_drop('a'), fy_kw.lxa_5_inst)
        self.assertEqual(ptn_object_key('abc'), fy_kw.lxa_7_inst)
        self.assertEqual(ptn_entry_already_inserted(lc_kw.fq_uu_power_qv, 123, '2013-01-31'), fy_kw.lxa_9_inst)
        self.assertEqual(ptn_load_from_db(lc_kw.fq_uu_power_qv), fy_kw.lxa_13_inst)
        self.assertEqual(ptn_load_from_db(lc_kw.fq_uu_power_qv, id_obiekt=123), fy_kw.lxa_61_inst)
        self.assertEqual(
            ptn_load_from_db(
                lc_kw.fq_uu_power_qv,
                id_obiekt=123,
                my_start_date='2013-01-01',
                my_end_date='2013-02-01',
                ),
            fy_kw.lxa_62_inst
            )
        self.assertEqual(ptn_add_new_object_key('n'), fy_kw.lxa_15_inst)
        self.assertEqual(ptn_insert_vector_of_samples(lc_kw.fq_uu_power_qv, 123, '2013-01-31', [None, 0, 0, 1.5, 2.5, 3], 1, 2, 7.0), fy_kw.lxa_17_inst)
        self.assertEqual(ptn_update_vector_of_samples(lc_kw.fq_uu_power_qv, 123, '2013-01-31', [None, 0, 0, 1.5, 2.5, 3], 1, 2, 7.0, 8), fy_kw.lxa_21_inst)
        self.assertEqual(ptn_update_stats_of_samples(lc_kw.fq_uu_power_qv, 1, 2, 7.0, 8), fy_kw.lxa_50_inst)
        self.assertEqual(ptn_liczniki_poboru_w_dniu(lc_kw.fq_uu_power_qv, 18, '2013-01-31'), fy_kw.lxa_33_inst)
        self.assertEqual(ptn_liczniki_poboru_w_dniu(lc_kw.fq_uu_energy_qv, 19, '2013-02-01'), fy_kw.lxa_36_inst)
        self.assertEqual(ptn_dane_jednego_obiektu(lc_kw.fq_uu_energy_qv, 7), fy_kw.lxa_38_inst)
        self.assertEqual(ptn_liczniki_poboru_w_miesiacu(lc_kw.fq_uu_energy_qv, 19, '2013-02-01', '2013-03-01'), fy_kw.lxa_58_inst)
        self.assertEqual(ptn_liczniki_poboru_w_roku(lc_kw.fq_uu_energy_qv, 19, 2013), fy_kw.lxa_59_inst)
        self.assertEqual(ptn_for_statistics(lc_kw.fq_uu_power_qv), fy_kw.lxa_63_inst)
        self.assertEqual(ptn_get_ordered_objects(), fy_kw.lxa_64_inst)
