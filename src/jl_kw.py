#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lp_kw
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
            elem = lp_kw.HourMiniServer(column_index)
            self.all_time_columns.append(elem)
            self.time_for_header.append(elem.header_for_hour_column)
        HoQuServer.__init__(self, 1)

    def verify_hours_headers(self, energy_reader, start_energy_col):
        '''
        HourServer:
        '''
        for sample_index, one_column in enumerate(self.all_time_columns):
            tmp_text = energy_reader.vx_num_time(start_energy_col + sample_index, 6)
            expected = one_column.header_for_hour_column
            lp_kw.verify_for_equal(tmp_text, expected)
