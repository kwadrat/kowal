#!/usr/bin/python
# -*- coding: UTF-8 -*-

import lp_kw


class HourMiniServer(object):
    def __init__(self, column_index):
        '''
        HourMiniServer:
        '''
        self.header_for_hour_column = lp_kw.describe_hour_column(column_index)

    def __repr__(self):
        '''
        HourMiniServer:
        '''
        return 'HS(%s)' % self.header_for_hour_column
