#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
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

class GeneratorUU:
    def __init__(self):
        '''
        GeneratorUU:
        '''
        self.my_place = None
        self.my_start_date = None
        self.my_end_date = None

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
        part_my_limits = ' AND '.join(all_my_limits)
        return fy_kw.lxa_23_inst % dict(
            part_my_limits=part_my_limits,
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

def generate_gnuplot_drawing(dfb):
    pytanie = "SELECT m_samples from uu_energy where f_object=1 and m_date >= '2013-03-11' and m_date < '2013-03-25' order by m_date;"
    result = dfb.query_dct(pytanie, flg_nowy=1)
    tmp_frags = []
    for row_nr, row_data in enumerate(result):
        for col_nr, value in enumerate(row_data[0]):
            if value is not None:
                tmp_frags.append('%d %d %f\n' % (col_nr, row_nr, value))
        tmp_frags.append('\n')
    together = ''.join(tmp_frags)
    sf_iw_kw.zapisz_jawnie('gen0', together)

class TestUUQueries(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual
    def test_uu_0_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU()
        obk.set_place(1)
        obk.set_start_date('2013-03-11')
        obk.set_end_date('2013-03-25')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_24_inst)

    def test_uu_1_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU()
        obk.set_start_date('2013-03-11')
        obk.set_end_date('2013-03-25')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_25_inst)

    def test_uu_2_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU()
        obk.set_place(1)
        obk.set_end_date('2013-03-25')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_26_inst)

    def test_uu_3_queries(self):
        '''
        TestUUQueries:
        '''
        obk = GeneratorUU()
        obk.set_place(1)
        obk.set_start_date('2013-03-11')
        self.assertEqual(obk.final_shape(), fy_kw.lxa_27_inst)
