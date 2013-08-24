#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lk_kw
import rq_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

# Nie ujednolicaj adresu IP z nazwą, bo na razie chcemy synchronizować różne treści
rjb_klnt_ip = '87.101.66.154'

rjb_pocz_hm_dir = '/home/'
rjb_do_pbl_ht = lk_kw.rjb_sam_slsh + 'public_html'
rjb_sama_tylda = '~'
PoczObrazka = 'plik_'
RozszerzenieObrazka = '.png'
url_ameryka_http = 'http://'
rjb_hs_pocz = 'https://'
if rq_kw.WersjaUbuntuRun:
    ##############################################################################
    adres_maszyny = '192.168.56.101'
    ##############################################################################
else:
    ##############################################################################
    adres_maszyny = 'media.ciri.pl'
    ##############################################################################
url_kotw_a_ica = url_ameryka_http + adres_maszyny
rjb_hs_pcztk_sam = rjb_hs_pocz + adres_maszyny
url_kotw_b_ica = url_kotw_a_ica + lk_kw.rjb_sam_slsh
rjb_tld_kw_d_apl = 'inne'
rjb_tld_kw_e_apl = '2'
rjb_tld_kw_f_apl = rjb_tld_kw_d_apl + rjb_tld_kw_e_apl
konto_uzytkownika = 'kwadrat'
rjb_tld_kw_a_apl = rjb_sama_tylda + konto_uzytkownika
rjb_tld_kw_b_apl = lk_kw.rjb_sam_slsh + rjb_sama_tylda + konto_uzytkownika
rjb_sciezka_kw = url_kotw_b_ica + rjb_tld_kw_a_apl
rjb_kt_dom_uzt = rjb_pocz_hm_dir + konto_uzytkownika
rjb_ph_uztk = rjb_kt_dom_uzt + rjb_do_pbl_ht + lk_kw.rjb_sam_slsh
rjb_sciezka_a_kw = rjb_sciezka_kw + lk_kw.rjb_sam_slsh
GenPicDir = 'gen_kowal/'
poczatek_gen = rjb_sciezka_a_kw + GenPicDir
SciezkaPlikow = rjb_ph_uztk + GenPicDir
EYK_lporz_fktr = 'lp_faktury'
rjb_kwl_sam = 'kowal'
rjb_sczk_do_kwl = rjb_kt_dom_uzt + lk_kw.rjb_sam_slsh + rjb_kwl_sam
LogDir = rjb_sczk_do_kwl + '/log'
rjb_tld_kw_g_apl = '.py'
fq_kx_qv = 'kx'
fq_ky_qv = 'ky'
fq_px_qv = 'px'
fq_py_qv = 'py'
fq_nowy_this_qv = 'nowy_this'

def pelna_generowana_nazwa(nazwa):
    return poczatek_gen + nazwa

def dodaj_py(nazwa):
    return nazwa + rjb_tld_kw_g_apl

def fn_a_in_dwa(wersja_produkcyjna):
    if wersja_produkcyjna:
        wynik = rjb_tld_kw_d_apl
    else:
        wynik = rjb_tld_kw_f_apl
    return wynik

class KalejdoskopStron(object):
    def __init__(self, numer_strony):
        '''
        KalejdoskopStron:
        '''
        self.rj_sam_rdzen = 'l%d' % numer_strony
        self.rj_py_wersja = dodaj_py(self.rj_sam_rdzen)

rjb_strona_pierwsza = KalejdoskopStron(1)
rjb_strona_druga = KalejdoskopStron(2)
rjb_strona_trzecia = KalejdoskopStron(3)
rjb_strona_czwarta = KalejdoskopStron(4)
rjb_strona_piata = KalejdoskopStron(5)
rjb_strona_szosta = KalejdoskopStron(6)
rjb_strona_siodma = KalejdoskopStron(7)
rjb_strona_osma = KalejdoskopStron(8)
rjb_strona_dziewiata = KalejdoskopStron(9)
rjb_strona_dziesiata = KalejdoskopStron(10)

def fn_adres_post(wersja_produkcyjna):
    return lk_kw.rjb_sam_slsh + fn_a_in_dwa(wersja_produkcyjna) + lk_kw.rjb_sam_slsh + dodaj_py(rjb_strona_druga.rj_sam_rdzen)

class TestConstantStrings(unittest.TestCase):
    def test_constant_strings(self):
        '''
        TestConstantStrings:
        '''
        self.assertEqual(rjb_pocz_hm_dir, '/home/')
        self.assertEqual(rjb_do_pbl_ht, '/public_html')
        self.assertEqual(rjb_sama_tylda, '~')
        self.assertEqual(PoczObrazka, 'plik_')
        self.assertEqual(RozszerzenieObrazka, '.png')
        self.assertEqual(url_ameryka_http, 'http://')
        self.assertEqual(rjb_hs_pocz, 'https://')
        self.assertEqual(adres_maszyny, 'media.ciri.pl')
        self.assertEqual(url_kotw_a_ica, 'http://media.ciri.pl')
        self.assertEqual(rjb_hs_pcztk_sam, 'https://media.ciri.pl')
        self.assertEqual(url_kotw_b_ica, 'http://media.ciri.pl/')
        self.assertEqual(konto_uzytkownika, 'kwadrat')
        self.assertEqual(rjb_tld_kw_a_apl, '~kwadrat')
        self.assertEqual(rjb_tld_kw_b_apl, '/~kwadrat')
        self.assertEqual(rjb_kt_dom_uzt, '/home/kwadrat')
        self.assertEqual(rjb_ph_uztk, '/home/kwadrat/public_html/')
        self.assertEqual(rjb_sciezka_kw, 'http://media.ciri.pl/~kwadrat')
        self.assertEqual(rjb_sciezka_a_kw, 'http://media.ciri.pl/~kwadrat/')
        self.assertEqual(GenPicDir, 'gen_kowal/')
        self.assertEqual(poczatek_gen, 'http://media.ciri.pl/~kwadrat/gen_kowal/')
        self.assertEqual(SciezkaPlikow, '/home/kwadrat/public_html/gen_kowal/')
        self.assertEqual(pelna_generowana_nazwa('tmp.png'), 'http://media.ciri.pl/~kwadrat/gen_kowal/tmp.png')
        self.assertEqual(pelna_generowana_nazwa('inny.jpg'), 'http://media.ciri.pl/~kwadrat/gen_kowal/inny.jpg')
        self.assertEqual(rjb_klnt_ip, '87.101.66.154')
        self.assertEqual(rjb_kwl_sam, 'kowal')
        self.assertEqual(rjb_sczk_do_kwl, '/home/kwadrat/kowal')
        self.assertEqual(LogDir, '/home/kwadrat/kowal/log')
        self.assertEqual(rjb_tld_kw_g_apl, '.py')
        self.assertEqual(dodaj_py('a'), 'a.py')
        self.assertEqual(rjb_strona_pierwsza.rj_sam_rdzen, 'l1')
        self.assertEqual(rjb_strona_pierwsza.rj_py_wersja, 'l1.py')
        self.assertEqual(rjb_strona_druga.rj_sam_rdzen, 'l2')
        self.assertEqual(rjb_strona_piata.rj_sam_rdzen, 'l5')
        self.assertEqual(rjb_strona_piata.rj_py_wersja, 'l5.py')
        self.assertEqual(rjb_strona_szosta.rj_sam_rdzen, 'l6')
        self.assertEqual(rjb_strona_szosta.rj_py_wersja, 'l6.py')
        self.assertEqual(rjb_strona_siodma.rj_sam_rdzen, 'l7')
        self.assertEqual(rjb_strona_siodma.rj_py_wersja, 'l7.py')
        self.assertEqual(rjb_strona_osma.rj_sam_rdzen, 'l8')
        self.assertEqual(rjb_strona_osma.rj_py_wersja, 'l8.py')
        self.assertEqual(rjb_strona_dziewiata.rj_sam_rdzen, 'l9')
        self.assertEqual(rjb_strona_dziewiata.rj_py_wersja, 'l9.py')
        self.assertEqual(rjb_strona_dziesiata.rj_sam_rdzen, 'l10')
        self.assertEqual(rjb_strona_dziesiata.rj_py_wersja, 'l10.py')
        self.assertEqual(fn_a_in_dwa(0), 'inne2')
        self.assertEqual(fn_a_in_dwa(1), 'inne')
        self.assertEqual(fn_adres_post(1), '/inne/l2.py')
        self.assertEqual(fn_adres_post(0), '/inne2/l2.py')
        self.assertEqual(rjb_tld_kw_d_apl, 'inne')
        self.assertEqual(rjb_tld_kw_e_apl, '2')
        self.assertEqual(rjb_tld_kw_f_apl, 'inne2')

    def test_kalejdoskopu_stron(self):
        '''
        TestConstantStrings:
        '''
        obk = KalejdoskopStron(1)
        self.assertEqual(obk.rj_sam_rdzen, 'l1')
        self.assertEqual(obk.rj_py_wersja, 'l1.py')

    def test_2_kalejdoskopu_stron(self):
        '''
        TestConstantStrings:
        '''
        obk = KalejdoskopStron(2)
        self.assertEqual(obk.rj_sam_rdzen, 'l2')
        self.assertEqual(obk.rj_py_wersja, 'l2.py')
