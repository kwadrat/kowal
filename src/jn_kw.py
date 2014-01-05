#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class HoQuServer(object):
    def __init__(self, smpl_per_hour):
        '''
        HoQuServer:
        '''
        self.smpl_per_hour = smpl_per_hour
        self.cnt_of_samples = len(self.time_for_header)

    def dst_double_hour(self, row_date, sample_index):
        '''
        HoQuServer:
        '''
        result = 0
        if dn_kw.autumn_dst_day(row_date):
            if self.smpl_per_hour == 4:
                result = 7 <= sample_index <= 10
            else:
                assert self.smpl_per_hour == 1
                result = sample_index == 1
        return result
