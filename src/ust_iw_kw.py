#!/usr/bin/python
# -*- coding: UTF-8 -*-

TymczasowoM0 = 0
TymczasowoM1 = 1

# Tymczasowa zmienna, docelowo ma być zmieniona na 1,
# gdy zostanie dopracowana weryfikacja faktur G-3
# na kwotę 804.04 zł: 00/03836/2010, K80/00055/2010
DocelowoNowyKodDlaKorekt = 1

# Czy chcemy widzieć wizualizację faktury
TymczasowoSzczegolowaWizualizacja = 0

LokalnaDiagnostykaKlas = 0 and TymczasowoSzczegolowaWizualizacja

# Wizualizacja działania nadliczników
TymczasowoWizualizacjaNadlicznikow = 0 and TymczasowoSzczegolowaWizualizacja

DocelowoZmieniajPochodneFaktury = 1 and DocelowoNowyKodDlaKorekt

# Wizualizacja działania słowników zapalających licznikowane,
# czyli dopasowania wody i ścieków
TymczasowoWizualizacjaLicznikowanych = 0 and TymczasowoSzczegolowaWizualizacja

# Włącz wizualizację dopasowywania faktur zwykłych i korygujących
TymczasowoWizualizacjaZestawuFaktur = 1 and TymczasowoSzczegolowaWizualizacja

# Pokaz wynikowych słowników
WyswietlWynikoweSlowniki = 0

# Pokaz zapytań SQL
TymczasowoPokazSQL = 1
