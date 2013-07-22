#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ust_iw_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class ListaLubSlownikOgolnie(object):
    def __init__(self, wytworca_unikalnych_etykiet, etykieta_miejsca):
        '''
        ListaLubSlownikOgolnie:
        '''
        assert etykieta_miejsca is not None # Potrzeba mi etykiety
        self.moja_etykieta_instancji = wytworca_unikalnych_etykiet.nowy_licznik()
        if ust_iw_kw.LokalnaDiagnostykaKlas:
            print 'Wytworzono_%s %s w miejscu %s' % (
            wytworca_unikalnych_etykiet.jaki_to_rodzaj(),
            self.moja_etykieta_instancji, etykieta_miejsca)

    def wzorzec_repr(self, nazwa_klasy):
        '''
        ListaLubSlownikOgolnie:
        '''
        dlugosc = self.podaj_dlugosc()
        return '%s(%s):%d' % (nazwa_klasy, self.moja_etykieta_instancji, dlugosc)
