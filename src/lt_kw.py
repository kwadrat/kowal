#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza zużycia - szereg list pomiarów, prezentacja w postacji HTML
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import lc_kw
import le_kw
import dn_kw
import lw_kw
import ze_kw
import eu_kw
import fx_kw
import ey_kw
import hq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def zapamietaj_pomiar(slownik_wpisow, year, month, day, day_cell):
    etykieta_miesiaca = dn_kw.napis_z_rok_mies(year, month)
    if etykieta_miesiaca not in slownik_wpisow:
        slownik_wpisow[etykieta_miesiaca] = {}
    slownik_miesiaca = slownik_wpisow[etykieta_miesiaca]
    slownik_miesiaca[day] = day_cell

def compare_values(slow_value, fast_value):
    if slow_value != fast_value:
        raise RuntimeError('Rozne: %s, %s' % (repr(slow_value), repr(fast_value)))

def przemysl_wiersz_poborow(slownik_wpisow, single_row):
    day_cell = fx_kw.DayCellsStats()
    day_cell.cell_params(single_row[lc_kw.fq_m_none_qv], single_row[lc_kw.fq_m_zero_qv])
    full_date = single_row[lc_kw.fq_m_date_qv]
    zapamietaj_pomiar(
        slownik_wpisow,
        full_date.year,
        full_date.month,
        full_date.day,
        day_cell,
        )

def wykonaj_analize_danych(result):
    slownik_wpisow = {}
    for single_row in result:
        przemysl_wiersz_poborow(slownik_wpisow, single_row)
    return slownik_wpisow

def wyznacz_daty_miesieczne(slownik_wpisow):
    wszystkie_miesiace = slownik_wpisow.keys()
    wszystkie_miesiace.sort()
    return wszystkie_miesiace

def wygeneruj_wiersz_naglowka(lst_h, wszystkie_dni):
    lst_h.ddj(ze_kw.op_tr())
    lst_h.ddj(ze_kw.op_ptd('Miesiąc'))
    for jeden_dzien in wszystkie_dni:
        lst_h.ddj(ze_kw.op_ptd(str(jeden_dzien)))
    lst_h.ddj(ze_kw.formularz_67c_kon_wiersza)

def wygeneruj_wiersz_miesiaca(lst_h, slownik_wpisow, wszystkie_dni, jeden_miesiac):
    lst_h.ddj(ze_kw.op_tr())
    dane_miesiaca = slownik_wpisow[jeden_miesiac]
    lst_h.ddj(ze_kw.op_ptd(jeden_miesiac))
    for jeden_dzien in wszystkie_dni:
        day_cell = dane_miesiaca.get(jeden_dzien)
        if day_cell is None:
            tresc = ze_kw.hard_space
            class_ = None
            title = None
        else:
            tresc = day_cell.cell_message()
            class_ = day_cell.cell_background()
            title = day_cell.cell_title()
        lst_h.ddj(ze_kw.op_ptd(
            str(tresc),
            class_=class_,
            title=title,
            ))
    lst_h.ddj(ze_kw.formularz_67c_kon_wiersza)

def wygeneruj_tabelke_poborow(lst_h, slownik_wpisow):
    wszystkie_miesiace = wyznacz_daty_miesieczne(slownik_wpisow)
    wszystkie_dni = eu_kw.detect_my_days(slownik_wpisow)
    lst_h.ddj(ze_kw.op_tbl(class_=fy_kw.lxa_40_inst, border=1))
    wygeneruj_wiersz_naglowka(lst_h, wszystkie_dni)
    for jeden_miesiac in wszystkie_miesiace:
        wygeneruj_wiersz_miesiaca(lst_h, slownik_wpisow, wszystkie_dni, jeden_miesiac)
    lst_h.ddj(ze_kw.formularz_1c_kon_tabeli)

def zrob_tabele_poborow(lst_h, result):
    lst_h.ddj(ze_kw.formularz_1c_zlm_wrsz)
    slownik_wpisow = wykonaj_analize_danych(result)
    wygeneruj_tabelke_poborow(lst_h, slownik_wpisow)

WykresPomiarow = hq_kw.WykresPomiarow

class OgolnySzeregListPoborow(WykresPomiarow):
    def determine_table_name(self):
        '''
        OgolnySzeregListPoborow:
        '''
        self.table_name = {
            lw_kw.Dn_Energy: lc_kw.fq_uu_energy_qv,
            lw_kw.Dn_Power: lc_kw.fq_uu_power_qv,
            }[self.tvk_pobor]

    def __init__(self, tgk, dfb):
        '''
        OgolnySzeregListPoborow:
        '''
        self.dfb = dfb
        self.lista_slupkow = []
        self.tvk_pobor = tgk.wez_pobor()
        self.determine_table_name()
        aqr = ey_kw.SzkieletDatDlaPoborow(self.tvk_pobor)
        tgk.przygotuj_pobory(aqr, self.dfb)
        WykresPomiarow.__init__(self, tgk, aqr)
        self.ustaw_diagnostyke()

    def pobory_dla_licznikow(self):
        '''
        OgolnySzeregListPoborow:
        '''
        for lista_poborow in self.szereg_poborow:
            lista_poborow.pobory_dla_parametrow(self.dfb, self.id_obiekt, self.table_name)

    def zapamietaj_wybory_formularza_poborow(self):
        '''
        OgolnySzeregListPoborow:
        '''
        self.id_obiekt = int(self.tgk.wez_obiekt())

    def grafika_poborow_dla_pomiarow(self, lst_h):
        '''
        OgolnySzeregListPoborow:
        '''
        for lista_poborow in self.szereg_poborow:
            lista_poborow.html_ls_poborow(lst_h)

    def wizualizacja_pokrycia_poborami(self, lst_h):
        '''
        OgolnySzeregListPoborow:
        '''
        result = le_kw.dq_dane_jednego_obiektu(self.dfb, self.table_name, self.id_obiekt)
        zrob_tabele_poborow(lst_h, result)
