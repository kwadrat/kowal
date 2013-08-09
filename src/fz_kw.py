#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import dv_kw
import hj_kw
import ln_kw
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

def ptn_entry_already_inserted(n_table, key_object, row_date):
    return fy_kw.lxa_10_inst % dict(
        n_table=n_table,
        e_fields=hj_kw.ls_przec(lc_kw.fq_k_sample_qv, lc_kw.fq_f_object_qv, lc_kw.fq_m_date_qv, lc_kw.fq_m_samples_qv),
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        e_date=lc_kw.fq_m_date_qv,
        m_date=row_date,
        )

def ptn_load_from_db(table_name):
    return fy_kw.lxa_14_inst % dict(
        table_name=table_name,
        uu_object=lc_kw.fq_uu_object_qv,
        account=lc_kw.fq_account_qv,
        e_date=lc_kw.fq_m_date_qv,
        e_samples=lc_kw.fq_m_samples_qv,
        e_object=lc_kw.fq_f_object_qv,
        k_object=lc_kw.fq_k_object_qv,
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

def ptn_load_one_vector_from_db(table_name, key_object, row_date):
    return fy_kw.lxa_31_inst % dict(
        table_name=table_name,
        e_date=lc_kw.fq_m_date_qv,
        e_samples=lc_kw.fq_m_samples_qv,
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        m_date=row_date,
        )

def ptn_liczniki_poboru_w_roku(table_name, id_obiekt, tvk_data):
    return fy_kw.lxa_32_inst % dict(
        table_name=table_name,
        id_obiekt=id_obiekt,
        tvk_data=tvk_data,
        )

def ptn_jeden_licznik_poboru_w_roku(table_name, nr_probki):
    return fy_kw.lxa_34_inst % dict(
        table_name=table_name,
        nr_probki=nr_probki,
        )

def ptn_dane_jednego_obiektu(table_name, key_object):
    return fy_kw.lxa_39_inst % dict(
        table_name=table_name,
        e_date=lc_kw.fq_m_date_qv,
        e_none=lc_kw.fq_m_none_qv,
        e_zero=lc_kw.fq_m_zero_qv,
        e_sum=lc_kw.fq_m_sum_qv,
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        )

class ConsumptionQry(object):
    def __init__(self):
        '''
        ConsumptionQry:
        '''

    def cons_question(self):
        '''
        ConsumptionQry:
        '''
        table_name = lc_kw.fq_uu_energy_qv
        key_object = 7
        return fy_kw.lxa_39_inst % dict(
            table_name=table_name,
            e_date=lc_kw.fq_m_date_qv,
            e_none=lc_kw.fq_m_none_qv,
            e_zero=lc_kw.fq_m_zero_qv,
            e_sum=lc_kw.fq_m_sum_qv,
            e_object=lc_kw.fq_f_object_qv,
            f_object=key_object,
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
        self.assertEqual(ptn_add_new_object_key('n'), fy_kw.lxa_15_inst)
        self.assertEqual(ptn_insert_vector_of_samples(lc_kw.fq_uu_power_qv, 123, '2013-01-31', [None, 0, 0, 1.5, 2.5, 3], 1, 2, 7.0), fy_kw.lxa_17_inst)
        self.assertEqual(ptn_update_vector_of_samples(lc_kw.fq_uu_power_qv, 123, '2013-01-31', [None, 0, 0, 1.5, 2.5, 3], 1, 2, 7.0, 8), fy_kw.lxa_21_inst)
        self.assertEqual(ptn_update_stats_of_samples(lc_kw.fq_uu_power_qv, 1, 2, 7.0, 8), fy_kw.lxa_50_inst)
        self.assertEqual(ptn_load_one_vector_from_db(lc_kw.fq_uu_power_qv, 18, '2013-01-31'), fy_kw.lxa_30_inst)
        self.assertEqual(ptn_liczniki_poboru_w_roku(lc_kw.fq_uu_power_qv, 18, '2013-01-31'), fy_kw.lxa_33_inst)
        self.assertEqual(ptn_liczniki_poboru_w_roku(lc_kw.fq_uu_energy_qv, 19, '2013-02-01'), fy_kw.lxa_36_inst)
        self.assertEqual(ptn_jeden_licznik_poboru_w_roku(lc_kw.fq_uu_power_qv, 1860), fy_kw.lxa_35_inst)
        self.assertEqual(ptn_jeden_licznik_poboru_w_roku(lc_kw.fq_uu_energy_qv, 1861), fy_kw.lxa_37_inst)
        self.assertEqual(ptn_dane_jednego_obiektu(lc_kw.fq_uu_energy_qv, 7), fy_kw.lxa_38_inst)

    def test_2_various_patterns(self):
        '''
        TestVariousPatterns:
        '''
        obk = ConsumptionQry()
        odp = obk.cons_question()
        self.assertEqual(odp, fy_kw.lxa_38_inst)
