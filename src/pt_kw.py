#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Operacje generowania obrazu
Lewy, górny róg obrazka ma współrzędne (0, 0)
'''

import unittest

import lc_kw
import rq_kw
import oc_kw
import jt_kw
import ls_kw
import oa_kw
import dq_kw
import oh_kw
import mf_kw
import od_kw
import on_kw
import ow_kw

class KlasaObrazu(object):
    '''
    Klasa bazowa dla poszczególnych graficznych przedstawień w postaci PNG
    '''
    def __init__(self, tgk, aqr, dnw, literka_typu):
        '''
        KlasaObrazu:
        '''
        self.rozkaz_mapy = ''
        # Lista rejonów i numerów faktur dla generowanej mapy
        # Może też być z treścią dymka
        self.moja_mapa = []
        self.draw_line = on_kw.KreskiWykresu()
        self.my_texts = []
        self.tgk = tgk
        self.aqr = aqr
        self.dnw = dnw
        self.literka_typu = literka_typu
        self.szerokosc_dx_skali = 0
        self.moja_nazwa = mf_kw.plik_grafiki(self.tgk.znacznik_unik, self.literka_typu, self.dnw.lp_miejsca, ())
        self.html_name = self.html_my_name(self.literka_typu, self.dnw.lp_miejsca)

    def chce_po_lewej_miejsca_na_skale(self, pikseli_po_lewej):
        '''
        KlasaObrazu:
        '''
        self.szerokosc_dx_skali = pikseli_po_lewej

    def link_mapy(self, on_real_mouse, slownik):
        '''
        KlasaObrazu:
        '''
        return ow_kw.link_a_mapy(on_real_mouse, slownik, self.tgk.jestem_msie, self.html_name, self.moja_nazwa)

    def html_my_name(self, literka, lp_miejsca):
        '''
        KlasaObrazu:
        '''
        return '%s%d' % (literka, lp_miejsca)

    def im_draw(self, tlo):
        '''
        KlasaObrazu:
        '''
        return ls_kw.prepare_new_image((self.szerokosc_obrazu, self.wysokosc_obrazu), tlo)

    def kopia_obrazu(self, im):
        '''
        KlasaObrazu:
        '''
        return ls_kw.copy_existing_image(im)

    def link_do_obrazu(self):
        '''
        KlasaObrazu:
        '''
        lista = []
        # Nazwa mapy dla tego obrazku
        nazwa_tej_mapy = mf_kw.nazwa_mapy(self.literka_typu, self.dnw.lp_miejsca)
        if self.moja_mapa:
            lista.append(mf_kw.pocz_mapy(nazwa_tej_mapy))
            lista.extend(self.moja_mapa)
            lista.append(mf_kw.kon_mapy)
            self.rozkaz_mapy = ' usemap="#%(mapa_slupkow)s"' % dict(mapa_slupkow = nazwa_tej_mapy)
        zasadniczy_odsylacz = mf_kw.link_obrazu % dict(
            x = self.szerokosc_obrazu,
            y = self.wysokosc_obrazu,
            nazwa = oc_kw.core_resolver.pelna_generowana_nazwa(self.moja_nazwa),
            rozkaz_mapy = self.rozkaz_mapy,
            html_tmp_name = self.html_name)
        lista.append(zasadniczy_odsylacz)
        return ''.join(lista)

    def zapisz_obraz(self, im, wersja):
        '''
        KlasaObrazu:
        '''
        tmp_nazwa = mf_kw.plik_grafiki(self.tgk.znacznik_unik, self.literka_typu, self.dnw.lp_miejsca, wersja)
        im.save(oc_kw.SciezkaPlikow + tmp_nazwa)

    def rysuj_same_kreski(self, wsp_y_pocz, akt, szerokosc_obrazu):
        '''
        KlasaObrazu:
        '''
        x = self.aqr.poziomo_tego_dnia(akt, self.szerokosc_dx_skali, szerokosc_obrazu)
        self.draw_line.line_with_default_color((x, wsp_y_pocz, x, wsp_y_pocz + oa_kw.DlugoscKresekMiesiecy))

    def wypisz_rzymskie_miesiace(self, akt, nast):
        '''
        KlasaObrazu:
        '''
        NapisMiesiaca = jt_kw.RzymskiDnia(akt)
        wsp_x_napisu = self.aqr.poziomo_tego_dnia((nast + akt) // 2, self.szerokosc_dx_skali, self.szerokosc_obrazu)
        self.my_texts.append(
          (wsp_x_napisu,
            self.gorna_mniejsza,
            NapisMiesiaca,)
        )

    def rzymskie_miesiace_z_kreskami(self, koniec_paska):
        '''
        KlasaObrazu:
        '''
        # Dolne kreski dla poszczególnych miesięcy
        for akt, nast in self.aqr.pary_szkieletu():
            self.rysuj_same_kreski(koniec_paska - oa_kw.DlugoscKresekMiesiecy, akt, self.szerokosc_obrazu)
            self.wypisz_rzymskie_miesiace(akt, nast)

    def rysuj_zebrane_linie(self, draw):
        '''
        KlasaObrazu:
        '''
        self.draw_line.narysuj_na_obrazku(draw)

    def wypisz_zebrane_napisy(self, draw):
        '''
        KlasaObrazu:
        '''
        for x, y, NapisMiesiaca in self.my_texts:
            napis_szer = draw.textsize(NapisMiesiaca)[0]
            x = x - napis_szer // 2
            oa_kw.rj_text(draw, (x, y), NapisMiesiaca)

class TestGenerowaniaObrazu(unittest.TestCase):
    def test_generowania_obrazu(self):
        '''
        TestGenerowaniaObrazu:
        '''
        tgk = od_kw.PseudoTGK()
        tgk.wyznacz_unikalny_moment_dla_grafiki()
        aqr = dq_kw.KlasaOgolnaSzkieletuDat()
        lp_wykresu = 0
        dnw = oh_kw.SimpleDNW(lp_wykresu)
        literka_typu = 'a'
        obk = KlasaObrazu(tgk, aqr, dnw, literka_typu)
        self.assertEqual(obk.literka_typu, 'a')
        self.assertEqual(obk.html_name, 'a0')
