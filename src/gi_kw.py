#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Generator instrukcji do przesyłania plików zdjęć/audytów/dokumentacji.
'''

wybierz_obiekt = 'wybierz obiekt'
wyczysc_edycje = 'odznacz (wyczyść) pole "Zezwolenie na edycję plików i katalogów"'
zaznacz_edycje = 'zaznacz (wypełnij) pole "Zezwolenie na edycję plików i katalogów"'
nacisnij_wykonaj = 'naciśnij przycisk "Wykonaj"'
opcjonalnie_zmien_biezacy_na_operacje = 'jeśli jest widoczne pole "Katalog bieżący", to wybierz "operacje na katalogach" i naciśnij "Wykonaj"'
zmien_biezacy_poza_operacje = 'w polu "Katalog bieżący" wybierz nazwę wcześniej założonego katalogu'
wczesniej_zaloz_katalog = 'przed wgrywaniem plików należy wcześniej utworzyć przynajmniej jeden katalog'
kliknij_link_nazwy_katalogu = 'wskaż nazwę katalogu'
kliknij_link_nazwy_pliku = 'wskaż nazwę pliku'
wpisz_nowy_katalog = 'wpisz nazwę nowego katalogu w "Załóż nowy katalog"'
zaznacz_wybrane_katalogi = 'zaznacz (wypełnij) w dolnej tabelce pola "Zaznaczenie" przy interesujących katalogach'
zaznacz_wybrane_pliki = 'zaznacz (wypełnij) w dolnej tabelce pola "Zaznaczenie" przy interesujących plikach'
zaznacz_opcje_zmiany_nazwy = 'wybierz w górnej tabelce w polu "Dla zaznaczonych plików" opcję "Zmień nazwę"'
zaznacz_opcje_kasowania = 'wybierz w górnej tabelce w polu "Dla zaznaczonych plików" opcję "Usuń"'
nowa_nazwa_w_dolnej_tabelce = 'w dolnej tabelce wpisz w pierwszej kolumnie nową nazwę'
nowe_nazwy_plikow_w_dolnej_tabelce = 'w dolnej tabelce w pierwszej kolumnie popraw nazwy plików'
nacisnij_wybierz = 'w polu "Wybierz plik" wskaż plik do wgrania przez naciśnięcie przycisku "Wybierz..."'
logowanie_do_systemu = 'uruchom przeglądarkę internetową i zaloguj się do systemu Media'
uruchom_gr = 'znajdź na pulpicie komputera program o nazwie "gr_kw.py" i uruchom go'
nacisnij_kod = 'naciśnij przycisk "Wprowadź kod"'
znajdz_ramke = 'po lewej stronie, poniżej menu, znajdź ramkę z informacją o logowaniach do systemu'
zaznacz_kod = 'zaznacz myszką kod umieszczony drobnymi literami na dole ramki'
ctrl_c = 'skopiuj kod za pomocą kombinacji klawiszy "Ctrl-C"'
ctrl_v = 'wklej kod za pomocą kombinacji klawiszy "Ctrl-V"'
enter = 'naciśnij klawisz "Enter"'
wybor_w_drzewie = 'W lewej części okna (która pokazuje drzewo obiektów i katalogów) wybierz obiekt'
wybor_iza = 'wybierz inwentaryzację, zdjęcia lub audyt'
wybor_katalog = 'wybierz jeden z wcześniej założonych katalogów'
uruchom_we = 'uruchom program "Mój komputer" (ikonka znajduje się na pulpicie komputera)'
zmien_we = 'przejdź do katalogu, gdzie są umieszczone pliki do wgrania na serwer'
zaznacz = 'zaznacz w Eksploratorze Windows wiele plików (nie wolno jeszcze zaznaczać katalogów) przeznaczonych do wgrania na serwer'
przeciagnij = 'przeciągnij myszką pliki na okno "Pliki" umieszczone po prawej stronie'
zadania = [
    [
        'Zakładanie katalogu',
        [
            wybierz_obiekt,
            zaznacz_edycje,
            nacisnij_wykonaj,
            opcjonalnie_zmien_biezacy_na_operacje,
            wpisz_nowy_katalog,
            nacisnij_wykonaj,
            ],
        ],
    [
        'Zmienianie nazwy katalogu',
        [
            wybierz_obiekt,
            zaznacz_edycje,
            nacisnij_wykonaj,
            opcjonalnie_zmien_biezacy_na_operacje,
            zaznacz_wybrane_katalogi,
            zaznacz_opcje_zmiany_nazwy,
            nacisnij_wykonaj,
            nowa_nazwa_w_dolnej_tabelce,
            nacisnij_wykonaj,
            ],
        ],
    [
        'Kasowanie katalogu',
        [
            wybierz_obiekt,
            zaznacz_edycje,
            nacisnij_wykonaj,
            opcjonalnie_zmien_biezacy_na_operacje,
            zaznacz_wybrane_katalogi,
            zaznacz_opcje_kasowania,
            nacisnij_wykonaj,
            ],
        ],
    [
        'Wgrywanie jednego pliku',
        [
            wczesniej_zaloz_katalog,
            wybierz_obiekt,
            zaznacz_edycje,
            nacisnij_wykonaj,
            zmien_biezacy_poza_operacje,
            nacisnij_wykonaj,
            nacisnij_wybierz,
            nacisnij_wykonaj,
            ],
        ],
    [
        'Pobieranie pliku',
        [
            wybierz_obiekt,
            wyczysc_edycje,
            nacisnij_wykonaj,
            kliknij_link_nazwy_katalogu,
            nacisnij_wykonaj,
            kliknij_link_nazwy_pliku,
            ],
        ],
    [
        'Zmienianie nazw plików',
        [
            wybierz_obiekt,
            zaznacz_edycje,
            nacisnij_wykonaj,
            zmien_biezacy_poza_operacje,
            nacisnij_wykonaj,
            zaznacz_wybrane_pliki,
            zaznacz_opcje_zmiany_nazwy,
            nacisnij_wykonaj,
            nowe_nazwy_plikow_w_dolnej_tabelce,
            nacisnij_wykonaj,
            ],
        ],
    [
        'Usuwanie plików',
        [
            wybierz_obiekt,
            zaznacz_edycje,
            nacisnij_wykonaj,
            zmien_biezacy_poza_operacje,
            nacisnij_wykonaj,
            zaznacz_wybrane_pliki,
            zaznacz_opcje_kasowania,
            nacisnij_wykonaj,
            ],
        ],
    [
        'Wgrywanie wielu plików (wymaga osobnego programu)',
        [
            logowanie_do_systemu,
            znajdz_ramke,
            zaznacz_kod,
            ctrl_c,

            uruchom_gr,
            nacisnij_kod,

            ctrl_v,
            enter,
            wybor_w_drzewie,
            wybor_iza,
            wybor_katalog,
            uruchom_we,
            zmien_we,
            zaznacz,
            przeciagnij,
            ],
        ],
    ]


def Wykonaj():
    for nr_zad, lista_zadania in enumerate(zadania):
        tytul_zadania = lista_zadania[0]
        kroki_zadania = lista_zadania[1]
        ostatni_punkt = len(kroki_zadania) - 1
        print('Operacja %d - %s:' % (nr_zad + 1, tytul_zadania))
        for nr, tekst in enumerate(kroki_zadania):
            if nr == ostatni_punkt:
                znak_koncowy = '.'
            else:
                znak_koncowy = ';'
            print('  %d. %s%s' % (nr + 1, tekst, znak_koncowy))
        print('')


if __name__ == '__main__':
    Wykonaj()
