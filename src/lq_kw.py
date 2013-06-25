#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

def check_for_conflict():
    return 1

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
        self.list_of_samples[sample_index] = value

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
        self.assertEqual(check_for_conflict(), 1)
