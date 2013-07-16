#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Operacje generowania obrazu
Lewy, górny róg obrazka ma współrzędne (0, 0)
'''

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import ls_kw
import dn_kw
import oa_kw
import dq_kw
import oh_kw
import oc_kw
import mf_kw
import od_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

link_area_pocz = '''<area shape="rect" coords="%(px)d,%(py)d,%(kx)d,%(ky)d"\n'''
link_area_alt_title = ''' alt="%(tekst)s" title="%(tekst)s"'''
link_area_kon = ''' />\n'''
link_area_alter_this = ''' onMouseOver="%(over)s"\n onMouseOut="%(out)s"\n'''

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
        self.draw_line = []
        self.my_texts = []
        self.tgk = tgk
        self.aqr = aqr
        self.dnw = dnw
        self.literka_typu = literka_typu
        self.szerokosc_dx_skali = 0
        self.moja_nazwa = mf_kw.plik_grafiki(self.tgk, self.literka_typu, self.dnw.lp_miejsca, ())
        self.html_name = self.html_my_name(self.literka_typu, self.dnw.lp_miejsca)

    def chce_po_lewej_miejsca_na_skale(self, ile_pikseli):
        '''
        KlasaObrazu:
        '''
        self.szerokosc_dx_skali = ile_pikseli

    def link_mapy(self, on_mouse, slownik):
        '''
        KlasaObrazu:
        '''
        wynik = []
        self.tgk.zmniejsz_obszar_aktywny_dla_firefox(slownik)
        # Początek i współrzędne obszaru
        wynik.append(link_area_pocz % slownik)
        # Zmiana aktualnego obrazka
        lista_over = []
        lista_out = []
        if 'nowy_this' in slownik:
            lista_over.append("%s.src='%s'" % (self.html_name, oc_kw.pelna_generowana_nazwa(slownik['nowy_this'])))
            lista_out.append("%s.src='%s'" % (self.html_name, oc_kw.pelna_generowana_nazwa(self.moja_nazwa)))
        if oc_kw.EYK_lporz_fktr in slownik:
            moj_nr_faktury = slownik[oc_kw.EYK_lporz_fktr]
            etyk = mf_kw.nazwa_wiersza(moj_nr_faktury)
            lista_over.append("%s.bgColor='%s'" % (etyk, oa_kw.HEX_ZIELONY))
            lista_out.append("%s.bgColor='%s'" % (etyk,oa_kw.HEX_BIALY))
            if lc_kw.fq_tekst_qv not in slownik:
                slownik[lc_kw.fq_tekst_qv] = 'Faktura: %d' % moj_nr_faktury
        if lista_over or lista_out:
            zmiany = dict(
            over = ';'.join(lista_over),
            out = ';'.join(lista_out),
            )
            on_the_mouse = link_area_alter_this % zmiany
            wynik.append(on_the_mouse)
            if oc_kw.EYK_lporz_fktr in slownik:
                on_mouse[slownik[oc_kw.EYK_lporz_fktr]] = on_the_mouse
        # Dymek (opcjonalny)
        if lc_kw.fq_tekst_qv in slownik:
            wynik.append(link_area_alt_title % slownik)
        # Zakończenie adresu
        wynik.append(link_area_kon)
        return ''.join(wynik)

    def html_my_name(self, literka, lp_miejsca):
        '''
        KlasaObrazu:
        '''
        return '%s%d' % (literka, lp_miejsca)

    def im_draw(self, tlo):
        '''
        KlasaObrazu:
        '''
        return ls_kw.prepare_new_image('RGB', (self.szerokosc_obrazu, self.wysokosc_obrazu), tlo)

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
            nazwa = oc_kw.pelna_generowana_nazwa(self.moja_nazwa),
            rozkaz_mapy = self.rozkaz_mapy,
            html_tmp_name = self.html_name)
        lista.append(zasadniczy_odsylacz)
        return ''.join(lista)

    def zapisz_obraz(self, im, wersja):
        '''
        KlasaObrazu:
        '''
        tmp_nazwa = mf_kw.plik_grafiki(self.tgk, self.literka_typu, self.dnw.lp_miejsca, wersja)
        im.save(oc_kw.SciezkaPlikow + tmp_nazwa)

    def rysuj_same_kreski(self, koniec_paska, akt, szerokosc_obrazu):
        '''
        KlasaObrazu:
        '''
        x = self.aqr.poziomo_tego_dnia(akt, self.szerokosc_dx_skali, szerokosc_obrazu)
        self.draw_line.append(((x, koniec_paska - oa_kw.DlugoscKresekMiesiecy, x, koniec_paska),
          oa_kw.Kolor_Kresek))

    def wypisz_rzymskie_miesiace(self, poczatek_napisu, akt, nast):
        '''
        KlasaObrazu:
        '''
        NapisMiesiaca = dn_kw.RzymskiDnia(akt)
        wsp_x_napisu = self.aqr.poziomo_tego_dnia((nast + akt) // 2, self.szerokosc_dx_skali, self.szerokosc_obrazu)
        self.my_texts.append(
          (wsp_x_napisu,
            poczatek_napisu,
            NapisMiesiaca,)
        )

    def rzymskie_miesiace_z_kreskami(self, koniec_paska, poczatek_napisu):
        '''
        KlasaObrazu:
        '''
        # Dolne kreski dla poszczególnych miesięcy
        for akt, nast in self.aqr.pary_szkieletu():
            self.rysuj_same_kreski(koniec_paska, akt, self.szerokosc_obrazu)
            self.wypisz_rzymskie_miesiace(poczatek_napisu, akt, nast)

    def rysuj_zebrane_linie(self, draw):
        '''
        KlasaObrazu:
        '''
        for polozenie, kolor in self.draw_line:
            draw.line(polozenie, kolor)

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
