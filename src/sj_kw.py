#!/usr/bin/python
# -*- coding: UTF-8 -*-

'Jeden słupek do narysowania - współrzędne'


class JedenSlupek(object):
    def __init__(self, SlWspX, DolSlupka, GoraSlupka, Etykieta, yh_value, jeden_odc_bzw):
        '''
        JedenSlupek:
        '''
        self.SlWspX = SlWspX
        self.DolSlupka = DolSlupka
        self.GoraSlupka = GoraSlupka
        self.Etykieta = Etykieta
        self.yh_value = yh_value
        self.jeden_odc_bzw = jeden_odc_bzw

    def zwroc_pelna_krotke(self):
        '''
        JedenSlupek:
        '''
        return (self.SlWspX, self.DolSlupka, self.GoraSlupka, self.Etykieta, self.yh_value, self.jeden_odc_bzw)

    def klucz_porzadku(self):
        '''
        JedenSlupek:
        Sortowanie według góry słupka - te najwyższe (najmniejsza wsp. Y) są
        rysowane najwcześniej
        '''
        return self.GoraSlupka
