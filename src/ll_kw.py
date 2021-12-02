#!/usr/bin/python
# -*- coding: UTF-8 -*-

import us_kw


class ListaLubSlownikOgolnie(object):
    def __init__(self, wytworca_unikalnych_etykiet, etykieta_miejsca):
        '''
        ListaLubSlownikOgolnie:
        '''
        assert etykieta_miejsca is not None  # Potrzeba mi etykiety
        self.moja_etykieta_instancji = wytworca_unikalnych_etykiet.nowy_licznik()
        if us_kw.LokalnaDiagnostykaKlas:
            print('Wytworzono_%s %s w miejscu %s' % (
                wytworca_unikalnych_etykiet.jaki_to_rodzaj(),
                self.moja_etykieta_instancji,
                etykieta_miejsca,
                ))

    def wzorzec_repr(self, nazwa_klasy):
        '''
        ListaLubSlownikOgolnie:
        '''
        dlugosc = self.podaj_dlugosc()
        return '%s(%s):%d' % (nazwa_klasy, self.moja_etykieta_instancji, dlugosc)
