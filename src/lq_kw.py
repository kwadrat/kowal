#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
import le_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def allowed_replacement(old_value, new_value):
    if old_value is None:
        result = 1
    elif old_value == new_value:
        result = 1
    elif old_value == lm_kw.wartosc_zero_globalna:
        result = 1
    elif (
            lm_kw.have_dec_type(old_value) and
            new_value is not None and
            old_value == lm_kw.readjust_number(4, new_value)):
        result = 1
    else:
        result = 0
    return result

def cnt_none(elements):
    return len(filter(lambda x: x is None, elements))

def cnt_zero(elements):
    return len(filter(lambda x: x == lm_kw.wartosc_zero_globalna, elements))

def sum_of_not_nones(elements):
    return sum(filter(lambda x: x is not None, elements))

class SampleRow(object):
    def __init__(self):
        '''
        SampleRow:
        '''
        self.sample_key = None
        self.list_of_samples = None

    def new_and_empty(self, cnt_per_day):
        '''
        SampleRow:
        '''
        self.sample_key = None
        self.list_of_samples = [None] * cnt_per_day

    def update_for_index(self, sample_index, value):
        '''
        SampleRow:
        '''
        old_value = self.list_of_samples[sample_index]
        if allowed_replacement(old_value, value):
            self.list_of_samples[sample_index] = value
        else:
            raise RuntimeError('old_value: %s value: %s' % (repr(old_value), repr(value)))

    def fill_from_data(self, sample_key, sample_data):
        '''
        SampleRow:
        '''
        self.sample_key = sample_key
        self.list_of_samples = sample_data

    def put_in_database(self, dfb, table_of_samples, local_key):
        '''
        SampleRow:
        '''
        (key_object, row_date) = local_key
        v_none = cnt_none(self.list_of_samples)
        v_zero = cnt_zero(self.list_of_samples)
        v_sum = sum_of_not_nones(self.list_of_samples)
        if self.sample_key:
            le_kw.dq_update_vector_of_samples(dfb, table_of_samples, key_object, row_date, self.list_of_samples, self.sample_key)
        else:
            le_kw.dq_insert_vector_of_samples(dfb, table_of_samples, key_object, row_date, self.list_of_samples)

class TestRowChanges(unittest.TestCase):
    def test_row_changes(self):
        '''
        TestRowChanges:
        '''
        self.assertEqual(allowed_replacement(None, None), 1)
        self.assertEqual(allowed_replacement(7, None), 0)
        self.assertEqual(allowed_replacement(7, 7), 1)
        self.assertEqual(allowed_replacement(lm_kw.a2d('5.4200'), 5.42), 1)
        self.assertEqual(allowed_replacement(lm_kw.a2d('5.4568'), 5.456799999952317), 1)
        self.assertEqual(allowed_replacement(lm_kw.a2d('5.4200'), None), 0)
        self.assertEqual(allowed_replacement(lm_kw.a2d('0.0000'), 5.42), 1)
        self.assertEqual(cnt_none([]), 0)
        self.assertEqual(cnt_none([None]), 1)
        self.assertEqual(cnt_none([1]), 0)
        self.assertEqual(cnt_zero([
            lm_kw.wartosc_zero_globalna,
            lm_kw.wartosc_zero_globalna,
            1,
            None,
            ]), 2)
        self.assertEqual(sum_of_not_nones([
            lm_kw.wartosc_zero_globalna,
            None,
            1,
            2,
            3,
            ]),
            lm_kw.a2d('6'))
