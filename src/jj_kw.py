#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lp_kw
import jn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

HoQuServer = jn_kw.HoQuServer

class QuarterServer(HoQuServer):
    def __init__(self):
        '''
        QuarterServer:
        '''
        self.quarter_translator = {}
        self.list_of_quarters = []
        for i in xrange(96):
            hh_mm = lp_kw.determine_quarter(i)
            self.quarter_translator[hh_mm] = i
            self.list_of_quarters.append(hh_mm)
        HoQuServer.__init__(self, 4)

    def quarter_to_number(self, hh_mm):
        '''
        QuarterServer:
        '''
        return self.quarter_translator[hh_mm]

    def time_for_header(self):
        '''
        QuarterServer:
        '''
        return self.list_of_quarters

class TestPeriodQuarters(unittest.TestCase):
    def test_period_quarters(self):
        '''
        TestPeriodQuarters:
        '''
        obk = QuarterServer()
        self.assertEqual(obk.quarter_to_number('00:00'), 0)
        self.assertEqual(obk.quarter_to_number('00:15'), 1)
        self.assertEqual(obk.quarter_to_number('23:45'), 95)
