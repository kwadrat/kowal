#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pokryciowy szereg list
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import ze_kw
import le_kw
import eu_kw
import lh_kw
import lt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def wyznacz_daty_miesieczne(slownik_wpisow):
    wszystkie_miesiace = slownik_wpisow.keys()
    wszystkie_miesiace.sort()
    return wszystkie_miesiace

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

def wygeneruj_wiersz_naglowka(lst_h, wszystkie_dni):
    lst_h.ddj(ze_kw.op_tr())
    lst_h.ddj(ze_kw.op_ptd('Miesiąc'))
    for jeden_dzien in wszystkie_dni:
        lst_h.ddj(ze_kw.op_ptd(str(jeden_dzien)))
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
    slownik_wpisow = lt_kw.wykonaj_analize_danych(result)
    wygeneruj_tabelke_poborow(lst_h, slownik_wpisow)

OgolnySzeregListPoborow = lt_kw.OgolnySzeregListPoborow

class PokryciowySzeregListPoborow(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PokryciowySzeregListPoborow:
        '''
        OgolnySzeregListPoborow.__init__(self, tgk, dfb, krt_pobor)

    def wizualizacja_pokrycia_poborami(self, lst_h):
        '''
        PokryciowySzeregListPoborow:
        '''
        result = le_kw.dq_dane_jednego_obiektu(self.dfb, self.table_name, self.id_obiekt)
        zrob_tabele_poborow(lst_h, result)

    def html_pokrycia_szeregu_poborow(self):
        '''
        PokryciowySzeregListPoborow:
        '''
        lst_h = lh_kw.ListaHTML()
        self.zapamietaj_wybory_formularza_poborow()
        self.wizualizacja_pokrycia_poborami(lst_h)
        return lst_h.polacz_html()
