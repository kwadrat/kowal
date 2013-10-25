#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import le_kw
import dd_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def locate_object_key(dfb, under_name):
    key_object = le_kw.dq_object_key(dfb, under_name)
    if not key_object:
        key_object = le_kw.dq_add_new_object_key(dfb, under_name)
    ret_size = len(key_object)
    if ret_size == 1:
        key_object = key_object[0][lc_kw.fq_k_object_qv];
    else:
        raise RuntimeError('ret_size = %d' % ret_size)
    return key_object

class CommonRdWr(object):
    def __init__(self, tvk_pobor, period_server):
        '''
        CommonRdWr:
        '''
        self.krt_pobor = dd_kw.CechaEnergii(tvk_pobor)
        self.table_of_samples = self.krt_pobor.krt_table
        self.period_server = period_server
