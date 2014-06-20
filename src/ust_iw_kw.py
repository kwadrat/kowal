#!/usr/bin/python
# -*- coding: UTF-8 -*-

TymczasowoM0 = 0
TymczasowoM1 = 1

# Czy chcemy widzieć wizualizację faktury
TymczasowoSzczegolowaWizualizacja = 0

LokalnaDiagnostykaKlas = 0 and TymczasowoSzczegolowaWizualizacja

# Wizualizacja działania nadliczników
TymczasowoWizualizacjaNadlicznikow = 0 and TymczasowoSzczegolowaWizualizacja

DocelowoZmieniajPochodneFaktury = 1

# Wizualizacja działania słowników zapalających licznikowane,
# czyli dopasowania wody i ścieków
TymczasowoWizualizacjaLicznikowanych = 0 and TymczasowoSzczegolowaWizualizacja

# Włącz wizualizację dopasowywania faktur zwykłych i korygujących
TymczasowoWizualizacjaZestawuFaktur = 1 and TymczasowoSzczegolowaWizualizacja

# Pokaz wynikowych słowników
WyswietlWynikoweSlowniki = 0

# Pokaz zapytań SQL
TymczasowoPokazSQL = 1
