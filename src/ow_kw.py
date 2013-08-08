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

def zmniejsz_obszar_aktywny_dla_firefox(jestem_msie, slownik):
    if not jestem_msie:
        slownik[oc_kw.fq_kx_qv] -= 1
        slownik[oc_kw.fq_ky_qv] -= 1

def poszerz_pozycje(jestem_msie, pozycja):
    (px, py, kx, ky) = pozycja
    if jestem_msie:
        # MSIE ma tylko wnętrze, poszerzymy trochę koniec X i koniec Y
        kx += 1
        ky += 1
    else:
        # Firefox
        pass
    return (px, py, kx, ky)

class TestLinkuMapy(unittest.TestCase):
    def test_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        self.assertEqual(link_area_pocz, '''<area shape="rect" coords="%(px)d,%(py)d,%(kx)d,%(ky)d"\n''')
        self.assertEqual(link_area_alt_title, ''' alt="%(tekst)s" title="%(tekst)s"''')
        self.assertEqual(link_area_kon, ''' />\n''')
        self.assertEqual(link_area_alter_this, ''' onMouseOver="%(over)s"\n onMouseOut="%(out)s"\n''')

    def test_2_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        slownik = {
            oc_kw.fq_kx_qv: 10,
            oc_kw.fq_ky_qv: 20,
            }
        zmniejsz_obszar_aktywny_dla_firefox(1, slownik)
        self.assertEqual(slownik[oc_kw.fq_kx_qv], 10)
        self.assertEqual(slownik[oc_kw.fq_ky_qv], 20)

    def test_3_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        slownik = {
            oc_kw.fq_kx_qv: 10,
            oc_kw.fq_ky_qv: 20,
            }
        zmniejsz_obszar_aktywny_dla_firefox(0, slownik)
        self.assertEqual(slownik[oc_kw.fq_kx_qv], 9)
        self.assertEqual(slownik[oc_kw.fq_ky_qv], 19)

    def test_4_linku_mapy(self):
        '''
        TestLinkuMapy:
        '''
        self.assertEqual(poszerz_pozycje(1, (10, 20, 30, 40)), (10, 20, 31, 41))
        self.assertEqual(poszerz_pozycje(0, (10, 20, 30, 40)), (10, 20, 30, 40))
