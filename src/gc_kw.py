#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lm_kw
import lw_kw
import dd_kw
import sj_kw
import oa_kw
import ey_kw
import oh_kw
import od_kw
import oq_kw
import es_kw

MojeSlupki = es_kw.MojeSlupki


class PoboroweOgolneSlupki(MojeSlupki):
    pikseli_po_lewej = 30

    def __init__(self, tgk, aqr, dnw, dolny_podpis):
        '''
        PoboroweOgolneSlupki:
        '''
        rn_after = 2
        MojeSlupki.__init__(self, tgk, aqr, dnw, rn_after)
        self.chce_bez_tresci = 1
        self.chce_po_lewej_miejsca_na_skale(self.pikseli_po_lewej)
        self.dolny_podpis = dolny_podpis

    def linii_na_dole(self):
        '''
        PoboroweOgolneSlupki:
        '''
        return 2

    def ustaw_skalowanie_obrazu(self):
        '''
        PoboroweOgolneSlupki:
        '''
        LiczbaPaskow = self.aqr.liczba_paskow()
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz
        self.szerokosc_wykresu = oa_kw.zaokraglij_mi(self.szerokosc_obrazu - self.pikseli_po_lewej, LiczbaPaskow)
        self.koniec_x_wykresu = self.szerokosc_wykresu + self.pikseli_po_lewej
        self.szerokosc_slupka = self.szerokosc_wykresu / LiczbaPaskow

    def wyznacz_etykiete(self, pocz):
        '''
        PoboroweOgolneSlupki:
        '''
        return ''

    def wypisz_kwadransy_godziny(self, wsp_y_napisu, akt, nast):
        '''
        PoboroweOgolneSlupki:
        '''
        NapisCzasowy = self.aqr.tekst_pelnej_godziny(akt)
        wsp_x_napisu = self.aqr.poziomo_tego_dnia((nast + akt) // 2, self.szerokosc_dx_skali, self.koniec_x_wykresu)
        self.my_texts.append((wsp_x_napisu, wsp_y_napisu, NapisCzasowy))

    def wypisz_jednostke_godziny(self):
        '''
        PoboroweOgolneSlupki:
        '''
        wsp_x_napisu = (self.pikseli_po_lewej + self.koniec_x_wykresu) // 2
        wsp_y_napisu = 149
        self.my_texts.append((wsp_x_napisu, wsp_y_napisu, self.dolny_podpis))

    def kwadransy_godziny_z_kreskami(self):
        '''
        PoboroweOgolneSlupki:
        '''
        for akt, nast in self.aqr.pary_szkieletu():
            if self.aqr.to_pelna_godzina(akt):
                self.rysuj_same_kreski(self.wsp_y_na_dole_slupka + 1, akt, self.koniec_x_wykresu)
                self.wypisz_kwadransy_godziny(self.gorna_mniejsza, akt, nast)
        self.wypisz_jednostke_godziny()

    def add_vertical_axis(self, vert_axis, krt_pobor):
        '''
        PoboroweOgolneSlupki:
        '''
        end_x = self.szerokosc_dx_skali
        end_y = self.wsp_y_na_dole_slupka
        n_total, n_step = oq_kw.determine_vert_params(vert_axis.MaxY)
        for i in range(n_total + 1):
            Wartosc = float(i * n_step)
            gora_slupka = vert_axis.wyznacz_gorna_wartosc(Wartosc)
            GoraSlupka = int(end_y - (end_y - self.margines_dy_powyzej_slupka) * gora_slupka)
            self.draw_line.tick_on_vertical_axis(end_x, GoraSlupka)
            napis_liczby = lm_kw.rzeczywista_na_napis(Wartosc)
            self.my_texts.append((end_x - 15, GoraSlupka, napis_liczby))

        self.my_texts.append((15, 5, krt_pobor.krt_jedn))

    def podpisz_obie_osie(self, vert_axis, krt_pobor):
        '''
        PoboroweOgolneSlupki:
        '''
        self.kwadransy_godziny_z_kreskami()
        self.add_vertical_axis(vert_axis, krt_pobor)

    def wyznacz_poborowe_slupki(self, vert_axis, krt_pobor):
        '''
        PoboroweOgolneSlupki:
        '''
        krt_pobor.cumulative_init()
        pracuj = self.sprawdz_nietypowe_sytuacje(self.IleSlupkow, vert_axis)
        if pracuj:
            moje_paczki_faktur = self.dnw.odcinki_bazowe.p_odc_baz()
            for jeden_odc_bzw in moje_paczki_faktur:
                pocz, kon = jeden_odc_bzw.get_pk()
                SlWspX = self.aqr.miejsce_umieszczenia_slupka(pocz, kon, self.szerokosc_dx_skali, self.koniec_x_wykresu)
                if SlWspX is not None:
                    yh_value = jeden_odc_bzw.slownik_qm.jh_kwota()
                    krt_pobor.cumulative_update(yh_value)
                    GoraSlupka, DolSlupka = self.wyznacz_gore_dol_slupka(vert_axis, yh_value)
                    Etykieta = self.wyznacz_etykiete(pocz)
                    jeden_slupek = sj_kw.JedenSlupek(SlWspX, DolSlupka, GoraSlupka, Etykieta, yh_value, jeden_odc_bzw)
                    self.DodajSlupek(jeden_slupek)
            self.RysujListeSlupkow()


class TestPoborowychOgolnychSlupkow(unittest.TestCase):
    def test_poborowych_ogolnych_slupkow(self):
        '''
        TestPoborowychOgolnychSlupkow:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        krt_pobor = dd_kw.CechaEnergii(lw_kw.Dm_Energy)
        aqr = ey_kw.SzkieletDatDlaPoborow(krt_pobor)
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        obk = PoboroweOgolneSlupki(tgk, aqr, dnw, lw_kw.PDS_Godziny)
        self.assertEqual(obk.pikseli_po_lewej, 30)
        self.assertEqual(obk.szerokosc_obrazu, 1250)
        self.assertEqual(obk.szerokosc_dx_skali, 30)
        self.assertEqual(obk.szerokosc_wykresu, 1200)
        self.assertEqual(obk.koniec_x_wykresu, 1230)
        self.assertEqual(obk.szerokosc_slupka, 50)
        self.assertEqual(obk.wysokosc_obrazu, 160)
        self.assertEqual(obk.margines_dy_powyzej_slupka, 20)
        self.assertEqual(obk.wsp_y_na_dole_slupka, 130)
        self.assertEqual(obk.gorna_mniejsza, 140)
        self.assertEqual(obk.linii_na_dole(), 2)
        self.assertEqual(obk.chce_bez_tresci, 1)
        self.assertEqual(obk.dolny_podpis, 'godziny')
