#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fz_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def dq_object_key(dfb, under_name):
    db_statement = fz_kw.ptn_object_key(under_name)
    return dfb.query_dct(db_statement)

def dq_entry_already_inserted(dfb, n_table, key_object, row_date, my_hour):
    db_statement = fz_kw.ptn_entry_already_inserted(n_table, key_object, row_date, my_hour)
    return dfb.query_dct(db_statement)
