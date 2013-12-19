#!/usr/bin/python
# -*- coding: UTF-8 -*-

class HoQuServer(object):
    def __init__(self, smpl_per_hour):
        '''
        HoQuServer:
        '''
        self.smpl_per_hour = smpl_per_hour
        self.cnt_of_samples = len(self.time_for_header())

    def dst_double_hour(self, row_date, sample_index):
        '''
        HoQuServer:
        '''
        result = 0
        if row_date == '2013-10-27' or row_date == '2012-10-28':
            if self.smpl_per_hour == 4:
                result = 7 <= sample_index <= 10
            else:
                assert self.smpl_per_hour == 1
                result = sample_index == 1
        return result
