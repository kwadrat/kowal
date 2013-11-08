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

class HourEstimate(object):
    def store_value(self, quarter_index, one_sample):
        '''
        HourEstimate:
        '''
        self.quarter_index = quarter_index
        self.one_sample = one_sample

    def __init__(self, full_hour):
        '''
        HourEstimate:
        '''
        self.full_hour = full_hour
        self.store_value(None, None)

    def consult_value(self, quarter_index, one_sample):
        '''
        HourEstimate:
        '''
        if one_sample is not None:
            if self.one_sample is None:
                self.store_value(quarter_index, one_sample)
            elif one_sample > self.one_sample:
                self.store_value(quarter_index, one_sample)

    def has_interesting_data(self):
        '''
        HourEstimate:
        '''
        return self.quarter_index is not None

class MonthSummary(object):
    def __init__(self):
        '''
        MonthSummary:
        '''
        self.interesting_hours = []

    def add_day_samples(self, my_data):
        '''
        MonthSummary:
        '''
        the_samples = my_data[lc_kw.fq_m_samples_qv]
        for full_hour in range(24):
            hour_est = HourEstimate(full_hour)
            start_offset = 4 * full_hour
            hour_samples = the_samples[start_offset:start_offset + 4]
            if hour_samples:
                for quarter_index, one_sample in enumerate(hour_samples):
                    hour_est.consult_value(quarter_index, one_sample)
            if hour_est.has_interesting_data():
                self.interesting_hours.append(hour_est)

class TestMonthStatistics(unittest.TestCase):
    def test_hour_estimate(self):
        '''
        TestMonthStatistics:
        '''
        obk = HourEstimate(full_hour=23)
        quarter_index = 0
        one_sample = None
        obk.consult_value(quarter_index, one_sample)
        self.assertEqual(obk.has_interesting_data(), 0)
        quarter_index = 1
        one_sample = 5
        obk.consult_value(quarter_index, one_sample)
        self.assertEqual(obk.has_interesting_data(), 1)

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
