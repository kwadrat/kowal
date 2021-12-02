#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import bz2

import sf_kw
import dn_kw
import en_kw
import dg_kw

Katalog_dokumentow = os.getcwd().decode(en_kw.en_cod_cp_win) + u'\\'
faktura_bazowa_szkielet = 'Energia_szablon.xls'
katalog_logu = Katalog_dokumentow + u'archiwum_aplikacji'
zeszyt_pomiarow = u"ZST_zużycie_en_elektr_obiekty_obce.xls"


def nazwa_pliku_faktury_bazowej():
    return Katalog_dokumentow + faktura_bazowa_szkielet


def dolacz_katalog(plik_dokumentu):
    return Katalog_dokumentow + plik_dokumentu


def zrob_kopie_pliku(nazwa_programu, przedrostek, prawie_rowne=0):
    if dg_kw.TymczasowoF:
        tmp_format = "nazwa_programu"; print 'Eval:', tmp_format, repr(eval(tmp_format))
    koncowka_pliku = 'bz2'
    kawalki_wzoru = [r'^', przedrostek, r'.+\.', koncowka_pliku, r'$']
    poskladany_wzor = u''.join(kawalki_wzoru)
    wzor_nazwy = re.compile(poskladany_wzor)
    lista_nazw = os.listdir(katalog_logu)
    zrob_kopie = 0
    dane_programu = sf_kw.wczytaj_plik(nazwa_programu)
    lista_nazw = filter(lambda x: wzor_nazwy.search(x), lista_nazw)
    if dg_kw.TymczasowoF:
        tmp_format = "lista_nazw"; print 'Eval:', tmp_format, repr(eval(tmp_format))
    if lista_nazw:
        dane_na_dysku = sf_kw.wczytaj_plik(katalog_logu + u'\\' + lista_nazw[-1])
        dane_rozpakowane = bz2.decompress(dane_na_dysku)
        if prawie_rowne:
            czy_rozne = dg_kw.porownaj_wielkosc_i_kilkubajtowe_roznice(dane_programu, dane_rozpakowane)
        else:
            czy_rozne = (dane_programu != dane_rozpakowane)
        if czy_rozne:
            if dg_kw.TymczasowoF:
                print 'Robie kopie, bo dane sa rozne.'
            zrob_kopie = 1
    else:
        if dg_kw.TymczasowoF:
            print 'Robie kopie, bo jej jeszcze nie ma.'
        zrob_kopie = 1
    if zrob_kopie:
        dane_spakowane = bz2.compress(dane_programu)
        elementy_nazwy = [u'\\', przedrostek, dn_kw.SekTeraz(), u'.', koncowka_pliku]
        nazwa_pliku = u''.join(elementy_nazwy)
        sf_kw.zapisz_plik(katalog_logu + nazwa_pliku, dane_spakowane)


def wykonaj_kopie_plikow():
    sf_kw.sprawdz_lub_utworz_katalog_logu(katalog_logu)
    zrob_kopie_pliku(nazwa_pliku_faktury_bazowej(), 'kopia_szablon_', prawie_rowne = 1)
    zrob_kopie_pliku(dolacz_katalog(zeszyt_pomiarow), 'kopia_pomiary_', prawie_rowne = 1)
