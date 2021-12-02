#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import if_kw
import hj_kw
import lm_kw
import le_kw


def cnt_none(elements):
    return len(filter(lambda x: x is None, elements))


def cnt_zero(elements):
    return len(filter(lambda x: x in (0.0, lm_kw.wartosc_zero_globalna), elements))


def sum_of_not_nones(krt_vl_fnctn, elements):
    return krt_vl_fnctn(hj_kw.remove_nones(elements))


def obtain_stats(krt_vl_fnctn, list_of_samples):
    v_none = cnt_none(list_of_samples)
    v_zero = cnt_zero(list_of_samples)
    v_sum = sum_of_not_nones(krt_vl_fnctn, list_of_samples)
    return v_none, v_zero, v_sum


def ignored_zero(value):
    return value == 0.0


class SampleRow(object):
    def __init__(self, rough_point):
        '''
        SampleRow:
        '''
        self.sample_key = None
        self.list_of_samples = None
        self.rough_point = rough_point

    def new_and_empty(self, cnt_per_day):
        '''
        SampleRow:
        '''
        self.sample_key = None
        self.list_of_samples = [None] * cnt_per_day

    def allowed_replacement(self, old_value, new_value):
        '''
        SampleRow:
        '''
        if old_value is None:
            result = 1
        elif old_value == new_value:
            result = 1
        elif old_value == lm_kw.wartosc_zero_globalna:
            result = 1
        elif (
                lm_kw.have_dec_type(old_value) and
                new_value is not None and
                self.rough_point.rough_replacement(old_value, new_value)):
            result = 1
        else:
            result = 0
        return result

    def update_for_index(self, sample_index, value, dst_allow, row_date):
        '''
        SampleRow:
        '''
        old_value = self.list_of_samples[sample_index]
        if self.allowed_replacement(old_value, value) or dst_allow:
            self.list_of_samples[sample_index] = value
        elif ignored_zero(value):
            pass
        else:
            statement = ('row_date: %s, sample_index: %d old_value: %s value: %s' % (
                repr(row_date),
                sample_index,
                repr(old_value),
                repr(value),
                ))
            if_kw.warn_halt(1, statement)

    def fill_from_data(self, sample_key, sample_data):
        '''
        SampleRow:
        '''
        self.sample_key = sample_key
        self.list_of_samples = sample_data

    def put_in_database(self, dfb, krt_pobor, table_of_samples, local_key):
        '''
        SampleRow:
        '''
        (key_object, row_date) = local_key
        v_none, v_zero, v_sum = obtain_stats(krt_pobor.krt_vl_fnctn, self.list_of_samples)
        if self.sample_key:
            le_kw.dq_update_vector_of_samples(dfb, table_of_samples, key_object, row_date, self.list_of_samples, v_none, v_zero, v_sum, self.sample_key)
        else:
            le_kw.dq_insert_vector_of_samples(dfb, table_of_samples, key_object, row_date, self.list_of_samples, v_none, v_zero, v_sum)

    def make_stats_of_samples(self, dfb, krt_pobor, table_of_samples, local_key):
        '''
        SampleRow:
        '''
        v_none, v_zero, v_sum = obtain_stats(krt_pobor.krt_vl_fnctn, self.list_of_samples)
        le_kw.dq_update_stats_of_samples(dfb, table_of_samples, v_none, v_zero, v_sum, self.sample_key)


class TestRowChanges(unittest.TestCase):
    def test_row_changes(self):
        '''
        TestRowChanges:
        '''
        point_three = lm_kw.CloseToValue(places=3)
        obk = SampleRow(point_three)
        self.assertEqual(obk.allowed_replacement(None, None), 1)
        self.assertEqual(obk.allowed_replacement(7, None), 0)
        self.assertEqual(obk.allowed_replacement(7, 7), 1)
        self.assertEqual(obk.allowed_replacement(lm_kw.a2d('5.4200'), 5.42), 1)
        self.assertEqual(obk.allowed_replacement(lm_kw.a2d('5.4568'), 5.456799999952317), 1)
        self.assertEqual(obk.allowed_replacement(lm_kw.a2d('5.4200'), None), 0)
        self.assertEqual(obk.allowed_replacement(lm_kw.a2d('0.0000'), 5.42), 1)
        self.assertEqual(cnt_none([]), 0)
        self.assertEqual(cnt_none([None]), 1)
        self.assertEqual(cnt_none([1]), 0)
        self.assertEqual(cnt_zero([
            lm_kw.wartosc_zero_globalna,
            lm_kw.wartosc_zero_globalna,
            1,
            None,
            ]), 2)
        self.assertEqual(cnt_zero([
            0.0,
            ]), 1)
        self.assertEqual(sum_of_not_nones(sum, [
            lm_kw.wartosc_zero_globalna,
            None,
            1,
            2,
            3,
            ]),
            lm_kw.a2d('6'))
