#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import du_kw
import lp_kw


class InvariantPackage(object):
    '''
    Dla ułatwienia wpisywania liczników - wykryj i zaproponuj typową godzinę
    odczytu licznika, np. jeśli codziennie licznik był odczytywany
    o godz. 07:00, to zaproponuj 07:00 jako następną godzinę odczytu.
    '''
    def __init__(self, cnt_ls, times_of_counters, counter_snapshot_moment):
        '''
        InvariantPackage:
        '''
        self.cnt_ls = cnt_ls
        self.counter_snapshot_moment = counter_snapshot_moment
        self.mono_cnt = lp_kw.detect_invariant_time(times_of_counters, self.counter_snapshot_moment)
        for one_x in cnt_ls:
            if one_x not in self.mono_cnt:
                self.mono_cnt[one_x] = counter_snapshot_moment
        self.stamp_times = lp_kw.convert_keys(self.mono_cnt)

    def get_initial_hour(self, selected_counter_id):
        '''
        InvariantPackage:
        '''
        if selected_counter_id not in self.mono_cnt:
            selected_counter_id = None
        if selected_counter_id is None:
            result = self.counter_snapshot_moment
        else:
            result = self.mono_cnt.get(selected_counter_id)
        return result

    def get_text_times(self):
        '''
        InvariantPackage:
        '''
        return self.stamp_times


class TestInvariantPack(unittest.TestCase):
    def test_a_invariant_pack(self):
        '''
        TestInvariantPack:
        '''
        obj = InvariantPackage([], [], du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(121212), du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(None), du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_text_times(), "{}")

    def test_b_invariant_pack(self):
        '''
        TestInvariantPack:
        '''
        cnt_ls = [1310, 959, 386, 381]
        obj = InvariantPackage(cnt_ls, lp_kw.example_data_from_db, du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(959), '07:30')
        self.assertEqual(obj.get_initial_hour(381), '08:00')
        self.assertEqual(obj.get_initial_hour(386), du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(121212), du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(None), du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_text_times(), "{'381': '08:00', '386': '10:41', '959': '07:30', '1310': '10:41'}")
