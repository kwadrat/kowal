#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import oo_kw
import lb_kw
import oa_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class WykresDlaFakturPomiarow:
    def start_odc_baz(self):
        '''
        WykresDlaFakturPomiarow:
        '''
        # Lista odcinków bazowych - lista elementów do wykreślenia w postaci
        # słupków: [pocz, kon, kwota, {lp miejsca: [lista lp faktur]}]
        self.odcinki_bazowe = lb_kw.ListaOdcBazowych()

    def __init__(self, tgk, aqr):
        '''
        WykresDlaFakturPomiarow:
        '''
        self.tgk = tgk
        self.aqr = aqr
        # Ma wartość 0 dla wykresu zbiorczego,
        # większą dla wykresu indywidualnego
        if oo_kw.DocelowoOsobneDane:
            ##############################################################################
            self.lp_miejsca = self.tgk.gen_num_miejsc.przydziel_kolejny_numer(self)
            ##############################################################################
        else:
            ##############################################################################
            self.lp_miejsca = self.tgk.gen_num_miejsc.przydziel_kolejny_numer(self)
            ##############################################################################
        self.start_odc_baz()

    def mam_wykres_zbiorczy(self):
        '''
        WykresDlaFakturPomiarow:
        '''
        return not self.lp_miejsca

    def kolor_tla(self):
        '''
        WykresDlaFakturPomiarow:
        Wykres zbiorczy ma mieć inne tło
        '''
        if self.mam_wykres_zbiorczy():
            moje_tlo = oa_kw.KOLOR_TLO_SELEDYN
        else:
            moje_tlo = oa_kw.KOLOR_EXCEL_TLO_SZARE
        return moje_tlo
