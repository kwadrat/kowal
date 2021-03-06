#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ciz_kw
import jn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
