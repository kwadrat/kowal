#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lk_kw
import oc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)


def fn_adres_post(wersja_produkcyjna):
    return lk_kw.rjb_sam_slsh + oc_kw.fn_a_in_dwa(wersja_produkcyjna) + lk_kw.rjb_sam_slsh + oc_kw.dodaj_py(oc_kw.rjb_strona_druga.rj_sam_rdzen)

class TestCaleidPages(unittest.TestCase):
    def test_caleid_pages(self):
        '''
        TestCaleidPages:
        '''
        self.assertEqual(fn_adres_post(1), '/inne/l2.py')
        self.assertEqual(fn_adres_post(0), '/inne2/l2.py')
