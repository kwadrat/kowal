#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
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

def ptn_entry_already_inserted(n_table, key_object, row_date, my_hour):
    return fy_kw.lxa_10_inst % dict(
        n_table=n_table,
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        e_date=lc_kw.fq_m_date_qv,
        m_date=row_date,
        e_time=lc_kw.fq_m_time_qv,
        m_time=my_hour,
        )

def ptn_insert_energy_entry(n_table, key_object, row_date, my_hour, value):
    return fy_kw.lxa_12_inst % dict(
        n_table=n_table,
        e_object=lc_kw.fq_f_object_qv,
        f_object=key_object,
        e_date=lc_kw.fq_m_date_qv,
        m_date=row_date,
        e_time=lc_kw.fq_m_time_qv,
        m_time=my_hour,
        e_value=lc_kw.fq_m_value_qv,
        m_value=value,
        )

def ptn_load_from_db(table_name):
    return fy_kw.lxa_14_inst % dict(
        table_name=table_name,
        uu_object=lc_kw.fq_uu_object_qv,
        account=lc_kw.fq_account_qv,
        e_date=lc_kw.fq_m_date_qv,
        e_time=lc_kw.fq_m_time_qv,
        e_value=lc_kw.fq_m_value_qv,
        e_object=lc_kw.fq_f_object_qv,
        k_object=lc_kw.fq_k_object_qv,
        )

def ptn_add_new_object_key(under_name):
    return fy_kw.lxa_16_inst % dict(
        under_name=under_name,
        uu_object=lc_kw.fq_uu_object_qv,
        )

class TestVariousPatterns(unittest.TestCase):
    def test_various_patterns(self):
        '''
        TestVariousPatterns:
        '''
        self.assertEqual(concatenate_index_name('t', 'f'), fy_kw.lxa_2_inst)
        self.assertEqual(index_create('a', 't', 'f'), fy_kw.lxa_3_inst)
        self.assertEqual(index_drop('a'), fy_kw.lxa_5_inst)
        self.assertEqual(ptn_object_key('abc'), fy_kw.lxa_7_inst)
        self.assertEqual(ptn_entry_already_inserted('t', 123, '2013-01-31', '23:34'), fy_kw.lxa_9_inst)
        self.assertEqual(ptn_insert_energy_entry('t', 123, '2013-01-31', '23:34', 0), fy_kw.lxa_11_inst)
        self.assertEqual(ptn_load_from_db('t'), fy_kw.lxa_13_inst)
        self.assertEqual(ptn_add_new_object_key('n'), fy_kw.lxa_15_inst)
