#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import sf_iw_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def generate_gnuplot_drawing(dfb):
    pytanie = "SELECT m_samples from uu_energy where f_object=1 and m_date >= '2013-03-11' and m_date < '2013-03-25' order by m_date;"
    result = dfb.query_dct(pytanie, flg_nowy=1)
    tmp_frags = []
    for row_nr, row_data in enumerate(result):
        for col_nr, value in enumerate(row_data[0]):
            if value is not None:
                tmp_frags.append('%d %d %f\n' % (col_nr, row_nr, value))
        tmp_frags.append('\n')
    together = ''.join(tmp_frags)
    sf_iw_kw.zapisz_jawnie('gen0', together)

class TestUUQueries(unittest.TestCase):
    def test_uu_queries(self):
        '''
        TestUUQueries:
        '''
