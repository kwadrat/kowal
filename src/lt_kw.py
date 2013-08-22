#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza zużycia - szereg list pomiarów, prezentacja w postacji HTML
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lm_kw
import ze_kw
import jb_kw
import hq_kw
import wn_kw
import gc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

WykresPomiarow = hq_kw.WykresPomiarow

class OgolnaListaPoborow(WykresPomiarow):
    def __init__(self, tgk, aqr, dfb, krt_pobor):
        '''
        OgolnaListaPoborow:
        '''
        self.dfb = dfb
        self.lista_slupkow = []
        self.table_name = krt_pobor.krt_table
        tgk.przygotuj_pobory()
        WykresPomiarow.__init__(self, tgk, aqr)
        self.id_obiekt = int(self.tgk.wez_obiekt())
        self.ustaw_diagnostyke()

    def rdzen_kwoty(self, akt, kwota):
        '''
        OgolnaListaPoborow:
        '''
        nast = akt + 1
        slownik_qm = wn_kw.KlasaSlownika()
        slownik_qm.jh_ustaw_kwt_qm(kwota)
        self.dnw.odcinki_bazowe.app_end(jb_kw.JedenOdcinekBazowy(2 * akt, 2 * nast, slownik_qm))

    def rdzen_rysowania(self, lst_h, krt_pobor, dolny_podpis):
        '''
        OgolnaListaPoborow:
        '''
        if self.aqr.malo_dat_szkieletu():
            lst_h.info_o_braku_dat()
        else:
            vert_axis = self.dnw.odcinki_bazowe.zakres_pionowy()
            ms = gc_kw.PoboroweOgolneSlupki(self.tgk, self.aqr, self.dnw, dolny_podpis)
            ms.wyznacz_poborowe_slupki(vert_axis, krt_pobor)
            moja_suma = krt_pobor.cumulative_value
            moja_jednostka = krt_pobor.krt_jedn
            opis_dotyczy = []
            opis_dotyczy.append(ze_kw.sp_stl(
                krt_pobor.krt_etykieta,
                lm_kw.rzeczywista_na_napis(moja_suma),
                moja_jednostka))
            if vert_axis.MaxY:
                ms.podpisz_obie_osie(vert_axis, krt_pobor)
                on_mouse = {}
                kod_html = ms.wykreslanie_slupkow(on_mouse)
                lst_h.ddj(''.join(opis_dotyczy))
                lst_h.ddj(kod_html)
            else:
                lst_h.info_o_braku_roznic_w_pionie(vert_axis.MaxY)
