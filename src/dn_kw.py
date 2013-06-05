#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import rq_kw
import du_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

SEC_PER_DAY = 24 * 60 * 60

tab_miesiecy = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień',]

tab_rzymskich = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
  'XI', 'XII']

dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela',]

dm_rk_baz = 2005 # Domyślny rok bazowy
dm_rk_hst = 2006 # Domyślny rok początkowy dla historii logowań

data_testowa_a = 1314612000 # 2011.08.29_12.00.00
data_testowa_b = 1288346400 # 2010.10.29_12.00.00
data_testowa_c = 1323769292 # 2011.12.13_10.41.32

def nazwa_rzymskiego(numer):
    return tab_rzymskich[numer - 1]

def rok_liczba(czas = None):
    return time.localtime(czas).tm_year

def miesiac_liczba(czas = None):
    return time.localtime(czas).tm_mon

def dzien_liczba(czas = None):
    return time.localtime(czas).tm_mday

def rok_sekundy(czas = None):
    rok = rok_liczba(czas)
    return str(rok)

def data_rmd(czas = None):
    krotka_daty = time.localtime(czas)
    rok = krotka_daty.tm_year
    miesiac = krotka_daty.tm_mon
    dzien = krotka_daty.tm_mday
    return (rok, miesiac, dzien)

def wyznacz_dzisiejsza_date(czas = None):
    krotka_daty = time.localtime(czas)
    rok = krotka_daty.tm_year
    miesiac = krotka_daty.tm_mon
    dzien = krotka_daty.tm_mday
    dz_tygodnia = krotka_daty.tm_wday
    napis_daty = '%(tygodnia)s, %(dzien)d %(miesiac)s, %(rok)d' % dict(
      tygodnia = dni_tygodnia[dz_tygodnia],
      rok = rok,
      miesiac = tab_miesiecy[miesiac - 1],
      dzien = dzien)
    return napis_daty

def NumerDnia(rok, miesiac, dzien):
    '''Zwraca numer dnia począwszy od 1 stycznia 1970
    Parametry:
    rok, miesiac, dzien - opis interesującego nas dnia
    Wartość zwracana:
    int - numer dnia
    '''
    try:
        try:
            numer = int(
              time.mktime((rok, miesiac, dzien, 12, 0, 0, 0, 0, 0)) /
              SEC_PER_DAY)
        except OverflowError:
            raise OverflowError('Problem z: "%s"' % repr((rok, miesiac, dzien)))
    except TypeError:
        raise TypeError('Problem z: "%s"' % repr((rok, miesiac, dzien)))
    return numer

def dzien_nowego_miesiaca(rok, miesiac):
    '''Zwraca numer pierwszego dnia podanego roku
    '''
    return NumerDnia(rok, miesiac, 1)

def dzien_nowego_roku(rok):
    '''Zwraca numer pierwszego dnia podanego roku
    '''
    return NumerDnia(rok, 1, 1)

def napis_na_numer_dnia(data):
    '''Zwraca numer dnia począwszy od 1 stycznia 1970
    Parametr:
    data - napis w formacie '2008-10-16'
    Wartość zwracana:
    int - numer dnia
    '''
    if type(data) is tuple:
        rok, miesiac, dzien = data
    else:
        rok, miesiac, dzien = data_z_napisu(data)
    return NumerDnia(rok, miesiac, dzien)

def CzasDzisiaj():
    '''
    Wyznacza dzień i moment w dniu:
    - rok, miesiąc, dzień
    - godzina, minuta, sekunda
    '''
    return time.localtime()[:6]

def DataDzisiaj():
    '''
    Wyznacza dzień:
    - rok, miesiąc, dzień
    '''
    return CzasDzisiaj()[:3]

def RokDzisiaj():
    '''
    Zwraca liczbę - aktualny rok
    '''
    return CzasDzisiaj()[0]

def RokTeraz():
    '''
    Wyznacza rok w postaci napisu: RRRR
    '''
    return str(RokDzisiaj())

RokObecnyStaly = RokDzisiaj()
MozliweLataZuzyc = map(str, range(RokObecnyStaly, rq_kw.RokPocz2 - 1, -1))
MozliweLataFaktur = map(str, range(RokObecnyStaly + 1, rq_kw.RokPocz2 - 1, -1))
MozliweLataDlaARok = [rq_kw.PoleWszystko] + MozliweLataZuzyc
MozliweLataDlaBRok = MozliweLataZuzyc

def NumerDzisiaj():
    '''Zwraca numer dzisiejszego dnia
    '''
    return NumerDnia( * DataDzisiaj())

def NapisDaty(rok, miesiac, dzien):
    '''Zwraca napis w postaci "RRRR-MM-DD"
    dla podanego roku, miesiąca i dnia
    '''
    return '%04d-%02d-%02d' % (rok, miesiac, dzien)

def napis_z_rok_mies(rok, miesiac):
    return '%04d-%02d' % (rok, miesiac)

def NapisDzisiaj():
    '''
    Wyznacza dzień w postaci napisu: RRRR-MM-DD
    '''
    # Za pomocą "*" rozwijamy krotkę: "rok, miesiąc, dzień" na 3 parametry
    return NapisDaty( * DataDzisiaj())

def SekTeraz():
    '''
    Wyznacza dzień i moment w dniu w postaci: RRRR.MM.DD_GG.MM.SS
    - rok, miesiąc, dzień
    - godzina, minuta, sekunda
    '''
    return time.strftime('%Y.%m.%d_%H.%M.%S')

def DzienTeraz():
    '''
    Wyznacza dzień w postaci do wstawiania do bazy danych: RRRR-MM-DD
    - rok, miesiąc, dzień
    '''
    return time.strftime('%Y-%m-%d')

def szczegolowa_krotka(x):
    '''Zwraca datę na podstawie numeru dnia
    Parametr:
    x - (int) numer dnia
    Wartość zwracana:
    krotka 9-elementowa z szczegółami czasu
    '''
    return time.localtime(x * SEC_PER_DAY + SEC_PER_DAY / 2)

def DataDnia(x):
    '''Zwraca datę na podstawie numeru dnia
    Parametr:
    x - (int) numer dnia
    Wartość zwracana:
    napis - krotka 3 liczb całkowitych: (rok, miesiąc, dzień)
    '''
    return szczegolowa_krotka(x)[:3]

def RokDnia(x):
    return DataDnia(x)[0]

def MiesiacDnia(x):
    return DataDnia(x)[1]

def RzymskiDnia(x):
    miesiac = MiesiacDnia(x)
    return nazwa_rzymskiego(miesiac)

def RoboczyDnia(x):
    '''Informuje, czy podany dzień jest roboczy.
    Parametr:
    x - (int) numer dnia
    Wartość zwracana - liczba całkowita:
    1 - dzień roboczy
    0 - dzień wolny od pracy (sobota/niedziela)
    '''
    return szczegolowa_krotka(x).tm_wday < 5

def NapisDnia(numer):
    '''Zwraca napis z datą na podstawie podanego numeru dnia
    Parametr:
    numer - liczba całkowita (numer dnia)
    Wartość zwracana:
    napis - data w postaci RRRR-MM-DD
    '''
    return NapisDaty( * DataDnia(numer))

def ZakresRoku(rok):
    '''Pierwszy dzień aktualnego i następnego roku dla podanego roku'''
    pocz = dzien_nowego_roku(rok)
    kon = dzien_nowego_roku(rok + 1)
    return pocz, kon

def ZakresMiesiaca(rok, miesiac):
    '''Zwraca początek i koniec danego miesiąca w postaci
    skrajnych numerów dnia - pierwszego danego i następnego miesiąca,
    co pozwala użyć tych wartości jako parametry range()
    Parametry:
    rok, miesiac - opis miesiąca, dla którego wyznaczamy zakres dni
    Wartość zwracana:
    krotka: (pocz, kon) - numer dnia zaczynającego aktualny oraz następny miesiąc
    '''
    pocz = dzien_nowego_miesiaca(rok, miesiac)
    # Przejdź na początek następnego miesiąca
    if miesiac < 12:
        miesiac += 1
    else:
        miesiac = 1
        rok += 1
    kon = dzien_nowego_miesiaca(rok, miesiac)
    return pocz, kon

def rok_przestepny(rok):
    '''
    Wartość zwracana:
    1 - rok jest przestępny, 0 - rok nie jest przestępny
    '''
    if rok % 4 != 0:
        przestepny = 0
    elif rok % 100 != 0:
        przestepny = 1
    elif rok % 400 != 0:
        przestepny = 0
    else:
        przestepny = 1
    return przestepny

LegalneMiesiace = ('01', '02', '03', '04', '05', '06',
'07', '08', '09', '10', '11', '12',)

DniWMiesiacu = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,)

LegalneDni = (
'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
'13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
'25', '26', '27', '28', '29', '30', '31',)

def DataBledna(napis):
    '''
    Wartość zwracana:
    pusty napis - data nie była błędna (czyli była poprawna)
    napis o niezerowej długości - wystąpił jakiś błąd
    '''
    bledna = '' # Załóż, że data nie jest poprawna
    kawalki = napis.split('-')
    ile_kawalkow = len(kawalki)
    if ile_kawalkow == 3:
        rok, miesiac, dzien = kawalki
        if rok in MozliweLataFaktur:
            if miesiac in LegalneMiesiace:
                rok = int(rok)
                miesiac = int(miesiac)
                liczba_legalnych_dni = DniWMiesiacu[miesiac - 1]
                # W lutym dodamy jeden dzień, jeśli rok jest przestępny
                if miesiac == 2:
                    liczba_legalnych_dni += rok_przestepny(rok)
                if dzien in LegalneDni[:liczba_legalnych_dni]:
                    pass # Mamy datę bez zastrzeżeń
                else:
                    bledna = 'Dzień poza obsługiwanym zakresem: "%s"' % dzien
            else:
                bledna = 'Miesiąc poza obsługiwanym zakresem: "%s"' % miesiac
        else:
            bledna = 'Rok poza obsługiwanym zakresem: "%s"' % rok
    else:
        bledna = 'Liczba kawałków oddzielanych myślnikiem: %d' % ile_kawalkow
    return bledna

def daty_lat(dzien_pocz, dzien_kon):
    '''
    Parametry:
    dzien_pocz (integer) - pierwszy dzień pierwszego roku zakresu
    dzien_kon (integer) - pierszy dzień ostatniego roku, który już nie wejdzie na wykres
    Wartość zwracana:
    - lista dat pierwszych styczni od roku początkowego aż do roku
    końcowego włącznie
    '''
    wynik = []
    rok_pocz = RokDnia(dzien_pocz)
    rok_kon = RokDnia(dzien_kon)
    for teraz in range(rok_pocz, rok_kon + 1):
        dzien = NumerDnia(teraz, 1, 1)
        wynik.append(dzien)
    return wynik

def daty_roku(rok, rok_z_rozszerzeniem):
    '''
    Parametry:
    rok - numer roku
    Wartość zwracana:
    lista numerów dni dla dat rozpoczynających poszczególne miesiące,
    na końcu jest data, która już nie wchodzi w zakres przetwarzanych danych
    '''
    wynik = []
    if rok_z_rozszerzeniem:
        # Rozpoczynamy okres ciągły na początku grudnia poprzedniego roku
        for mies in range(12 - rq_kw.DodatkoweMiesiacePrzed, 12):
            wynik.append(NumerDnia(rok - 1, mies + 1, 1))
    for mies in range(12):
        wynik.append(NumerDnia(rok, mies + 1, 1))
    wynik.append(NumerDnia(rok + 1, 1, 1))
    if rok_z_rozszerzeniem:
        # Kończymy okres ciągły na początku lutego następnego roku
        for mies in range(1, 1 + rq_kw.DodatkoweMiesiacePo):
            wynik.append(NumerDnia(rok + 1, mies + 1, 1))
    return wynik

def sprawdz_numery_dnia():
    '''Funkcja testowa do sprawdzenia, czy dzielenie przez
    liczbę dni poprawnie daje liczbę dni w roku
    '''
    rok_pocz = rok = 1970
    pocz = NumerDnia(rok, 1, 1)
    for nast in range(rok + 1, 2038 + 1):
        spodziewana_dlugosc = 365 + rok_przestepny(rok)
        kon = NumerDnia(nast, 1, 1)
        wg_kalendarza = kon - pocz
        if spodziewana_dlugosc == wg_kalendarza:
            pass # Wszystko w porządku - nic nie drukujemy
        else:
            # Jest jakaś niezgodność - wyświetl informację na ekranie
            print rok, nast, spodziewana_dlugosc, wg_kalendarza
            break
        rok = nast
        pocz = kon
    else:
        print 'Daty sprawdzone: %d <= rok < %d' % (rok_pocz, rok)

def zn_unik():
    '''Zwraca unikalny identyfikator (proces, sekunda), aby
    dało się rozróżnić pliki z jednej sesji danego klienta
    '''
    return 't%sp%s' % (time.time(), os.getpid())

def wyznacz_moment_wg_wzorca(wzorzec, czas):
    krotka = time.localtime(czas)
    return time.strftime(wzorzec, krotka)

def wyznacz_date_logu(czas = None):
    return wyznacz_moment_wg_wzorca('%Y-%m-%d %H:%M:%S', czas)

def wyznacz_dzien_logu(czas = None):
    return wyznacz_moment_wg_wzorca('%Y-%m-%d', czas)

def wyznacz_sekunde_logu(czas = None):
    return wyznacz_moment_wg_wzorca('%H:%M:%S', czas)

def wyznacz_minute_logu(czas = None):
    return wyznacz_moment_wg_wzorca('%H:%M', czas)

def data_z_napisu(napis):
    return time.strptime(napis, '%Y-%m-%d')[:3]

def checkdate(napis):
    poprawna = True
    try:
        data_z_napisu(napis)
    except ValueError:
        poprawna = False
    return poprawna

def RokMscDnia(x):
    return szczegolowa_krotka(x)[:2]

def rok_mies_z_napisu(x):
    return RokMscDnia(napis_na_numer_dnia(x))

def one_common_date_of_energy_as_month_and_year(data_pocz, data_kon):
    spcf_pocz = rok_mies_z_napisu(data_pocz)
    spcf_kon = rok_mies_z_napisu(data_kon)
    if spcf_pocz != spcf_kon:
        raise RuntimeError('Specyfikacje?: %s %s - %s, %s' % (data_pocz, data_kon, spcf_pocz, spcf_kon))
    return spcf_pocz

class TestDaysDates(unittest.TestCase):
    def test_stalych_datownika(self):
        '''
        TestDaysDates:
        '''
        self.assertEqual(rok_sekundy(data_testowa_a), '2011')
        self.assertEqual(rok_sekundy(data_testowa_b), '2010')
        self.assertEqual(rok_liczba(data_testowa_a), 2011)
        self.assertEqual(rok_liczba(data_testowa_b), 2010)
        self.assertEqual(miesiac_liczba(data_testowa_a), 8)
        self.assertEqual(miesiac_liczba(data_testowa_b), 10)
        self.assertEqual(dzien_liczba(data_testowa_a), 29)
        self.assertEqual(dzien_liczba(data_testowa_c), 13)
        self.assertEqual(wyznacz_dzisiejsza_date(data_testowa_a), 'poniedziałek, 29 sierpień, 2011')
        self.assertEqual(wyznacz_dzisiejsza_date(data_testowa_b), 'piątek, 29 październik, 2010')
        self.assertEqual(wyznacz_date_logu(data_testowa_c), du_kw.rjb_data_przkl)
        self.assertEqual(wyznacz_dzien_logu(data_testowa_c), du_kw.rjb_dzien_przkl)
        self.assertEqual(wyznacz_sekunde_logu(data_testowa_c), du_kw.rjb_godzina_przkl)
        self.assertEqual(wyznacz_minute_logu(data_testowa_c), du_kw.rjb_minuta_przkl)
        self.assertEqual(NumerDnia(1970, 1, 1), 0)
        self.assertEqual(dzien_nowego_miesiaca(1970, 1), 0)
        self.assertEqual(dzien_nowego_miesiaca(1970, 2), 31)
        self.assertEqual(dzien_nowego_miesiaca(1970, 3), 31 + 28)
        self.assertEqual(dzien_nowego_miesiaca(1970, 4), 31 + 28 + 31)
        self.assertEqual(dzien_nowego_roku(1970), 0)
        self.assertEqual(dzien_nowego_roku(1971), 365)
        self.assertEqual(napis_na_numer_dnia((1970, 1, 1)), 0)
        self.assertEqual(napis_na_numer_dnia('1970-01-01'), 0)
        self.assertEqual(napis_na_numer_dnia('2011-03-27'), 15060)
        self.assertEqual(napis_na_numer_dnia('2011-03-28'), 15060 + 1) # DST
        self.assertEqual(napis_na_numer_dnia('2011-03-29'), 15060 + 2)
        self.assertEqual(napis_na_numer_dnia('2011-10-30'), 15277)
        self.assertEqual(napis_na_numer_dnia('2011-10-31'), 15277 + 1) # DST
        self.assertEqual(napis_na_numer_dnia('2011-11-01'), 15277 + 2)
        self.assertEqual(napis_na_numer_dnia(du_kw.rjb_dzien_przkl), 15321)
        self.assertEqual(NapisDnia(0), '1970-01-01')
        self.assertEqual(ZakresRoku(1972), (730, 1096))
        self.assertEqual(DataDnia(0), (1970, 1, 1))
        self.assertEqual(DataDnia(15278), (2011, 10, 31))
        self.assertEqual(RokDnia(15278), 2011)
        self.assertEqual(MiesiacDnia(15278), 10)
        self.assertEqual(RzymskiDnia(15278), 'X')
        self.assertEqual(RoboczyDnia(0), 1) # Czwartek
        self.assertEqual(RoboczyDnia(1), 1)
        self.assertEqual(RoboczyDnia(2), 0) # Sobota
        self.assertEqual(RoboczyDnia(3), 0) # Niedziela
        self.assertEqual(RoboczyDnia(4), 1)
        self.assertEqual(RoboczyDnia(5), 1)
        self.assertEqual(RoboczyDnia(6), 1) # Środa
        self.assertEqual(data_rmd(data_testowa_a), (2011, 8, 29))
        daty_roczne = daty_lat(13149, 13879)
        self.assertEqual(daty_roczne, [13149, 13514, 13879])
        self.assertEqual(map(DataDnia, daty_roczne), [(2006, 1, 1), (2007, 1, 1), (2008, 1, 1)])
        self.assertEqual(ZakresMiesiaca(2008, 2), (13910, 13939))
        self.assertEqual(RokMscDnia(14975), (2011, 1))
        self.assertEqual(RokMscDnia(15006), (2011, 2))

    def test_verify_date(self):
        '''
        TestDaysDates:
        '''
        self.assertTrue(checkdate(wyznacz_dzien_logu(data_testowa_c)))
        self.assertFalse(checkdate('2012-02-31'))
        self.assertTrue(checkdate('2012-2-1'))
        self.assertEqual(data_z_napisu(du_kw.rjb_dzien_przkl), (2011, 12, 13))
        self.assertEqual(nazwa_rzymskiego(4), 'IV')
        self.assertEqual(len(daty_roku(2008, rok_z_rozszerzeniem=0)), rq_kw.RokZwykly + 1)
        self.assertEqual(len(daty_roku(2008, rok_z_rozszerzeniem=1)), rq_kw.RokDluzszy + 1)
        self.assertEqual(rok_mies_z_napisu('2010-01-01'), (2010, 1))
        self.assertEqual(napis_z_rok_mies(2011, 9), '2011-09')
