#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import uz_kw
import ze_kw
import uy_kw
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

def mam_pojedyn_wartosci(lista):
    return type(lista[0]) is str

def ListWyboruOgolna(tgk, nazwa, lista):
    w = []
    if len(lista) > 0:
        w.append(ze_kw.op_30_sbf(nazwa))
        Wybrana = tgk.qparam.get(nazwa, None)
        if mam_pojedyn_wartosci(lista):
            Podwojne = 0
        else:
            Podwojne = 1 # Lista zawiera etykietę oraz tekstowy opis
        for opcja in lista:
            if Podwojne:
                opcja, etykieta = opcja
            else:
                etykieta = opcja

            w.append(ze_kw.op_option(
              etykieta,
              opcja,
              opcja == Wybrana))
        w.append(ze_kw.formularz_1c_kon_slct)
    return ''.join(w)

class TestPodstSkrawka(unittest.TestCase):
    tassertEqual = uy_kw.tassertEqual
    def test_podstawowego_skrawka(self):
        '''
        TestPodstSkrawka:
        '''
        self.assertEqual(mam_pojedyn_wartosci([('a', 'opis A'), ('b', 'opis B')]), 0)
        self.assertEqual(mam_pojedyn_wartosci(('a', 'b')), 1)

    def test_listy_wyboru(self):
        '''
        TestPodstSkrawka:
        '''
        self.assertEqual(ListWyboruOgolna(None, None, []), '')
        tgk = od_kw.PseudoTGK()
        self.tassertEqual(ListWyboruOgolna(tgk, None, ['a']), uz_kw.ldp_1_inst)
        self.tassertEqual(ListWyboruOgolna(tgk, None, [(12, 'a')]), uz_kw.ldp_2_inst)
        self.tassertEqual(ListWyboruOgolna(tgk, 'bc', [(45, 'de')]), uz_kw.ldp_3_inst)
        nazwa = 'efg'
        opcja = 678
        tgk.qparam[nazwa] = opcja
        self.tassertEqual(ListWyboruOgolna(tgk, nazwa, [(opcja, 'hi')]), uz_kw.ldp_4_inst)
