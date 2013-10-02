#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Cechy energii pobranej - energia, moc
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import gb_kw
import lw_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

protected_max = max

energy_chooser = {
    lw_kw.Dn_Energy: [
        24,
        lc_kw.fq_uu_energy_qv,
        gb_kw.Jedn_kWh,
        fy_kw.lxa_56_inst,
        sum,
        ],
    lw_kw.Dn_Power: [
        96,
        lc_kw.fq_uu_power_qv,
        gb_kw.Jedn_kWtow,
        fy_kw.lxa_57_inst,
        protected_max,
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
            self.krt_jedn,
            self.krt_etykieta,
            self.krt_vl_fnctn,
            ) = energy_chooser[self.tvk_pobor]

    def cumulative_init(self):
        '''
        TestEnergyFeatures:
        '''
        self.cumulative_value = 0.0

    def cumulative_update(self, new_value):
        '''
        TestEnergyFeatures:
        '''
        if self.tvk_pobor == lw_kw.Dn_Energy:
            self.cumulative_value += new_value
        else:
            self.cumulative_value = max(self.cumulative_value, new_value)

class TestEnergyFeatures(unittest.TestCase):
    def test_energy_features(self):
        '''
        TestEnergyFeatures:
        '''
        obk = CechaEnergii(lw_kw.Dn_Energy)
        self.assertEqual(obk.krt_wymiar, 24)
        self.assertEqual(obk.krt_table, lc_kw.fq_uu_energy_qv)
        self.assertEqual(obk.krt_jedn, gb_kw.Jedn_kWh)
        self.assertEqual(obk.krt_etykieta, fy_kw.lxa_56_inst)
        self.assertEqual(obk.krt_vl_fnctn, sum)

    def test_2_energy_features(self):
        '''
        TestEnergyFeatures:
        '''
        obk = CechaEnergii(lw_kw.Dn_Power)
        self.assertEqual(obk.krt_wymiar, 96)
        self.assertEqual(obk.krt_table, lc_kw.fq_uu_power_qv)
        self.assertEqual(obk.krt_jedn, gb_kw.Jedn_kWtow)
        self.assertEqual(obk.krt_etykieta, fy_kw.lxa_57_inst)
        self.assertEqual(obk.krt_vl_fnctn, max)

    def test_sum_of_energy(self):
        '''
        TestEnergyFeatures:
        '''
        obk = CechaEnergii(lw_kw.Dn_Energy)
        obk.cumulative_init()
        self.assertEqual(obk.cumulative_value, 0.0)
        obk.cumulative_update(1)
        self.assertEqual(obk.cumulative_value, 1.0)
        obk.cumulative_update(3)
        self.assertEqual(obk.cumulative_value, 4.0)
        obk.cumulative_update(2)
        self.assertEqual(obk.cumulative_value, 6.0)

    def test_maximum_of_power(self):
        '''
        TestEnergyFeatures:
        '''
        obk = CechaEnergii(lw_kw.Dn_Power)
        obk.cumulative_init()
        self.assertEqual(obk.cumulative_value, 0.0)
        obk.cumulative_update(1)
        self.assertEqual(obk.cumulative_value, 1.0)
        obk.cumulative_update(3)
        self.assertEqual(obk.cumulative_value, 3.0)
        obk.cumulative_update(2)
        self.assertEqual(obk.cumulative_value, 3.0)
