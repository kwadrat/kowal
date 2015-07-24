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

class JednoKrotny(object):
    def __init__(self, use_bool=0):
        '''
        JednoKrotny:
        '''
        self.licznik = 0
        self.use_bool = use_bool

    def wywolaj_jednokrotnie(self):
        '''
        JednoKrotny:
        '''
        self.licznik += 1
        if self.licznik > 1:
            if not self.use_bool:
                raise RuntimeError('Zostałem wywołany kolejny raz')
        return self.licznik == 1

class TestCallAtMostOnce(unittest.TestCase):
    def test_call_at_most_once(self):
        '''
        TestCallAtMostOnce:
        '''
        ojt = JednoKrotny()
        ojt.wywolaj_jednokrotnie()
        self.assertRaises(RuntimeError, ojt.wywolaj_jednokrotnie)

    def test_a_call_at_most_once(self):
        '''
        TestCallAtMostOnce:
        '''
        ojt = JednoKrotny(use_bool=1)
        self.assertEqual(ojt.wywolaj_jednokrotnie(), 1)
        self.assertEqual(ojt.wywolaj_jednokrotnie(), 0)
        self.assertEqual(ojt.wywolaj_jednokrotnie(), 0)
