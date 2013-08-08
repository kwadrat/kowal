#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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

link_area_pocz = '''<area shape="rect" coords="%(px)d,%(py)d,%(kx)d,%(ky)d"\n'''
link_area_alt_title = ''' alt="%(tekst)s" title="%(tekst)s"'''
link_area_kon = ''' />\n'''
link_area_alter_this = ''' onMouseOver="%(over)s"\n onMouseOut="%(out)s"\n'''

class TestLinkuMapy(unittest.TestCase):
    def test_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        self.assertEqual(link_area_pocz, '''<area shape="rect" coords="%(px)d,%(py)d,%(kx)d,%(ky)d"\n''')
        self.assertEqual(link_area_alt_title, ''' alt="%(tekst)s" title="%(tekst)s"''')
        self.assertEqual(link_area_kon, ''' />\n''')
        self.assertEqual(link_area_alter_this, ''' onMouseOver="%(over)s"\n onMouseOut="%(out)s"\n''')
