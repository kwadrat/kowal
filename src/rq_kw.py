#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

# Baza produkcyjna/rozwojowa
MamBazeProd = 0

zst_wysyla_energie_na_prod = 0

WersjaUbuntuTest = 0
WersjaUbuntuRun = WersjaUbuntuTest and 0

RokBazowyRaportuEnergii = 2010
RokPocz2 = 2004

DodatkoweMiesiacePrzed = 1
DodatkoweMiesiacePo = 2

# Liczba miesięcy dla faktur punktowych - tylko rok
RokZwykly = 12
# Dla faktur ciągłych pozwalamy na dodatkowe miesiące na ekranie
RokDluzszy = DodatkoweMiesiacePrzed + RokZwykly + DodatkoweMiesiacePo

ZEZWOLENIE_NSK = 1 # Ogranicz tylko dla poszczególnych lat

ECHO_NIE = 0 # Pracuj po cichu
ECHO_TAK = 1 # Generuj HTML

PoprawneLiczbyPaskowDlaOkresuMiesiecznego = (
  RokZwykly, # faktury miesięczne punktowe
  RokDluzszy, # faktury miesięczne ciągłe
  )

DaneOkresu = (
Dt_Miesiac,
Dt_Rok,
Dt_RapPierwszy,
Dt_RapDrugi,
) = (
'W danym roku',
'W latach',
'Raport 1',
'Raport 2',
)

DanePrezentacji = (
DP_Wykres,
DP_Tabela,
) = (
'Wykres',
'Tabela',
)

# Domyślnie chcemy wszystkie lata w zestawieniu
PoleWszystko = 'Wszystko'
PoleNN = 'None'
NiePtrzBRok = (PoleWszystko, None, )
BezKonkretnychRocznikow = (PoleWszystko, PoleNN, None)
DaneDomeny = (
    Dn_Kwota,
    Dn_Towar,
    Dn_Moc,
    ) = (
    'Koszty',
    'Ilość',
    'Moc',
    )

DP_PotrzebujeDomene = (DP_Wykres, PoleNN)
DP_NiePotrzebujeDomeny = (DP_Tabela, )

DaneAktWsz = (
DA_Aktywne,
DA_Wszystkie,
) = (
'Aktywne',
'Wszystkie',
)

DaneRazem = (
DR_Polaczone,
DR_Oddzielnie,
) = (
'Razem',
'Oddzielnie',
)

DodatkoweObiekty = (
ObiektGwiazdka,
) = (
'Wszystkie obiekty',
)

WyborOgolnegoObiektu = [(ObiektGwiazdka, ObiektGwiazdka)]

JP_ChcePolaczone = (DR_Polaczone, PoleNN)

# Sytuacja załadowania świeżego formularza, kiedy domyślnie
# pewne pola są pokazywane, a inne ukrywane
PR_Brak = None

PR_PotrzebujeRoku = (Dt_Miesiac, PR_Brak, )
PR_NiePotrzebujeRoku = (Dt_Rok, Dt_RapPierwszy, Dt_RapDrugi, )

# Dla grupy (pojedyncze obiekty, przedszkola)
PR_PotrzebujeGrupy = (Dt_Miesiac, Dt_Rok, Dt_RapPierwszy, Dt_RapDrugi, PR_Brak, )
PR_NiePotrzebujeGrupy = ()

# Dla prezentacji (tabela, wykres)
PR_PotrzebujePrezent = (Dt_RapPierwszy, Dt_RapDrugi, )
PR_NiePotrzebujePrezent = (Dt_Miesiac, Dt_Rok, PR_Brak, )

# Dla medium (np. ciepło, gaz)
PR_PotrzebujeMedium = (Dt_Miesiac, Dt_Rok, PR_Brak, )
PR_NiePotrzebujeMedium = (Dt_RapPierwszy, Dt_RapDrugi, )

# Dla domeny (złotówki, ilość towaru)
PR_PotrzebujeDomena = (Dt_Miesiac, Dt_Rok, PR_Brak, )
PR_NiePotrzebujeDomena = (Dt_RapDrugi, )
PR_MozeDomena = (Dt_RapPierwszy, )

# Dla razem/osobno
PR_PotrzebujeRazem = (Dt_RapPierwszy,)
PR_NiePotrzebujeRazem = (PR_Brak, Dt_Miesiac, Dt_Rok, Dt_RapDrugi)

# Dla roku A
PR_PotrzebujeARok = (Dt_RapPierwszy, )
PR_NiePotrzebujeARok = (Dt_Miesiac, Dt_Rok, Dt_RapDrugi, PR_Brak, )
PR_OkresDlaKwot = (Dt_Miesiac, Dt_Rok, Dt_RapDrugi, PR_Brak, )
PR_OkresBycMozeDlaKwot = (Dt_RapPierwszy, )


# Wybrano pojedyncze obiekty, a nie konkretną grupę
DG_BrakGrupowania = 'Pojedynczy obiekt'
PR_ChcemyObiektu = (PR_Brak, DG_BrakGrupowania)
DG_Obiekty = (DG_BrakGrupowania, DG_BrakGrupowania)

niekonkretny_obiekt = (None, )

Dla_Dwoch_Raportow = (Dt_RapPierwszy, Dt_RapDrugi, )

# Ograniczanie wyświetlania odcinków bazowych, nakładek albo zbitek
TymczasowoOgrWysw = 1

# Pokaż odcinki bazowe
TymczasowoPkzBaz = 1

# Pokaż zbitki
TymczasowoPkzZbt = 1

jquery_enabled = 0

if WersjaUbuntuTest:
    ##############################################################################
    Docelowo_psyco_nie_pygresql = 1
    ##############################################################################
else:
    ##############################################################################
    Docelowo_psyco_nie_pygresql = 0
    ##############################################################################

# (default: 0) Sumowanie słupka indywidualnego:
# 1 - słupki indywidualne od razu są sumowane, potem drugie sumowanie
# jest w słupku zbiorczym
# 0 - jest tylko sumowanie w słupku zbiorczym
# Sumowanie słupka:
# - zbiorczego - zawsze
# - indywidualnego - być może

# Sumowanie słupka na wykresie indywidualnego licznika
TymczasowoSumowanieInd = 0

Tymczasowo_pokaz_klucz_faktury_zamiast_licz_porz = 0
Tymczasowo_pokaz_etykiety_pol_faktury = 0

Niebezpieczne_testowa_aplikacja_produkcyjna_baza = 0

DocelowoOdwrotnieOproczOstatniego = 1
TymczasowoPozwolNaUzupelnienieBorki = 0
TymczasowoWygenerujSztywne = 0
DocelowoObiektoweSezonyGrzewcze = 1

TymczasowoTylkoJeden = 0
DocelowoPosrednikDokladnejLiczby = 0
TymczasowoPokazWzory = 0
TymczasowoTylkoWybranyArkusz = 1
