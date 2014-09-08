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

Jedn_sztuki = 'szt'
# Kilowatogodzin
Jedn_kWh = 'kWh'
Jedn_kWtow = 'kW'
Jedn_zlotowki = 'zł'
Jedn_procent = '%'

def nawiasy_kwadratowe(jednostka):
    return '[%s]' % jednostka

Jedn_k_zlotowki = nawiasy_kwadratowe(Jedn_zlotowki)
Jedn_jy_sztuki = nawiasy_kwadratowe(Jedn_sztuki)
Jedn_k_procenty = nawiasy_kwadratowe(Jedn_procent)
Jedn_k_zl_na_kWh = nawiasy_kwadratowe('%s/%s' % (Jedn_zlotowki, Jedn_kWh))
tytul_kilowatow_przekroczenia = nawiasy_kwadratowe(Jedn_kWtow)
JednHour = 'h'
# Metrów sześciennych
JednM3 = 'm<sup>3</sup>'
JednMet3h = hj_kw.rcp_dziel(JednM3, JednHour)
# Megawatów
JednMW = 'MW'
# Kilowatogodzin/Megawatogodzin? Ludzie różnie wpisują, na razie nie
# szukałem sposobu na rozróżnienie, którą jednostkę podają.
Jedn_kW_MWh = 'kWh/MWh'
# Gigadżuli
JednGJ = 'GJ'

class TestUnitNames(unittest.TestCase):
    def test_unit_names(self):
        '''
        TestUnitNames:
        '''
        self.assertEqual(Jedn_sztuki, 'szt')
        self.assertEqual(Jedn_jy_sztuki, '[szt]')
        self.assertEqual(Jedn_kWh, 'kWh')
        self.assertEqual(Jedn_kWtow, 'kW')
        self.assertEqual(Jedn_zlotowki, 'zł')
        self.assertEqual(Jedn_k_zlotowki, '[zł]')
        self.assertEqual(Jedn_k_procenty, '[%]')
        self.assertEqual(Jedn_k_zl_na_kWh, '[zł/kWh]')
        self.assertEqual(tytul_kilowatow_przekroczenia, '[kW]')
        self.assertEqual(JednHour, 'h')
        self.assertEqual(JednM3, 'm<sup>3</sup>')
        self.assertEqual(JednMet3h, 'm<sup>3</sup>/h')
        self.assertEqual(Jedn_kW_MWh, 'kWh/MWh')
        self.assertEqual(JednGJ, 'GJ')
        self.assertEqual(JednMW, 'MW')
