#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import sf_iw_kw
import dv_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class GeneratorUU(object):
    def __init__(self, my_table_name):
        '''
        GeneratorUU:
        '''
        self.my_place = None
        self.my_start_date = None
        self.my_end_date = None
        self.my_week_day = None
        self.my_table_name = my_table_name

    def final_shape(self):
        '''
        GeneratorUU:
        '''
        all_my_limits = []
        if self.my_place is not None:
            all_my_limits.append('f_object=%d' % self.my_place)
        if self.my_start_date is not None:
            all_my_limits.append("m_date >= '2013-03-11'")
        if self.my_end_date is not None:
            all_my_limits.append("m_date < '2013-03-25'")
        if self.my_week_day is not None:
            all_my_limits.append("EXTRACT(dow FROM m_date)=%d" % self.my_week_day)
        part_my_limits = ' AND '.join(all_my_limits)
        return fy_kw.lxa_23_inst % dict(
            part_my_limits=part_my_limits,
            my_table_name=self.my_table_name,
            )

    def set_place(self, my_place):
        '''
        GeneratorUU:
        '''
        self.my_place = my_place

    def set_start_date(self, my_start_date):
        '''
        GeneratorUU:
        '''
        self.my_start_date = my_start_date

    def set_end_date(self, my_end_date):
        '''
        GeneratorUU:
        '''
        self.my_end_date = my_end_date

    def set_week_day(self, my_week_day):
        '''
        GeneratorUU:
        '''
        self.my_week_day = my_week_day

    def samples_for_recalculating(self):
        '''
        GeneratorUU:
        '''
        return fy_kw.lxa_49_inst % dict(
            e_key_sample=lc_kw.fq_k_sample_qv,
            e_samples=lc_kw.fq_m_samples_qv,
            my_table_name=self.my_table_name,
            )

def generate_specific_drawing(dfb, pytanie, multiplier):
    result = dfb.query_dct(pytanie)
    tmp_frags = []
    for row_nr, row_data in enumerate(result):
        for col_nr, value in enumerate(row_data[0]):
            if value is not None:
                tmp_frags.append('%d %d %f\n' % (col_nr * multiplier, row_nr, value))
        tmp_frags.append('\n')
    return ''.join(tmp_frags)

def generate_gnuplot_drawing(dfb):
    for my_domain in (lc_kw.fq_uu_energy_qv, lc_kw.fq_uu_power_qv):
        multiplier = {
            lc_kw.fq_uu_energy_qv: 4,
            lc_kw.fq_uu_power_qv: 1,
            }[my_domain]
        for my_object in xrange(1, 20 + 1):
            for week_day in range(7):
                obk = GeneratorUU(my_domain)
                obk.set_place(my_object)
                obk.set_week_day(week_day)
                pytanie = obk.final_shape()
                together = generate_specific_drawing(dfb, pytanie, multiplier)
                sf_iw_kw.zapisz_jawnie('%s_%d_%d.gen' % (my_domain[3], my_object, week_day), together)

class TestUUQueries(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual
    def test_uu_0_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_energy_qv)
        obk.set_place(1)
        obk.set_start_date('2013-03-11')
        obk.set_end_date('2013-03-25')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_24_inst)

    def test_uu_1_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_energy_qv)
        obk.set_start_date('2013-03-11')
        obk.set_end_date('2013-03-25')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_25_inst)

    def test_uu_2_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_energy_qv)
        obk.set_place(1)
        obk.set_end_date('2013-03-25')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_26_inst)

    def test_uu_3_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_energy_qv)
        obk.set_place(1)
        obk.set_start_date('2013-03-11')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_27_inst)

    def test_uu_4_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_energy_qv)
        obk.set_place(1)
        obk.set_week_day(0)
        self.assertEqual(obk.final_shape(), fy_kw.lxa_28_inst)

    def test_uu_5_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_power_qv)
        obk.set_place(1)
        obk.set_week_day(0)
        self.assertEqual(obk.final_shape(), fy_kw.lxa_29_inst)

    def test_uu_6_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU(lc_kw.fq_uu_energy_qv)
        self.assertEqual(obk.samples_for_recalculating(), fy_kw.lxa_48_inst)
