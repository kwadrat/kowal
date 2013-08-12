#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Cechy energii pobranej - energia, moc
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import lw_kw
import gb_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

energy_chooser = {
    lw_kw.Dn_Energy: [
        24,
        lc_kw.fq_uu_energy_qv,
        ],
    lw_kw.Dn_Power: [
        96,
        lc_kw.fq_uu_power_qv,
        ],
    }

class CechaEnergii(object):
    def __init__(self, tvk_pobor):
        '''
        TestEnergyFeatures:
        '''
        self.tvk_pobor = tvk_pobor
        (
            self.krt_wymiar,
            self.krt_table,
            ) = energy_chooser[self.tvk_pobor]

class TestEnergyFeatures(unittest.TestCase):
    def test_energy_features(self):
        '''
        TestEnergyFeatures:
        '''
        obk = CechaEnergii(lw_kw.Dn_Energy)
        self.assertEqual(obk.krt_wymiar, 24)
        self.assertEqual(obk.krt_table, lc_kw.fq_uu_energy_qv)

    def test_2_energy_features(self):
        '''
        TestEnergyFeatures:
        '''
        obk = CechaEnergii(lw_kw.Dn_Power)
        self.assertEqual(obk.krt_wymiar, 96)
        self.assertEqual(obk.krt_table, lc_kw.fq_uu_power_qv)
