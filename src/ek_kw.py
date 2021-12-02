#!/usr/bin/python
# -*- coding: UTF-8 -*-

ETK_jedna_faktura = 'etk_jedna_faktura'
ETK_pozycje_licznikowane = 'etk_pozycje_licznikowane'
ETK_pozycje_sztukowane = 'etk_pozycje_sztukowane'
ETK_maly_licznik_odczyty = 'etk_maly_licznik_odczyty'
ETK_maly_licznik_dane_wazn_faktury = 'etk_maly_licznik_dane_wazn_faktury'
ETK_maly_licznik_znajdz_lub_przygotuj = 'etk_maly_licznik_znajdz_lub_przygotuj'
ETK_maly_licznik_znajdz_ogolny = 'etk_maly_licznik_znajdz_ogolny'
ETK_maly_licznik_znajdz_szczegolowy = 'etk_maly_licznik_znajdz_szczegolowy'
ETK_nadlicznik_slownik_towaru = 'nadlicznik_slownik_towaru'
ETK_nadlicznik_dane_ogolne = 'nadlicznik_dane_ogolne'
ETK_slownik_wszystkich_odczytow_nadlicznika = 'slownik_wszystkich_odczytow_nadlicznika'
ETK_nadlicznik_slow_przez_daty = 'nadlicznik_slow_przez_daty'
ETK_unikalne_nadlicznika = 'unikalne_nadlicznika'
ETK_scieki_dla_wody = 'etk_scieki_dla_wody'
ETK_lista_znajdz_lub_przygotuj = 'lista_znajdz_lub_przygotuj'
ETK_lista_indeksow_wagonikow = 'lista_indeksow_wagonikow'

# Zbiór linii pozycji, które pojawiły się w zestawieniu
zbr_licznik_linii = 'lil'  # Tyle razy linia była powtórzona w pliku XML (lub CSV)
zbr_podlaczeni_klienci = 'pdk'  # Tacy klienci wzięli od nas zużycie
zbr_realny_wyplyw = 'rwp'  # Ile wypłynęło z nadlicznika po odjęciu zużycia w podlicznikach
zbr_moj_klucz = 'mkl'  # Jaki jest mój klucz dla odczytu
zbr_to_nadrzedny = 'ndr'  # Czy jestem nadrzędnym licznikiem

pola_dodatkowe_slownikow = frozenset([
    zbr_licznik_linii,
    zbr_podlaczeni_klienci,
    zbr_realny_wyplyw,
    zbr_moj_klucz,
    zbr_to_nadrzedny,
    ])
