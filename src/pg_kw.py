#!/usr/bin/python
# -*- coding: UTF-8 -*-

import dg_kw
import sw_kw
import we_kw
import fq_kw


class PosrednikAplikacjiExcela(object):

    def podlacz_app_excel(self):
        '''
        PosrednikAplikacjiExcela:
        '''
        self.xl = dg_kw.NowyXL()

    def __init__(self):
        '''
        PosrednikAplikacjiExcela:
        '''
        self.xl = None
        self.wsl = sw_kw.WyznaczanieSlownie()

    def pusty_nowy_arkusz(self):
        '''
        PosrednikAplikacjiExcela:
        '''
        return self.xl.Workbooks.Add()

    def otwarcie_pliku_xls(self, nazwa):
        '''
        PosrednikAplikacjiExcela:
        '''
        return self.xl.Workbooks.Open(nazwa)

    def otworz_plik_tego_zeszytu(self, nazwa_pliku):
        '''
        PosrednikAplikacjiExcela:
        '''
        return self.otwarcie_pliku_xls(fq_kw.dolacz_katalog(nazwa_pliku))

    def pokazywanie_okien_dialogowych(self, zezwolenie):
        '''
        PosrednikAplikacjiExcela:
        '''
        if self.xl is not None:
            self.xl.DisplayAlerts = zezwolenie

    def pokaz_aplikacje_excela(self, widzialny):
        '''
        PosrednikAplikacjiExcela:
        '''
        self.xl.Visible = widzialny

    def przesun_krawedz_wydruku(self):
        '''
        PosrednikAplikacjiExcela:
        '''
        self.xl.ActiveWindow.View = we_kw.WartosciExcel.xlPageBreakPreview
        self.xl.ActiveSheet.VPageBreaks(1).DragOff(Direction=we_kw.WartosciExcel.xlToRight, RegionIndex=1)
        self.xl.ActiveWindow.View = we_kw.WartosciExcel.xlNormalView

    def zakoncz_excela(self):
        '''
        PosrednikAplikacjiExcela:
        '''
        self.pokazywanie_okien_dialogowych(False)
        if self.xl is not None:
            self.xl.Quit()
            self.xl = None
