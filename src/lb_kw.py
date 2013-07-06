#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class ListaOdcBazowych:
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
        return MinY, MaxY

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
