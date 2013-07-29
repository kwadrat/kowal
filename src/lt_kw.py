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
import lh_kw
import ey_kw
import hq_kw
import lu_kw
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

def przemysl_wiersz_poborow(slownik_wpisow, single_row):
    day_cell = fx_kw.DayCellsStats()
    for single_col in single_row[lc_kw.fq_m_samples_qv]:
        day_cell.analyze_the_cell(single_col)
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
        class_ = None
        if day_cell is None:
            tresc = ze_kw.hard_space
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
    lst_h.ddj(ze_kw.op_tbl(class_='tabelkowiec', border=1))
    wygeneruj_wiersz_naglowka(lst_h, wszystkie_dni)
    for jeden_miesiac in wszystkie_miesiace:
        wygeneruj_wiersz_miesiaca(lst_h, slownik_wpisow, wszystkie_dni, jeden_miesiac)
    lst_h.ddj(ze_kw.formularz_1c_kon_tabeli)

def zrob_tabele_poborow(lst_h, result):
    lst_h.ddj(ze_kw.formularz_1c_zlm_wrsz)
    slownik_wpisow = wykonaj_analize_danych(result)
    wygeneruj_tabelke_poborow(lst_h, slownik_wpisow)

WykresPomiarow = hq_kw.WykresPomiarow

class SzeregListPoborow(WykresPomiarow):
    def __init__(self, tgk, dfb):
        '''
        SzeregListPoborow:
        '''
        self.dfb = dfb
        self.lista_slupkow = []
        self.tvk_pobor = tgk.wez_pobor()
        aqr = ey_kw.SzkieletDatDlaPoborow(self.tvk_pobor)
        tgk.przygotuj_pobory(aqr, self.dfb)
        WykresPomiarow.__init__(self, tgk, aqr)
        self.ustaw_diagnostyke()

    def pobory_dla_licznikow(self):
        '''
        SzeregListPoborow:
        '''
        for lista_poborow in self.szereg_poborow:
            lista_poborow.pobory_dla_parametrow(self.dfb, self.id_obiekt, self.table_name)

    def przygotuj_sie_dla_listy_dni(self, lista_nr_probek):
        '''
        SzeregListPoborow:
        '''
        tmp_lista = []
        for nr_probki in lista_nr_probek:
            elem = lu_kw.PoboryDanegoDnia(self.tgk, self.aqr, self.tekstowa_diagnostyka, self.id_obiekt, nr_probki)
            tmp_lista.append(elem)
        self.szereg_poborow = tmp_lista

    def zapamietaj_wybory_formularza_poborow(self):
        '''
        SzeregListPoborow:
        '''
        self.id_obiekt = int(self.tgk.wez_obiekt())

    def determine_table_name(self):
        '''
        SzeregListPoborow:
        '''
        self.table_name = {
            lw_kw.Dn_Energy: lc_kw.fq_uu_energy_qv,
            lw_kw.Dn_Power: lc_kw.fq_uu_power_qv,
            }[self.tvk_pobor]

    def numer_probki_na_podstawie_formularza(self):
        '''
        SzeregListPoborow:
        '''
        self.determine_table_name()
        tvk_data = self.tgk.wez_date()
        result = le_kw.dq_liczniki_poboru_w_roku(self.dfb, self.table_name, self.id_obiekt, tvk_data)
        return map(lambda x: x[lc_kw.fq_k_sample_qv], result)

    def numer_probki_pokrycia_na_podstawie_formularza(self):
        '''
        SzeregListPoborow:
        '''
        self.determine_table_name()
        result = le_kw.dq_ogolnie_liczniki_poboru(self.dfb, self.table_name, self.id_obiekt)
        return map(lambda x: x[lc_kw.fq_k_sample_qv], result)

    def przygotuj_dla_poborow(self):
        '''
        SzeregListPoborow:
        '''
        self.zapamietaj_wybory_formularza_poborow()
        lista_nr_probek = self.numer_probki_na_podstawie_formularza()
        self.przygotuj_sie_dla_listy_dni(lista_nr_probek)
        self.pobory_dla_licznikow()

    def przygotuj_dla_pokrycia_poborow(self):
        '''
        SzeregListPoborow:
        '''
        self.zapamietaj_wybory_formularza_poborow()
        lista_nr_probek = self.numer_probki_pokrycia_na_podstawie_formularza()
        self.przygotuj_sie_dla_listy_dni(lista_nr_probek)
        self.pobory_dla_licznikow()

    def grafika_poborow_dla_pomiarow(self, lst_h, on_mouse):
        '''
        SzeregListPoborow:
        '''
        for lista_poborow in self.szereg_poborow:
            lista_poborow.html_ls_poborow(lst_h, on_mouse)

    def wizualizacja_pokrycia_poborami(self, lst_h):
        '''
        SzeregListPoborow:
        '''
        result = le_kw.dq_dane_jednego_obiektu(self.dfb, self.table_name, self.id_obiekt)
        zrob_tabele_poborow(lst_h, result)

    def html_szeregu_poborow(self, on_mouse):
        '''
        SzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        lst_h.ddj(fy_kw.lxa_47_inst)
        self.przygotuj_dla_poborow()
        self.grafika_poborow_dla_pomiarow(lst_h, on_mouse)
        return lst_h.polacz_html()

    def html_pokrycia_szeregu_poborow(self, on_mouse):
        '''
        SzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        self.przygotuj_dla_pokrycia_poborow()
        self.wizualizacja_pokrycia_poborami(lst_h)
        return lst_h.polacz_html()