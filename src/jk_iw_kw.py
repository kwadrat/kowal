#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

class JednoKrotny:
    def __init__(self):
        '''
        JednoKrotny:
        '''
        self.licznik = 0

    def wywolaj_jednokrotnie(self):
        '''
        JednoKrotny:
        '''
        self.licznik += 1
        if self.licznik > 1:
            raise RuntimeError('Zostałem wywołany kolejny raz')
