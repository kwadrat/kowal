#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import sj_kw
import oa_kw
import od_kw
import es_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

MojeSlupki = es_kw.MojeSlupki

class PoboroweSlupki(MojeSlupki):
    ile_pikseli = 30
    def __init__(self, tgk, aqr, dwk):
        '''
        PoboroweSlupki:
        '''
        MojeSlupki.__init__(self, tgk, aqr, dwk)
        self.chce_po_lewej_miejsca_na_skale(self.ile_pikseli)

    def ustaw_skalowanie_obrazu(self):
        '''
        PoboroweSlupki:
        '''
        LiczbaPaskow = self.aqr.liczba_paskow()
        if LiczbaPaskow not in (24, 96):
            raise RuntimeError('LiczbaPaskow: %d' % LiczbaPaskow)
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz
        self.szerokosc_wykresu = oa_kw.zaokraglij_mi(self.szerokosc_obrazu - self.ile_pikseli, LiczbaPaskow)
        self.koniec_wykresu = self.szerokosc_wykresu + self.ile_pikseli
        self.szerokosc_slupka = self.szerokosc_wykresu / LiczbaPaskow

    def wyznacz_etykiete(self, pocz):
        '''
        PoboroweSlupki:
        '''
        return ''

    def wyznacz_poborowe_slupki(self, MinY, MaxY):
        '''
        PoboroweSlupki:
        '''
        self.MinWysSlupka = self.wysokosc_obrazu - self.MarginesSlupka

        pracuj = self.sprawdz_nietypowe_sytuacje(self.IleSlupkow, MinY, MaxY)
        if pracuj:
            moje_paczki_faktur = self.dwk.odcinki_bazowe.p_odc_baz()
            for jeden_odc_bzw in moje_paczki_faktur:
                pocz, kon = jeden_odc_bzw.get_pk()
                SlWspX = self.aqr.miejsce_umieszczenia_slupka(pocz, kon, self.szerokosc_skali, self.koniec_wykresu)
                if SlWspX != None:
                    Wartosc = jeden_odc_bzw.slownik_qm.jh_kwota()
                    GoraSlupka, DolSlupka = self.wyznacz_gore_dol_slupka(MinY, MaxY, Wartosc)
                    Etykieta = self.wyznacz_etykiete(pocz)
                    jeden_slupek = sj_kw.JedenSlupek(SlWspX, DolSlupka, GoraSlupka, Etykieta, Wartosc, jeden_odc_bzw)
                    self.DodajSlupek(jeden_slupek)
            self.RysujListeSlupkow()
