#!/usr/bin/python
# -*- coding: UTF-8 -*-

class SampleRow:
    def new_and_empty(self, cnt_per_day):
        '''
        SampleRow:
        '''
        self.sample_key = None
        self.list_of_samples = [None] * cnt_per_day
