#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def concatenate_index_name(table, field):
    return '%(table)s_%(field)s_index' % dict(
        table=table,
        field=field,
        )

def index_create(name, table, field):
    return fy_kw.lxa_4_inst % dict(
        name=name,
        table=table,
        field=field,
        )

class TestVariousPatterns(unittest.TestCase):
    def test_various_patterns(self):
        '''
        TestVariousPatterns:
        '''
        self.assertEqual(concatenate_index_name('t', 'f'), fy_kw.lxa_2_inst)
        self.assertEqual(index_create('a', 't', 'f'), fy_kw.lxa_3_inst)
