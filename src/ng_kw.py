#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Etykiety dla styli generowanych plików Excel
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

import unittest

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

code_strings = '''
NVB_3_STYLE
NVB_6_STYLE
NVB_7_STYLE
'''
for single_name in code_strings.split():
    exec '%(single_name)s = "%(single_name)s"' % dict(
        single_name=single_name,
        )

class TestZnacznikowStylu(unittest.TestCase):
    def test_znacznikow_stylu(self):
        '''
        TestZnacznikowStylu:
        '''
        self.assertEqual(NVB_3_STYLE, 'NVB_3_STYLE')
