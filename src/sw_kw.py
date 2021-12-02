#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Słowne przedstawienie kwoty
'''

import unittest

import en_kw

# liczba pojedyncza, liczba mnoga, dopełniacz

odmiana_zloty = {
  'liczba pojedyncza': 'złoty',
  'liczba mnoga': 'złote',
  'dopełniacz': 'złotych',
}

odmiana_tysiac = {
  'liczba pojedyncza': 'tysiąc',
  'liczba mnoga': 'tysiące',
  'dopełniacz': 'tysięcy',
}

slownik_setek = {
  1: 'sto',
  2: 'dwieście',
  3: 'trzysta',
  4: 'czterysta',
  5: 'pięćset',
  6: 'sześćset',
  7: 'siedemset',
  8: 'osiemset',
  9: 'dziewięćset',
}

slownik_dziesiatek = {
  2: 'dwadzieścia',
  3: 'trzydzieści',
  4: 'czterdzieści',
  5: 'pięćdziesiąt',
  6: 'sześćdziesiąt',
  7: 'siedemdziesiąt',
  8: 'osiemdziesiąt',
  9: 'dziewięćdziesiąt',
}

slownik_dwudziestki = {
  1: 'jeden',
  2: 'dwa',
  3: 'trzy',
  4: 'cztery',
  5: 'pięć',
  6: 'sześć',
  7: 'siedem',
  8: 'osiem',
  9: 'dziewięć',
  10: 'dziesięć',
  11: 'jedenaście',
  12: 'dwanaście',
  13: 'trzynaście',
  14: 'czternaście',
  15: 'piętnaście',
  16: 'szesnaście',
  17: 'siedemnaście',
  18: 'osiemnaście',
  19: 'dziewiętnaście',
}

dane_testowe = '''\
1,jeden złoty
2,dwa złote
3,trzy złote
4,cztery złote
5,pięć złotych
6,sześć złotych
7,siedem złotych
8,osiem złotych
9,dziewięć złotych
10,dziesięć złotych
11,jedenaście złotych
12,dwanaście złotych
13,trzynaście złotych
14,czternaście złotych
15,piętnaście złotych
16,szesnaście złotych
17,siedemnaście złotych
18,osiemnaście złotych
19,dziewiętnaście złotych
20,dwadzieścia złotych
21,dwadzieścia jeden złotych
22,dwadzieścia dwa złote
23,dwadzieścia trzy złote
24,dwadzieścia cztery złote
25,dwadzieścia pięć złotych
26,dwadzieścia sześć złotych
27,dwadzieścia siedem złotych
28,dwadzieścia osiem złotych
29,dwadzieścia dziewięć złotych
30,trzydzieści złotych
31,trzydzieści jeden złotych
32,trzydzieści dwa złote
33,trzydzieści trzy złote
34,trzydzieści cztery złote
35,trzydzieści pięć złotych
36,trzydzieści sześć złotych
37,trzydzieści siedem złotych
38,trzydzieści osiem złotych
39,trzydzieści dziewięć złotych
40,czterdzieści złotych
41,czterdzieści jeden złotych
42,czterdzieści dwa złote
43,czterdzieści trzy złote
44,czterdzieści cztery złote
45,czterdzieści pięć złotych
46,czterdzieści sześć złotych
47,czterdzieści siedem złotych
48,czterdzieści osiem złotych
49,czterdzieści dziewięć złotych
50,pięćdziesiąt złotych
51,pięćdziesiąt jeden złotych
52,pięćdziesiąt dwa złote
53,pięćdziesiąt trzy złote
54,pięćdziesiąt cztery złote
55,pięćdziesiąt pięć złotych
56,pięćdziesiąt sześć złotych
57,pięćdziesiąt siedem złotych
58,pięćdziesiąt osiem złotych
59,pięćdziesiąt dziewięć złotych
60,sześćdziesiąt złotych
61,sześćdziesiąt jeden złotych
62,sześćdziesiąt dwa złote
63,sześćdziesiąt trzy złote
64,sześćdziesiąt cztery złote
65,sześćdziesiąt pięć złotych
66,sześćdziesiąt sześć złotych
67,sześćdziesiąt siedem złotych
68,sześćdziesiąt osiem złotych
69,sześćdziesiąt dziewięć złotych
70,siedemdziesiąt złotych
71,siedemdziesiąt jeden złotych
72,siedemdziesiąt dwa złote
73,siedemdziesiąt trzy złote
74,siedemdziesiąt cztery złote
75,siedemdziesiąt pięć złotych
76,siedemdziesiąt sześć złotych
77,siedemdziesiąt siedem złotych
78,siedemdziesiąt osiem złotych
79,siedemdziesiąt dziewięć złotych
80,osiemdziesiąt złotych
81,osiemdziesiąt jeden złotych
82,osiemdziesiąt dwa złote
83,osiemdziesiąt trzy złote
84,osiemdziesiąt cztery złote
85,osiemdziesiąt pięć złotych
86,osiemdziesiąt sześć złotych
87,osiemdziesiąt siedem złotych
88,osiemdziesiąt osiem złotych
89,osiemdziesiąt dziewięć złotych
90,dziewięćdziesiąt złotych
91,dziewięćdziesiąt jeden złotych
92,dziewięćdziesiąt dwa złote
93,dziewięćdziesiąt trzy złote
94,dziewięćdziesiąt cztery złote
95,dziewięćdziesiąt pięć złotych
96,dziewięćdziesiąt sześć złotych
97,dziewięćdziesiąt siedem złotych
98,dziewięćdziesiąt osiem złotych
99,dziewięćdziesiąt dziewięć złotych
100,sto złotych
200,dwieście złotych
300,trzysta złotych
400,czterysta złotych
500,pięćset złotych
600,sześćset złotych
700,siedemset złotych
800,osiemset złotych
900,dziewięćset złotych
0,zero złotych
101,sto jeden złotych
1001,tysiąc jeden złotych
10001,dziesięć tysięcy jeden złotych
100001,sto tysięcy jeden złotych
999999,dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć złotych
993992,dziewięćset dziewięćdziesiąt trzy tysiące dziewięćset dziewięćdziesiąt dwa złote
'''


class WyznaczanieSlownie(object):
    def deklinacja(self, wartosc, odmiana):
        '''
        WyznaczanieSlownie:
        '''
        if wartosc == 1:
            return odmiana['liczba pojedyncza']
        elif 2 <= wartosc % 10 <= 4:
            if 12 <= wartosc % 100 <= 14:
                return odmiana['dopełniacz']
            else:
                return odmiana['liczba mnoga']
        else:
            return odmiana['dopełniacz']

    def jako_nps(self, wartosc, jestem_opcjonalny_jeden, odmiana, ile_tysiecy=0):
        '''
        WyznaczanieSlownie:
        '''
        reszta, tn_jednosci = divmod(wartosc, 10)
        tn_setki, tn_dziesiatki = divmod(reszta, 10)
        wynik = []
        if tn_setki:
            kawalek = slownik_setek[tn_setki]
            wynik.append(kawalek)
        if tn_dziesiatki >= 2:
            kawalek = slownik_dziesiatek[tn_dziesiatki]
            wynik.append(kawalek)
            if tn_jednosci:
                kawalek = slownik_dwudziestki[tn_jednosci]
                wynik.append(kawalek)
        else:
            tn_jednosci += 10 * tn_dziesiatki
            if tn_jednosci and (wartosc != 1 or not jestem_opcjonalny_jeden):
                kawalek = slownik_dwudziestki[tn_jednosci]
                wynik.append(kawalek)
        if odmiana:
            kawalek = self.deklinacja(ile_tysiecy * 1000 + wartosc, odmiana)
            wynik.append(kawalek)
        return wynik

    def wypowiedz_utf(self, wartosc):
        '''
        WyznaczanieSlownie:
        '''
        assert type(wartosc) is int
        ile_tysiecy, ile_jednostek = divmod(wartosc, 1000)
        wynik = []
        jestem_opcjonalny_jeden = 1
        if ile_tysiecy:
            kawalek = self.jako_nps(ile_tysiecy, jestem_opcjonalny_jeden, odmiana_tysiac)
            wynik.extend(kawalek)

        jestem_opcjonalny_jeden = 0
        if ile_jednostek:
            kawalek = self.jako_nps(ile_jednostek, jestem_opcjonalny_jeden, odmiana_zloty, ile_tysiecy=ile_tysiecy)
            wynik.extend(kawalek)
        else:
            if not ile_tysiecy:
                kawalek = 'zero'
                wynik.append(kawalek)
            kawalek = 'złotych'
            wynik.append(kawalek)
        return ' '.join(wynik)

    def wypowiedz(self, wartosc):
        '''
        WyznaczanieSlownie:
        '''
        result = self.wypowiedz_utf(wartosc)
        return en_kw.utf_to_unicode(result)


def sprawdzanie_tlumaczenia(wsl):
    for i in dane_testowe.splitlines():
        if len(i) > 0 and i[0] != '#':
            liczba, reczny = i.split(',')
            liczba = int(liczba)
            automatyczny = wsl.wypowiedz_utf(liczba)
            if reczny != automatyczny:
                print liczba
                print "'%s'" % reczny
                print "'%s'" % automatyczny
                raise RuntimeError("Wczesny koniec")


class TestSlownie(unittest.TestCase):
    def test_slownie(self):
        '''
        TestSlownie:
        '''
        wsl = WyznaczanieSlownie()
        sprawdzanie_tlumaczenia(wsl)
