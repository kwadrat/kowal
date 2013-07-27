#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza zużycia - lista pomiarów dla jednego licznika
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import lm_kw
import le_kw
import ze_kw
import jb_kw
import hq_kw
import wn_kw
import eq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def wykonaj_pobor(dfb, table_name, nr_probki):
    jeden_pomiar = le_kw.dq_jeden_licznik_poboru_w_roku(dfb, table_name, nr_probki)
    if jeden_pomiar:
        wynik = jeden_pomiar[0][lc_kw.fq_m_samples_qv]
    else:
        wynik = None
    return wynik

WykresPomiarow = hq_kw.WykresPomiarow

class PoboryDanegoDnia(WykresPomiarow):
    def __init__(self, tgk, aqr, tekstowa_diagnostyka, id_obiekt, nr_probki):
        '''
        PoboryDanegoDnia:
        '''
        self.id_obiekt = id_obiekt
        self.nr_probki = nr_probki
        self.tekstowa_diagnostyka = tekstowa_diagnostyka
        WykresPomiarow.__init__(self, tgk, aqr)

    def pobory_dla_parametrow(self, dfb, id_obiekt, table_name):
        '''
        PoboryDanegoDnia:
        '''
        self.lista_pomiarow = wykonaj_pobor(dfb, table_name, self.nr_probki)
        if self.tekstowa_diagnostyka:
            print self.lista_pomiarow

    def zbuduj_odcinki_y_bazowe(self):
        '''
        PoboryDanegoDnia:
        '''
        for akt, kwota in enumerate(self.lista_pomiarow):
            nast = akt + 1
            kwota = lm_kw.dec2flt(kwota)
            if kwota is not None:
                slownik_qm = wn_kw.KlasaSlownika()
                slownik_qm.jh_ustaw_kwt_qm(kwota)
                self.dnw.odcinki_bazowe.app_end(jb_kw.JedenOdcinekBazowy(2 * akt, 2 * nast, slownik_qm))

    def html_ls_poborow(self, lst_h, on_mouse):
        '''
        PoboryDanegoDnia:
        '''
        self.zbuduj_odcinki_y_bazowe()
        vert_axis = self.dnw.odcinki_bazowe.zakres_pionowy()
        ms = eq_kw.PoboroweSlupki(self.tgk, self.aqr, self.dnw)
        moja_suma = ms.wyznacz_poborowe_slupki(vert_axis)
        moja_jednostka = ms.jednostka_osi_pionowej()
        opis_dotyczy = []
        # qaz - duplikat
        opis_dotyczy.append(ze_kw.sp_stl(
            lm_kw.rzeczywista_na_napis(moja_suma),
            moja_jednostka))
        # qaz - duplikat
        ms.podpisz_obie_osie(vert_axis)
        kod_html = ms.wykreslanie_slupkow(on_mouse)
        lst_h.ddj(''.join(opis_dotyczy))
        lst_h.ddj(kod_html)
