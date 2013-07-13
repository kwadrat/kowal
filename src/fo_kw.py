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

class SpecGrupyWykFak(object):
    '''
    Dane współdzielone przez grupę wykresów lub grupę faktur
    Paczka zwracana jako:
    - wykaz liczników, dla których pokazujemy wykresy
    - wykaz faktur dla danego licznika
    '''
    def __init__(self, tfi_medium, lista_slownikow):
        '''
        SpecGrupyWykFak:
        '''
        self.tfi_medium = tfi_medium
        self.lista_wewn = lista_slownikow

    def podaj_twoja_liste(self):
        '''
        SpecGrupyWykFak:
        '''
        return self.lista_wewn

    def dolacz_na_koncu(self, dodatkowy):
        '''
        SpecGrupyWykFak:
        '''
        druga_lista = dodatkowy.podaj_twoja_liste()
        self.lista_wewn.extend(druga_lista)

    def akt_dlugosc(self):
        '''
        SpecGrupyWykFak:
        '''
        return len(self.lista_wewn)
