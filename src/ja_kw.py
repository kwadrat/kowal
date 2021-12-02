#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import heapq

import lc_kw
import lp_kw


class HourEstimate(object):
    def store_value(self, quarter_index, one_sample):
        '''
        HourEstimate:
        '''
        self.quarter_index = quarter_index
        self.one_sample = one_sample

    def __init__(self, one_date, full_hour):
        '''
        HourEstimate:
        '''
        self.one_date = one_date
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

    def get_hhmm(self):
        '''
        HourEstimate:
        '''
        return lp_kw.part_of_day_hs(self.full_hour, 15 * self.quarter_index, 0)


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
        one_date = my_data[lc_kw.fq_m_date_qv]
        for full_hour in range(24):
            hour_est = HourEstimate(one_date, full_hour)
            start_offset = 4 * full_hour
            hour_samples = the_samples[start_offset:start_offset + 4]
            if hour_samples:
                for quarter_index, one_sample in enumerate(hour_samples):
                    hour_est.consult_value(quarter_index, one_sample)
            if hour_est.has_interesting_data():
                self.interesting_hours.append(hour_est)

    def prepare_top_values(self, liczba_max):
        '''
        MonthSummary:
        '''
        self.ordered_limited = heapq.nlargest(
            liczba_max,
            self.interesting_hours,
            lambda obk: obk.one_sample,
            )


class TestMonthStatistics(unittest.TestCase):
    def test_hour_estimate(self):
        '''
        TestMonthStatistics:
        '''
        obk = HourEstimate(one_date='2013-11-08', full_hour=23)
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
        my_samples = [None, 5, 10, None]
        my_data = {
            lc_kw.fq_m_date_qv: None,
            lc_kw.fq_m_samples_qv: my_samples,
            }
        obk.add_day_samples(my_data)
        my_samples = [None, None, None, 7]
        my_data = {
            lc_kw.fq_m_date_qv: None,
            lc_kw.fq_m_samples_qv: my_samples,
            }
        obk.add_day_samples(my_data)
        my_samples = [9, None, None, None]
        my_data = {
            lc_kw.fq_m_date_qv: None,
            lc_kw.fq_m_samples_qv: my_samples,
            }
        obk.add_day_samples(my_data)
        self.assertEqual(len(obk.interesting_hours), 3)
        obk.prepare_top_values(2)
        self.assertEqual(obk.interesting_hours[1].get_hhmm(), '00:45')
