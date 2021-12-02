#!/usr/bin/python
# -*- coding: UTF-8 -*-

import rq_kw
import op_kw


class ListaOdcBazowych(object):
    def __init__(self):
        '''
        ListaOdcBazowych:
        '''
        self.wykaz_odcinkow_bazowych = []

    def app_end(self, element):
        '''
        ListaOdcBazowych:
        '''
        self.wykaz_odcinkow_bazowych.append(element)

    def pokaz_odcinkow_bazowych(self):
        '''
        ListaOdcBazowych:
        '''
        if rq_kw.TymczasowoOgrWysw:
            if not rq_kw.TymczasowoPkzBaz:
                return
        for i in self.wykaz_odcinkow_bazowych:
            print i.formatted_pkks()

    def len_odcinkow_bazowych(self):
        '''
        ListaOdcBazowych:
        '''
        return len(self.wykaz_odcinkow_bazowych)

    def lista_pocz(self):
        '''
        ListaOdcBazowych:
        '''
        return map(lambda x: x.get_pocz(), self.wykaz_odcinkow_bazowych)

    def lista_kon(self):
        '''
        ListaOdcBazowych:
        '''
        return map(lambda x: x.get_kon(), self.wykaz_odcinkow_bazowych)

    def lista_max_kwot(self):
        '''
        ListaOdcBazowych:
        '''
        return map(lambda x: x.slownik_qm.get_max_kwota(), self.wykaz_odcinkow_bazowych)

    def zakres_pionowy(self):
        '''
        ListaOdcBazowych:
        '''
        # Na wykresie musi zmieścić się najwyższy słupek
        moje_kwoty = self.lista_max_kwot()
        MinY = 0
        if moje_kwoty:
            MaxY = max(moje_kwoty)
        else:
            MaxY = 0
        return op_kw.AxisY(MinY, MaxY)

    def lista_slownikow_qm(self):
        '''
        ListaOdcBazowych:
        '''
        return map(lambda x: x.slownik_qm, self.wykaz_odcinkow_bazowych)

    def pk_head(self):
        '''
        ListaOdcBazowych:
        '''
        return self.wykaz_odcinkow_bazowych[0].get_pk()

    def pk_tail(self):
        '''
        ListaOdcBazowych:
        '''
        wynik = []
        for element in self.wykaz_odcinkow_bazowych[1:]:
            pocz_kon = element.get_pk()
            wynik.append(pocz_kon)
        return wynik

    def p_odc_baz(self):
        '''
        ListaOdcBazowych:
        '''
        return self.wykaz_odcinkow_bazowych
