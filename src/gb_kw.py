#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Nazwy jednostek
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import hj_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

JednHour = 'h'
Jedn_sztuki = 'szt'
# Kilowatogodzin
Jedn_kWtow = 'kW'
Jedn_kWh = Jedn_kWtow + JednHour
Jedn_a_kWh_h = hj_kw.rcp_dziel(Jedn_kWh, JednHour)
Jedn_b_kWh_h_za_h = ''.join([Jedn_a_kWh_h, ' za ', JednHour])
Jedn_zlotowki = 'zł'
Jedn_procent = '%'

def nawiasy_kwadratowe(jednostka):
    return '[%s]' % jednostka

Jedn_k_kWh = nawiasy_kwadratowe(Jedn_kWh)
Jedn_k_zlotowki = nawiasy_kwadratowe(Jedn_zlotowki)
Jedn_jy_sztuki = nawiasy_kwadratowe(Jedn_sztuki)
Jedn_k_procenty = nawiasy_kwadratowe(Jedn_procent)
Jedn_k_zl_na_kWh = nawiasy_kwadratowe(hj_kw.rcp_dziel(Jedn_zlotowki, Jedn_kWh))
Jedn_k_a_kWh_h = nawiasy_kwadratowe(Jedn_a_kWh_h)
tytul_kilowatow_przekroczenia = nawiasy_kwadratowe(Jedn_kWtow)
# Metrów sześciennych
JednM3 = 'm<sup>3</sup>'
JednMet3h = hj_kw.rcp_dziel(JednM3, JednHour)
Jedn_a_Met3_n = JednM3 + '<sub>n</sub>'
# Megawatów
JednMW = 'MW'
Jedn_MWh = JednMW + JednHour
# Kilowatogodzin/Megawatogodzin? Ludzie różnie wpisują, na razie nie
# szukałem sposobu na rozróżnienie, którą jednostkę podają.
Jedn_kW_MWh = hj_kw.rcp_dziel(Jedn_kWh, Jedn_MWh)
# Gigadżuli
JednGJ = 'GJ'
# Ton
JednTon = 'ton'
JednAsciiM3 = 'm3'
Jedn_wsp_kWh_M3 = hj_kw.rcp_dziel(Jedn_kWh, JednM3)
Jedn_n_wsp_kWh_M3 = nawiasy_kwadratowe(Jedn_wsp_kWh_M3)

class TestUnitNames(unittest.TestCase):
    def test_unit_names(self):
        '''
        TestUnitNames:
        '''
        self.assertEqual(Jedn_sztuki, 'szt')
        self.assertEqual(Jedn_jy_sztuki, '[szt]')
        self.assertEqual(Jedn_kWh, 'kWh')
        self.assertEqual(Jedn_k_kWh, '[kWh]')
        self.assertEqual(Jedn_a_kWh_h, 'kWh/h')
        self.assertEqual(Jedn_b_kWh_h_za_h, 'kWh/h za h')
        self.assertEqual(Jedn_k_a_kWh_h, '[kWh/h]')
        self.assertEqual(Jedn_kWtow, 'kW')
        self.assertEqual(Jedn_zlotowki, 'zł')
        self.assertEqual(Jedn_k_zlotowki, '[zł]')
        self.assertEqual(Jedn_k_procenty, '[%]')
        self.assertEqual(Jedn_k_zl_na_kWh, '[zł/kWh]')
        self.assertEqual(tytul_kilowatow_przekroczenia, '[kW]')
        self.assertEqual(JednHour, 'h')
        self.assertEqual(JednM3, 'm<sup>3</sup>')
        self.assertEqual(JednMet3h, 'm<sup>3</sup>/h')
        self.assertEqual(Jedn_a_Met3_n, 'm<sup>3</sup><sub>n</sub>')
        self.assertEqual(Jedn_kW_MWh, 'kWh/MWh')
        self.assertEqual(JednGJ, 'GJ')
        self.assertEqual(JednMW, 'MW')
        self.assertEqual(Jedn_MWh, 'MWh')
        self.assertEqual(JednTon, 'ton')
        self.assertEqual(JednAsciiM3, 'm3')
        self.assertEqual(Jedn_wsp_kWh_M3, 'kWh/m<sup>3</sup>')
        self.assertEqual(Jedn_n_wsp_kWh_M3, '[kWh/m<sup>3</sup>]')
