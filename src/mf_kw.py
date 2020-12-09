#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import ga_kw
import lk_kw
import dv_kw
import oc_kw
import ze_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

link_obrazu = '''\
<img name="%(html_tmp_name)s" src="%(nazwa)s" width="%(x)d" height="%(y)d"%(rozkaz_mapy)s> <br/>
'''

def pocz_mapy(nazwa):
    return '''\
  <map id="%(mapa_slupkow)s" name="%(mapa_slupkow)s">
  ''' % dict(mapa_slupkow = nazwa)

kon_mapy = '''\
</map>
'''

kawalki_quote = (
    ('&', ga_kw.MHG_LAMP),
    ('<', '&lt;'),
    ('>', '&gt;'),
    ('"', '&quot;'),
    ("'", '&prime;'),
    )

def quote_html(napis):
    for a, b in kawalki_quote:
        napis = napis.replace(a, b)
    return napis

def UsunDuplikaty(lista):
    '''
    Zwraca oryginalną listę, ale posortowaną i z usuniętymi
    duplikatami
    '''
    wynik = []
    lista_do_sortowania = lista[:]
    lista_do_sortowania.sort()
    ile_elementow = len(lista_do_sortowania)
    if ile_elementow > 0:
        Poprz = lista_do_sortowania[0]
        wynik.append(Poprz)
        for elem in lista_do_sortowania[1:]:
            if elem != Poprz:
                wynik.append(elem)
            Poprz = elem
    return wynik

def numer_wiersza(etyk):
    '''
    Odcinamy dodatkową literkę, aby uzyskać czysty numer faktury.
    Literka została dodana tylko po to, aby identyfikator nie był
    samym numerem.
    '''
    return int(etyk[1:])

def zrob_tab_html(on_mouse, ls_wr_tab):
    wynik = []
    wynik.append(ze_kw.op_32_sbf())
    for jn_wr_tab in ls_wr_tab:
        nazwa = jn_wr_tab.get_line_name()
        if nazwa: # Nazwa określa numer faktury
            on_tmp_mouse = ''
            tmp_liczba = numer_wiersza(nazwa)
            if tmp_liczba in on_mouse:
                on_tmp_mouse = on_mouse[tmp_liczba]
            wynik.append(ze_kw.op_tr(id_=nazwa, nzw_wrsz=nazwa, rest=on_tmp_mouse))
        else: # Tylko dla pierwszego wiersza z nagłówkami opisującymi zawartość kolumn
            wynik.append(ze_kw.formularz_67c_pocz_wiersza)
        jn_wr_tab.to_comma()
        jn_wr_tab.use_color()
        wiersz = jn_wr_tab.get_line_row()
        for kolumna in wiersz:
            wynik.append(ze_kw.op_ptd(kolumna))
        wynik.append(ze_kw.formularz_67c_kon_wiersza)
    wynik.append(ze_kw.formularz_1c_kon_tabeli)
    return ''.join(wynik)

def nazwa_wiersza(lp_faktury):
    '''
    Zwraca nazwę wiersza tabeli
    '''
    return 'w%d' % lp_faktury

def plik_grafiki(znacznik_unik, litera_typu, nr_miejsca, wersja):
    '''
    Zwraca nazwę pliku graficznego PNG
    litera_typu - 's' (słupek), 'p' (pasek), 'w' (wykres raportu 1, 2)
    nr_miejsca - liczba całkowita, numer miejsca
    wersja - krotka z zestawem liczb (pusta - wersja podstawowa pliku)
    '''
    return '%s%s_%s%d_%s%s' % (
      oc_kw.PoczObrazka,
      znacznik_unik,
      litera_typu,
      nr_miejsca,
      '_'.join(map(str, wersja)),
      oc_kw.RozszerzenieObrazka)

def nazwa_mapy(litera_typu, nr_miejsca):
    '''
    Zwraca nazwę pliku graficznego PNG
    litera_typu - 's' (słupek), 'p' (pasek)
    nr_miejsca - liczba całkowita, numer miejsca
    wersja - krotka z zestawem liczb (pusta - wersja podstawowa pliku)
    '''
    return 'mapa_%s%d' % (litera_typu, nr_miejsca)

class TestListyNagTabeli(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual
    def test_naglowka_tabeli(self):
        '''
        TestListyNagTabeli:
        '''
        self.assertEqual(plik_grafiki('t123p45', lk_kw.LITERA_SLUPEK, 0, ()), 'plik_t123p45_s0_.png')
        self.assertEqual(plik_grafiki('t123p45', lk_kw.LITERA_SLUPEK, 1, (2,)), 'plik_t123p45_s1_2.png')
        self.assertEqual(quote_html(''''"<>&'''), '&prime;&quot;&lt;&gt;&amp;')
        self.assertEqual(nazwa_wiersza(7), 'w7')
        self.assertEqual(numer_wiersza('w7'), 7)
        self.assertEqual(nazwa_mapy('s', 1), 'mapa_s1')
