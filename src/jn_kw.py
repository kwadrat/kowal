#!/usr/bin/python
# -*- coding: UTF-8 -*-


class HoQuServer(object):
    def __init__(self, smpl_per_hour):
        '''
        HoQuServer:
        '''
        self.smpl_per_hour = smpl_per_hour
        self.cnt_of_samples = len(self.time_for_header)
