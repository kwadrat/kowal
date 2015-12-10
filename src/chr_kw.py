#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def husk_object(fvk_ob_ct):
    (id_obkt, tvk_junction) = fvk_ob_ct
    return id_obkt

class TestHuskingIdentifier(unittest.TestCase):
    def test_husking_identifier(self):
        '''
        TestHuskingIdentifier:
        '''
        self.assertEqual(husk_object(fvk_ob_ct=(1, 2)), 1)
        self.assertEqual(husk_object(fvk_ob_ct=(3, 1)), 3)
