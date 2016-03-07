#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import du_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def invariable_time(time_ls, default_value):
    if len(time_ls) > 1 and len(set(time_ls)) == 1:
        result = time_ls[0]
    else:
        result = default_value
    return result

class TestTimeVariability(unittest.TestCase):
    def test_time_variability(self):
        '''
        TestTimeVariability:
        '''
        self.assertEqual(invariable_time([], None), None)
        self.assertEqual(invariable_time(['07:30', '07:30'], None), '07:30')
        self.assertEqual(invariable_time(['08:00', '08:00'], None), '08:00')
        self.assertEqual(invariable_time(['07:30', '08:00'], None), None)
        self.assertEqual(invariable_time(['07:30'], None), None)
        self.assertEqual(invariable_time(['07:30', '07:30', '08:00'], None), None)
        self.assertEqual(invariable_time(['07:30', '08:00'], du_kw.rjb_minuta_przkl), du_kw.rjb_minuta_przkl)
