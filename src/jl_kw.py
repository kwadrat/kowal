#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import ciz_kw
import jn_kw

HoQuServer = jn_kw.HoQuServer

class HourServer(HoQuServer):
    def __init__(self):
        '''
        HourServer:
        '''
        self.all_time_columns = []
        self.time_for_header = []
        for column_index in xrange(24):
            elem = ciz_kw.HourMiniServer(column_index)
            self.all_time_columns.append(elem)
            self.time_for_header.append(elem.header_for_hour_column)
        HoQuServer.__init__(self, 1)

class TestHour_t_Server(unittest.TestCase):
    pass
