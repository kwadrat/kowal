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
    result = dfb.query_dct(db_statement)
    return result

def dq_entry_already_inserted(dfb, n_table, key_object, row_date, my_hour):
    db_statement = "select * from %(n_table)s where f_object=%(f_object)d and m_date='%(m_date)s' and m_time='%(m_time)s';" % dict(
        n_table=n_table,
        f_object=key_object,
        m_date=row_date,
        m_time=my_hour,
        )
    return dfb.query_dct(db_statement)
