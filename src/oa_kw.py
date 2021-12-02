#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


# Stałe kolorów
KOLOR_ZIELONY = (0, 255, 0)
KOLOR_CIEMNY_ZIELONY = (0, 128, 0)
KOLOR_CZERWONY = (255, 0, 0)
KOLOR_ZOLTY = (255, 255, 0)
KOLOR_SZARY = (128, 128, 128)
KOLOR_JASNYSZARY = (240, 240, 240)
KOLOR_MNIEJ_JASNYSZARY = (216, 216, 216)
KOLOR_AMIGA = (0x66, 0x88, 0xAA)
KOLOR_BIALY = (255, 255, 255)
KOLOR_CZARNY = (0, 0, 0)
KOLOR_EXCEL_NIEBIESKI = (153, 153, 255)
KOLOR_EXCEL_TLO_SZARE = (192, 192, 192)
KOLOR_TLO_SELEDYN = (20, 212, 212)
# Kolor testowy dla tła automatycznie wprowadzonej faktury dla wodociągów
KOLOR_TLO_ATMT_ZOLTE = (255, 255, 0)  # Yellow
KOLOR_TLO_ATMT_PURPUROWE = (255, 0, 255)  # Magenta
KOLOR_TLO_ATMT_TURKUSOWE = (0, 255, 255)  # Cyan
KOLOR_TLO_SELEDYNOWY_ROK = (204, 255, 255)
Format_Koloru = '#%02X%02X%02X'
HEX_BIALY = Format_Koloru % KOLOR_BIALY
HEX_ZIELONY = Format_Koloru % KOLOR_ZIELONY
HEX_TLO_ATMT_ZOLTE = Format_Koloru % KOLOR_TLO_ATMT_ZOLTE
HEX_TLO_ATMT_PURPUROWE = Format_Koloru % KOLOR_TLO_ATMT_PURPUROWE
HEX_TLO_ATMT_TURKUSOWE = Format_Koloru % KOLOR_TLO_ATMT_TURKUSOWE
HEX_TLO_SELEDYNOWY_ROK = Format_Koloru % KOLOR_TLO_SELEDYNOWY_ROK

# Kolory tła dla poszczególnych mediów
MDM_GAZ_ZOLTY = KOLOR_ZOLTY
MDM_WODA_NIEBIESKI = KOLOR_EXCEL_NIEBIESKI
MDM_PRAD_CZERWONY = KOLOR_CZERWONY
MDM_CIEPLO_ZIELONY = KOLOR_ZIELONY
MDM_OLEJ_FIOLET = (229, 35, 247)
MDM_WEGIEL_CIEMNO_SZARY = KOLOR_EXCEL_TLO_SZARE
# MDM_SZAMBO_CIEMNY_CZERW = (209, 104, 118)
# MDM_SZAMBO_CIEMNY_CZERW = (75, 0, 130) # Indygo
MDM_SZAMBO_CIEMNY_CZERW = (0, 255, 255)  # Seledynowy

Kolor_Kresek = KOLOR_SZARY

Kolor_Napisow = KOLOR_CZARNY

KOLOR_CZERWONE_RAMKA = (153, 0, 0)
KOLOR_CZERWONE_TLO = (192, 0, 0)

# Każdy dzień będzie jako 2 punkty - wtedy 365 dni w roku
# zmieści się w poziomie na ekranie 1024x768
sk_pelny_obraz = 1250

# Długość kresek zaznaczających poszczególne miesiące lub lata
DlugoscKresekMiesiecy = 3

# Wysokość linii z napisem
wysokosc_napisu = 10  # draw.textsize('0')[1]


def poziomo_dla_dni(min_domain, akt, max_domain, min_pixels, max_pixels):
    return int(
        min_pixels
        + (akt - min_domain)
        * (max_pixels - min_pixels)
        / (max_domain - min_domain)
        )


def zaokraglij_mi(all_points, small_part):
    return all_points - (all_points % small_part)


def rj_text(draw, place, message):
    draw.text(place, message, fill=Kolor_Napisow)


class TestRozmiaruObrazu(unittest.TestCase):
    def test_rozmiaru_obrazu(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(sk_pelny_obraz, 1250)
        self.assertEqual(wysokosc_napisu, 10)

    def test_szkieletowego_datownika(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(poziomo_dla_dni(1, 4, 4, 0, 3), 3)
        self.assertEqual(poziomo_dla_dni(0, 0, 4, 1, 3), 1)
        self.assertEqual(poziomo_dla_dni(0, 31 + 365 + 31 + 29, 31 + 365 + 31 + 29, 0, sk_pelny_obraz), sk_pelny_obraz)

    def test_szkieletowego_zaokraglenia(self):
        '''
        TestRozmiaruObrazu:
        '''
        self.assertEqual(zaokraglij_mi(96, 96), 96)
        self.assertEqual(zaokraglij_mi(96 + 95, 96), 96)
        self.assertEqual(zaokraglij_mi(96 + 96, 96), 192)
