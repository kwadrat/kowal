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

class ManipulateSheet(object):
    def __init__(self):
        '''
        ManipulateSheet:
        '''

    def read_cell(self, wiersz, kolumna):
        '''
        ManipulateSheet:
        '''
        if kolumna < self.sheet.ncols and wiersz < self.sheet.nrows:
            value = self.sheet.cell(wiersz, kolumna).value
        else:
            value = None
        return value
