#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import oo_kw
import lk_kw
import dn_kw
import oa_kw
import mf_kw
import pt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

Kolor_Przyszlosc = oa_kw.KOLOR_JASNYSZARY
Kolor_Bledny = oa_kw.KOLOR_CZERWONY
Kolor_Poprawny = oa_kw.KOLOR_ZIELONY

# Dla górnych kresek (faktur) kreski będą dłuższe
DlugoscKresekFaktur = 6

KlasaObrazu = pt_kw.KlasaObrazu

class MojPasek(KlasaObrazu):
    '''Rysowanie paska wypełnienia poszczególnych miesięcy fakturami
    '''
    def pasek_podstawowy(self, lista, koniec_paska):
        '''
        MojPasek:
        Pasek podstawowy:
        - zielony - są faktury
        - czerwony - brak faktur
        - szary - dzień jest w przyszłości
        '''
        przyszlosc = dn_kw.NumerDzisiaj() + 1
        for i in self.aqr.kolejne_dni_szkieletu():
            if i in lista:
                kolor = Kolor_Poprawny
            else:
                if i >= przyszlosc:
                    kolor = Kolor_Przyszlosc
                else:
                    kolor = Kolor_Bledny
            x_pocz = self.aqr.poziomo_tego_dnia(i, self.szerokosc_skali, self.szerokosc_obrazu)
            x_kon = self.aqr.poziomo_tego_dnia(i + 1, self.szerokosc_skali, self.szerokosc_obrazu)
            for f in xrange(x_pocz, x_kon):
                self.draw_line.append(((f, self.pocz_paska, f, koniec_paska), kolor))

    def kreski_dla_faktur(self):
        '''
        MojPasek:
        '''
        # Początek dla kresek oznaczających okresy faktur
        pocz_kres_okr = self.pocz_paska
        kon_kres_okr = pocz_kres_okr + DlugoscKresekFaktur
        if self.aqr.mam_dat_na_dluzszy_rok():
            for akt in self.dwk.odcinki_bazowe.lista_pocz():
                if akt != None:
                    tmp_x = self.aqr.poziomo_tego_dnia(akt, self.szerokosc_skali, self.szerokosc_obrazu)
                    self.draw_line.append(((tmp_x, pocz_kres_okr, tmp_x, kon_kres_okr),
                      oa_kw.Kolor_Kresek))

    def __init__(self, lista, tgk, aqr, dwk, dnw):
        '''
        MojPasek:
        - linia z napisem "Okresy rozliczeniowe"
        - barwny pasek z fakturami
        - rzymskie numery dla miesięcy
        Założenie: assert tgk.okres_miesiac
        Wycentrowanie w osi X napisów miesięcy
        Parametry:
        lista - lista dni dla wszystkich faktur
        '''
        KlasaObrazu.__init__(self, tgk, aqr, dwk, dnw, lk_kw.LITERA_PASEK)
        self.szerokosc_obrazu = oa_kw.sk_pelny_obraz
        pocz_okr_rozlicz = 0 # Początek dla "Okresy rozliczeniowe"
        kon_okr_rozlicz = pocz_okr_rozlicz + oa_kw.wysokosc_napisu
        self.pocz_paska = kon_okr_rozlicz # Od tego piksela zaczyna się pasek
        self.wys_paska = 20 # Wysokość rysowanego paska
        # Koniec paska w osi Y (niżej niż początek, bo ma większą wartość)
        koniec_paska = self.pocz_paska + self.wys_paska
        poczatek_napisu = koniec_paska
        self.wysokosc_obrazu = poczatek_napisu + oa_kw.wysokosc_napisu
        # Wypisz na środku etykietę okresów rozliczeniowych
        self.my_texts.append((self.szerokosc_obrazu / 2, pocz_okr_rozlicz, 'Okresy rozliczeniowe'))
        self.pasek_podstawowy(lista, koniec_paska)
        self.rzymskie_miesiace_z_kreskami(koniec_paska, poczatek_napisu)
        self.kreski_dla_faktur()

    def rysuj_prostokat(self, draw, lg_x, lg_y, pd_x, pd_y, kolor):
        '''
        MojPasek:
        '''
        # Korekta współrzędnych poza obrazem
        pd_x -= 1
        pd_y -= 1
        if lg_x <= pd_x and lg_y <= pd_y:
            draw.rectangle((lg_x, lg_y, pd_x, pd_y), kolor)

    def dodaj_mouse_over(self, on_mouse, lg_x, lg_y, pd_x, pd_y, wersja):
        '''
        MojPasek:
        '''
        tmp_nazwa2 = mf_kw.plik_grafiki(self.tgk, self.literka_typu, self.dnw.lp_miejsca, wersja)
        slownik = dict(
          px = lg_x,
          py = lg_y,
          kx = pd_x,
          ky = pd_y,
          nowy_this = tmp_nazwa2,
          lp_faktury = wersja[0], # wersja to jednoelementowa lista l.p. faktur
        )
        self.moja_mapa.append(self.link_mapy(on_mouse, slownik))

    def zaznacz_faktury(self, draw, wersja, on_mouse, kolor):
        '''
        MojPasek:
        '''
        mam_jedna_wersje = (len(wersja) == 1)
        momenty = self.dwk.zbitki_qm.keys()
        momenty.sort()
        # czas_t0 - początek całej skali czasowej
        czas_t0 = czas_akt = momenty[0]
        czas_tn = momenty[-1]
        for czas_nast in momenty[1:]:
            faktury = self.dwk.zbitki_qm[czas_akt]
            ile_faktur = len(faktury)
            for nr_kol in range(ile_faktur):
                lp_faktury = faktury[nr_kol]
                # Czy rysować daną fakturę
                if lp_faktury in wersja:
                    # Współrzędne lewego górnego rogu (włącznie)
                    lg_x = oa_kw.poziomo_dla_dni(czas_t0, czas_akt, czas_tn, self.szerokosc_skali, self.szerokosc_obrazu)
                    lg_y = self.pocz_paska + (nr_kol * self.wys_paska) / ile_faktur
                    # Współrzędne prawego dolnego rogu (już poza obszarem)
                    pd_x = oa_kw.poziomo_dla_dni(czas_t0, czas_nast, czas_tn, self.szerokosc_skali, self.szerokosc_obrazu)
                    pd_y = self.pocz_paska + ((nr_kol + 1) * self.wys_paska) / ile_faktur
                    self.rysuj_prostokat(draw, lg_x, lg_y, pd_x, pd_y, kolor)
                    # Gdy podano tylko jedną l.p. faktury, to znaczy, że możemy
                    # wygenerować zmianę (obrazka, słupka, tabelki) dla myszy nad tym obszarem
                    if mam_jedna_wersje:
                        self.dodaj_mouse_over(on_mouse, lg_x, lg_y, pd_x, pd_y, wersja)
            czas_akt = czas_nast

    def dla_jednej_zaznaczonej_faktury(self, im, wersja, on_mouse):
        '''
        MojPasek:
        '''
        im2, draw2 = self.kopia_obrazu(im)
        self.zaznacz_faktury(draw2, wersja, on_mouse, oa_kw.KOLOR_CZARNY)
        self.zapisz_obraz(im2, wersja)
        del draw2
        del im2

    def wersje_kolejno_zaznaczonych_faktur(self, im, on_mouse):
        '''
        MojPasek:
        '''
        if oo_kw.DocelowoOsobneDane:
            ##############################################################################
            for wersja in self.dnw.odmiany_grafiki:
                self.dla_jednej_zaznaczonej_faktury(im, wersja, on_mouse)
            ##############################################################################
        else:
            ##############################################################################
            for wersja in self.dwk.odmiany_grafiki:
                self.dla_jednej_zaznaczonej_faktury(im, wersja, on_mouse)
            ##############################################################################

    def wykreslanie_paska(self, on_mouse):
        '''
        MojPasek:
        Wykreślanie elementów rysunku
        '''
        im, draw = self.im_draw(oa_kw.KOLOR_BIALY)
        self.rysuj_zebrane_linie(draw)
        self.wypisz_zebrane_napisy(draw)
        self.zapisz_obraz(im, ())
        del draw
        self.wersje_kolejno_zaznaczonych_faktur(im, on_mouse)
        del im
        return self.link_do_obrazu()
