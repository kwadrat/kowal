#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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

class MonthSummary(object):
    def __init__(self):
        '''
        MonthSummary:
        '''

    def add_day_samples(self, my_data):
        '''
        MonthSummary:
        '''
        the_samples = my_data[lc_kw.fq_m_samples_qv]
        for full_hour in range(24):
            start_offset = 4 * full_hour
            hour_samples = the_samples[start_offset:start_offset + 4]
            if hour_samples:
                pass

class TestMonthStatistics(unittest.TestCase):
    def test_month_statistics(self):
        '''
        TestMonthStatistics:
        '''
        obk = MonthSummary()
        my_samples = [None, None, None, None]
        my_data = {
            lc_kw.fq_m_date_qv: None,
            lc_kw.fq_m_samples_qv: my_samples,
            }
        my_data[lc_kw.fq_m_date_qv]
        my_data[lc_kw.fq_m_samples_qv]
        obk.add_day_samples(my_data)
