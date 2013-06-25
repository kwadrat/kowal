#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
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
    if old_value is None or old_value == new_value:
        result = 1
    elif (
            lm_kw.have_dec_type(old_value) and
            new_value is not None and
            old_value == lm_kw.readjust_number(4, new_value)):
        result = 1
    else:
        result = 0
    return result

class SampleRow:
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

    def get_row_of_samples(self):
        '''
        SampleRow:
        '''
        return self.list_of_samples

    def get_row_key(self):
        '''
        SampleRow:
        '''
        return self.sample_key

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
