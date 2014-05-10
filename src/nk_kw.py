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

class DaneWspolneDlaRoku(object):
    def __init__(self):
        '''
        DaneWspolneDlaRoku:
        '''
        self.dane_dla_miesiaca = {}

    def wartosc_z_roku(self, fvk_miesiac, qj_ta_kolumna):
        '''
        DaneWspolneDlaRoku:
        '''
        if fvk_miesiac in self.dane_dla_miesiaca:
            wynik = self.dane_dla_miesiaca[fvk_miesiac].wartosc_z_miesiaca(qj_ta_kolumna)
        else:
            wynik = 0
        return wynik
