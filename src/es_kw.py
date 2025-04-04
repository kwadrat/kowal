#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lk_kw
import rq_kw
import lm_kw
import hd_kw
import sj_kw
import jb_kw
import hr_kw
import oa_kw
import wn_kw
import ow_kw
import pt_kw

Kolor_Srodka = oa_kw.KOLOR_ZIELONY
Kolor_Srodka = oa_kw.KOLOR_EXCEL_NIEBIESKI
Kolor_umw_Srodka = oa_kw.KOLOR_ZIELONY

# Taką część dostępnej szerokości zajmuje pasek słupka
CzescSlupka = 3

SzerPaska = 90
SzerSlupka = int(float(SzerPaska) / CzescSlupka)  # Szerokość samego słupka

slownik_normalnego_slupka = dict(outline=oa_kw.Kolor_Kresek, fill=Kolor_Srodka)
slownik_przekroczonego_slupka = dict(outline=oa_kw.KOLOR_CZERWONE_RAMKA, fill=oa_kw.KOLOR_CZERWONE_TLO)
slownik_mocy_umownej = dict(fill=Kolor_umw_Srodka)


def prawdziwe_rysowanie(draw, lista_prostokatow, slownik_rect, slownik_przekroczenia=None):
    for tmp_punkt in lista_prostokatow:
        x1, y1, x2, y2 = tmp_punkt.zwroc_cztery_wsp()
        if tmp_punkt.przekroczenie_a_umw and slownik_przekroczenia is not None:
            slownik_efektywny = slownik_przekroczenia
        else:
            slownik_efektywny = slownik_rect
        draw.rectangle((x1, y1, x2, y2), ** slownik_efektywny)


KlasaObrazu = pt_kw.KlasaObrazu


class MojeSlupki(KlasaObrazu):
    def linii_na_dole(self):
        '''
        MojeSlupki:
        '''
        return 1

    def pusta_lista_wszystkiego(self):
        '''
        MojeSlupki:
        '''
        # Napisy do wycentrowania w zadanym punkcie
        self.lista_napisow_wartosci = []
        # Napisy do wstawienia w danym punkcie
        self.lista_napisow_punkt = []
        self.lista_rectangle = []
        self.lista_rect_umw = []
        self.mam_slupki = []

    def CenterNapis(self, SlWspX, SlWspY, napis, jeden_odc_bzw):
        '''
        MojeSlupki:
        '''
        self.lista_napisow_wartosci.append((SlWspX, SlWspY, napis, jeden_odc_bzw))

    def RysujSlupek(self, jeden_slupek):
        '''
        MojeSlupki:
        '''
        SlWspX, DolSlupka, GoraSlupka, Etykieta, yh_value, jeden_odc_bzw = jeden_slupek.zwroc_pelna_krotke()
        Wartosc = yh_value
        half_pillar_width = self.szerokosc_slupka / 2
        x0 = SlWspX - half_pillar_width
        x1 = SlWspX + half_pillar_width
        tmp_punkt = hr_kw.ProstokatDoRysowania(x0, DolSlupka, x1, GoraSlupka)
        if jeden_odc_bzw is not None:
            tmp_punkt.zaznacz_przekroczenie(jeden_odc_bzw.slownik_qm.przekroczenie_b_umw)
        self.lista_rectangle.append(tmp_punkt)
        pozycja_wart_y = GoraSlupka
        if pozycja_wart_y > self.wsp_y_na_dole_slupka:
            pozycja_wart_y = self.wsp_y_na_dole_slupka
        pozycja_wart_y -= oa_kw.wysokosc_napisu
        dotted_txt = lm_kw.rzeczywista_na_napis(Wartosc, rn_after=self.rn_after)
        dotted_txt = hd_kw.comma_and_some_zero(dotted_txt, self.rn_after)
        self.CenterNapis(SlWspX, pozycja_wart_y, dotted_txt, jeden_odc_bzw)
        if Etykieta:
            slownik_qm = wn_kw.KlasaSlownika()
            self.CenterNapis(SlWspX, DolSlupka + 5, Etykieta, jb_kw.JedenOdcinekBazowy(None, None, slownik_qm))

    def RysujListeSlupkow(self):
        self.mam_slupki.sort(key=lambda jeden_slupek: jeden_slupek.klucz_porzadku(), reverse=False)
        for jeden_slupek in self.mam_slupki:
            self.RysujSlupek(jeden_slupek)

    def DodajSlupek(self, jeden_slupek):
        '''
        MojeSlupki:
        '''
        self.mam_slupki.append(jeden_slupek)

    def dodaj_paczke(self, on_real_mouse, pozycja, jeden_odc_bzw):
        '''
        MojeSlupki:
        '''
        # Tylko gdy dostaliśmy prawdziwą fakturę (ciągłą, nie punktową),
        # to prosimy ją o dymek
        if jeden_odc_bzw is not None:
            (px, py, kx, ky) = ow_kw.poszerz_pozycje(self.tgk.jestem_msie, pozycja)
            tekst = jeden_odc_bzw.dymek_dla_slupka(self.chce_bez_tresci)
            tmp_slownik = dict(
                px=px,
                py=py,
                kx=kx,
                ky=ky,
                tekst=tekst,
                )
            self.moja_mapa.append(self.link_mapy(on_real_mouse, tmp_slownik))

    def rysowanie_prostokatow(self, draw):
        '''
        MojeSlupki:
        '''
        prawdziwe_rysowanie(draw, self.lista_rectangle, slownik_normalnego_slupka, slownik_przekroczonego_slupka)

    def rysowanie_prost_umw(self, draw):
        '''
        MojeSlupki:
        '''
        prawdziwe_rysowanie(draw, self.lista_rect_umw, slownik_mocy_umownej)

    def wypisz_napisy_w_rogu(self, draw):
        '''
        MojeSlupki:
        '''
        for x, y, napis in self.lista_napisow_punkt:
            oa_kw.rj_text(draw, (x, y), napis)

    def kolorowanie_faktur_wodociagow(self, slownik_qm, draw, px, py, kx, ky):
        '''
        MojeSlupki:
        '''
        mapowanie_na_lf_lub_f1 = self.tgk.gen_num_faktur.liczba_porz_obiektu_na_obiekt
        wykaz_zaznaczen = []
        for jedna_lista in slownik_qm.jh_values():
            for numer_faktury in jedna_lista:
                dodaj_zaznaczenie = mapowanie_na_lf_lub_f1[numer_faktury].podaj_kolor_zaznaczenia()
                if dodaj_zaznaczenie and dodaj_zaznaczenie not in wykaz_zaznaczen:
                    wykaz_zaznaczen.append(dodaj_zaznaczenie)
        przyrost_ramki = 0
        wykaz_zaznaczen.sort()
        for jedno_zaznaczenie in wykaz_zaznaczen:
            draw.rectangle(
                (px - przyrost_ramki, py - przyrost_ramki, kx + przyrost_ramki, ky + przyrost_ramki),
                outline=jedno_zaznaczenie,
                fill=None,
                )
            przyrost_ramki -= 1

    def wypisz_liczby_otoczone_ramkami(self, draw, on_mouse):
        '''
        MojeSlupki:
        Napisy wartości dodatkowo modyfikujemy - przesunięcie w górę,
        jeśli nachodzą na siebie
        '''
        juz_zuzyte = []
        for x, y, napis, jeden_odc_bzw in self.lista_napisow_wartosci:
            szer, wys = draw.textsize(napis)
            szukaj_kolizji = 1  # Jeszcze nie znalazłem dobrego miejsca dla napisu
            # -------------------------------------------------------------------------
            px = x - szer / 2
            # Napisy wychodzące z lewej strony obrazka wepchnij na obszar widoczny
            if px < 0:
                px = 0
            py = y
            kx = px + szer
            ky = py + wys

            while szukaj_kolizji:
                for ax, ay, bx, by in juz_zuzyte:
                    # Czy w poziomie napisy na siebie nachodzą?
                    if ax < kx and px < bx:
                        # Czy w pionie napisy na siebie nachodzą?
                        if ay < ky and py < by:
                            # Mamy kolizję napisów - robimy korektę
                            delta = ay - ky
                            py += delta
                            ky += delta
                            # Chcemy listę przejrzeć od nowa, bo mogła teraz
                            # wystąpić kolizja z wcześniejszym elementem listy
                            break
                else:
                    # Nie było kolizji, możemy użyć pozycji
                    szukaj_kolizji = 0
                    # Zapamiętaj, że ta pozycja już jest zajęta
                    pozycja = (px, py, kx, ky)
                    juz_zuzyte.append(pozycja)
                    self.dodaj_paczke(on_mouse, pozycja, jeden_odc_bzw)
            slownik_qm = jeden_odc_bzw.slownik_qm
            self.kolorowanie_faktur_wodociagow(slownik_qm, draw, px, py, kx, ky)
            oa_kw.rj_text(draw, (px, py), napis)

    def wykreslanie_slupkow(self, on_mouse):
        '''
        MojeSlupki:
        '''
        moje_tlo = self.dnw.kolor_tla()
        im, draw = self.im_draw(moje_tlo)
        self.rysowanie_prost_umw(draw)
        self.rysowanie_prostokatow(draw)
        self.wypisz_napisy_w_rogu(draw)
        self.wypisz_liczby_otoczone_ramkami(draw, on_mouse)
        self.rysuj_zebrane_linie(draw)
        self.wypisz_zebrane_napisy(draw)
        self.zapisz_obraz(im, ())
        self.pusta_lista_wszystkiego()
        del draw
        return self.link_do_obrazu()

    def dolacz_napis_dla_rogu(self, napis):
        '''
        MojeSlupki:
        '''
        self.lista_napisow_punkt.append((0, 0, napis))

    def brakuje_mi_slupkow(self, IleSlupkow):
        '''
        MojeSlupki:
        '''
        if IleSlupkow <= 0:  # Omijamy wykresy z małą liczbą wartości
            napis = ('Brak danych, kolumn = %(IleSlupkow)s' % dict(
                IleSlupkow=str(IleSlupkow),
                )
            )
        else:
            napis = None
        return napis

    def sprawdz_nietypowe_sytuacje(self, IleSlupkow, vert_axis):
        '''
        MojeSlupki:
        '''
        pracuj = 1
        if pracuj:
            Napis = self.brakuje_mi_slupkow(IleSlupkow)
            if Napis:
                # Informacja o braku danych
                self.dolacz_napis_dla_rogu(Napis)
                pracuj = 0
        if pracuj:
            Napis = vert_axis.zbyt_niski_wykres()
            if Napis:
                # Informacja o za małym zróżnicowaniu danych
                self.dolacz_napis_dla_rogu(Napis)
                pracuj = 0
        return pracuj

    def podpisz_miesiacami(self):
        '''
        MojeSlupki:
        '''
        koniec_paska = self.wysokosc_obrazu
        self.rzymskie_miesiace_z_kreskami(koniec_paska)

    def ustaw_prosty_obraz(self):
        '''
        MojeSlupki:
        Dla skali miesięcznej
        Tyle będzie przedziałów miesięcznych (12 dla punktowych, 15 dla ciągłych faktur)
        '''
        LiczbaPaskow = self.aqr.liczba_paskow()
        if LiczbaPaskow not in rq_kw.PoprawneLiczbyPaskowDlaOkresuMiesiecznego:
            raise RuntimeError('LiczbaPaskow: %d' % LiczbaPaskow)
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz

    def ustaw_skalowany_obraz(self):
        '''
        MojeSlupki:
        Dla skali rocznej
        '''
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz

    def __init__(self, tgk, aqr, dnw, rn_after):
        '''
        MojeSlupki:
        '''
        self.rn_after = rn_after
        KlasaObrazu.__init__(self, tgk, aqr, dnw, lk_kw.LITERA_SLUPEK)
        self.pusta_lista_wszystkiego()
        self.margines_dy_powyzej_slupka = 20
        self.wsp_y_na_dole_slupka = 130
        self.gorna_mniejsza = 140
        self.wysokosc_obrazu = self.gorna_mniejsza + self.linii_na_dole() * oa_kw.wysokosc_napisu
        self.szerokosc_slupka = SzerSlupka
        self.chce_bez_tresci = 0
        self.IleSlupkow = self.dnw.odcinki_bazowe.len_odcinkow_bazowych()  # Tyle rysowanych słupków
        self.ustaw_skalowanie_obrazu()

    def wyznacz_gore_dol_slupka(self, vert_axis, Wartosc):
        '''
        MojeSlupki:
        '''
        gora_slupka = vert_axis.wyznacz_gorna_wartosc(Wartosc)
        GoraSlupka = int(self.wsp_y_na_dole_slupka - (self.wsp_y_na_dole_slupka - self.margines_dy_powyzej_slupka) * gora_slupka)
        DolSlupka = int(self.wsp_y_na_dole_slupka)
        return GoraSlupka, DolSlupka

    def wyznacz_slupki(self, vert_axis):
        '''
        MojeSlupki:
        '''
        pracuj = self.sprawdz_nietypowe_sytuacje(self.IleSlupkow, vert_axis)
        if pracuj:
            moje_paczki_faktur = self.dnw.odcinki_bazowe.p_odc_baz()
            for jeden_odc_bzw in moje_paczki_faktur:
                pocz, kon = jeden_odc_bzw.get_pk()
                SlWspX = self.aqr.miejsce_umieszczenia_slupka(pocz, kon, self.szerokosc_dx_skali, self.szerokosc_obrazu)
                if SlWspX is not None:
                    Wartosc = jeden_odc_bzw.slownik_qm.jh_kwota()
                    GoraSlupka, DolSlupka = self.wyznacz_gore_dol_slupka(vert_axis, Wartosc)
                    Etykieta = self.wyznacz_etykiete(pocz)
                    jeden_slupek = sj_kw.JedenSlupek(SlWspX, DolSlupka, GoraSlupka, Etykieta, Wartosc, jeden_odc_bzw)
                    self.DodajSlupek(jeden_slupek)
            self.RysujListeSlupkow()

    def wyznacz_ukw_slupki(self, vert_axis):
        '''
        MojeSlupki:
        Rysowanie mocy zamówionej jako tło - dla porównania z mocami pobranymi
        '''
        pracuj = self.sprawdz_nietypowe_sytuacje(self.IleSlupkow, vert_axis)
        if pracuj:
            moje_paczki_faktur = self.dnw.odcinki_bazowe.p_odc_baz()
            for jeden_odc_bzw in moje_paczki_faktur:
                pocz, kon = jeden_odc_bzw.get_pk()
                SlWspX1 = self.aqr.miejsce_umieszczenia_slupka(pocz, pocz, self.szerokosc_dx_skali, self.szerokosc_obrazu)
                SlWspX2 = self.aqr.miejsce_umieszczenia_slupka(kon, kon, self.szerokosc_dx_skali, self.szerokosc_obrazu)
                Wartosc = jeden_odc_bzw.slownik_qm.umw_wartosc_s_qm
                if SlWspX1 is not None and SlWspX2 is not None and Wartosc is not None:
                    GoraSlupka, DolSlupka = self.wyznacz_gore_dol_slupka(vert_axis, Wartosc)
                    tmp_punkt = hr_kw.ProstokatDoRysowania(SlWspX1, GoraSlupka, SlWspX2, DolSlupka)
                    self.lista_rect_umw.append(tmp_punkt)


class TestMoichSlupkow(unittest.TestCase):
    def test_moich_slupkow(self):
        '''
        TestMoichSlupkow:
        '''
        self.assertEqual(CzescSlupka, 3)
        self.assertEqual(SzerPaska, 90)
        self.assertEqual(SzerSlupka, 30)
