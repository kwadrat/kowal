#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lp_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
