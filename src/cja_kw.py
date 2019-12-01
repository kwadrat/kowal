#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import du_kw
import lp_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
        self.stamp_times = lp_kw.convert_keys(self.mono_cnt)

    def get_initial_hour(self, selected_counter_id):
        '''
        InvariantPackage:
        '''
        if selected_counter_id not in self.mono_cnt:
            if self.cnt_ls:
                selected_counter_id = self.cnt_ls[0]
            else:
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
        cnt_ls = [959, 386, 381]
        obj = InvariantPackage(cnt_ls, lp_kw.example_data_from_db, du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(959), '07:30')
        self.assertEqual(obj.get_initial_hour(381), '08:00')
        self.assertEqual(obj.get_initial_hour(386), du_kw.rjb_minuta_przkl)
        self.assertEqual(obj.get_initial_hour(121212), '07:30')
        self.assertEqual(obj.get_initial_hour(None), '07:30')
        self.assertEqual(obj.get_text_times(), "{'959': '07:30', '381': '08:00', '386': '10:41'}")
