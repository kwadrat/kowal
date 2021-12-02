#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import dn_kw
import lp_kw
import jn_kw

HoQuServer = jn_kw.HoQuServer


class QuarterServer(HoQuServer):
    def __init__(self):
        '''
        QuarterServer:
        '''
        self.quarter_translator = {}
        self.time_for_header = []
        for i in xrange(96):
            hh_mm = lp_kw.determine_quarter(i)
            self.quarter_translator[hh_mm] = i
            self.time_for_header.append(lp_kw.describe_quarter_column(i))
        HoQuServer.__init__(self, 4)

    def quarter_to_number(self, hh_mm):
        '''
        QuarterServer:
        '''
        return self.quarter_translator[hh_mm]

    def dst_double_hour(self, row_date, sample_index):
        '''
        QuarterServer:
        '''
        result = 0
        if dn_kw.autumn_dst_day(row_date):
            result = 7 <= sample_index <= 10
        return result


class TestPeriodQuarters(unittest.TestCase):
    def test_period_quarters(self):
        '''
        TestPeriodQuarters:
        '''
        obk = QuarterServer()
        self.assertEqual(obk.quarter_to_number('00:00'), 0)
        self.assertEqual(obk.quarter_to_number('00:15'), 1)
        self.assertEqual(obk.quarter_to_number('23:45'), 95)
