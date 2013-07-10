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

rjb_sam_slsh = '/'
PoczObrazka = 'plik_'
RozszerzenieObrazka = '.png'
url_ameryka_http = 'http://'
adres_maszyny = 'media.ciri.pl'
GenPicDir = 'gen_kowal/'

class TestConstantStrings(unittest.TestCase):
    def test_constant_strings(self):
        '''
        TestConstantStrings:
        '''
        self.assertEqual(rjb_sam_slsh, '/')
        self.assertEqual(PoczObrazka, 'plik_')
        self.assertEqual(RozszerzenieObrazka, '.png')
        self.assertEqual(url_ameryka_http, 'http://')
        self.assertEqual(adres_maszyny, 'media.ciri.pl')
        self.assertEqual(GenPicDir, 'gen_kowal/')
