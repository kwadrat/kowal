#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
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

rjb_sam_slsh = '/'
rjb_pocz_hm_dir = '/home/'
rjb_do_pbl_ht = rjb_sam_slsh + 'public_html'
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
url_kotw_b_ica = url_kotw_a_ica + rjb_sam_slsh
url_kotw_ica = url_kotw_b_ica + 'inne'
konto_uzytkownika = 'kwadrat'
rjb_tld_kw_a_apl = rjb_sama_tylda + konto_uzytkownika
rjb_tld_kw_b_apl = rjb_sam_slsh + rjb_sama_tylda + konto_uzytkownika
rjb_sciezka_kw = url_kotw_b_ica + rjb_tld_kw_a_apl
rjb_kt_dom_uzt = rjb_pocz_hm_dir + konto_uzytkownika
rjb_ph_uztk = rjb_kt_dom_uzt + rjb_do_pbl_ht + rjb_sam_slsh
rjb_sciezka_a_kw = rjb_sciezka_kw + rjb_sam_slsh
GenPicDir = 'gen_kowal/'
poczatek_gen = rjb_sciezka_a_kw + GenPicDir
SciezkaPlikow = rjb_ph_uztk + GenPicDir
EYK_lporz_fktr = 'lp_faktury'
rjb_kwl_sam = 'kowal'
rjb_sczk_do_kwl = rjb_kt_dom_uzt + rjb_sam_slsh + rjb_kwl_sam
LogDir = rjb_sczk_do_kwl + '/log'

def pelna_generowana_nazwa(nazwa):
    return poczatek_gen + nazwa

def dodaj_py(nazwa):
    return nazwa + '.py'

rjb_strona_pierwsza = 'l1'
rjb_py_pierwsza = dodaj_py(rjb_strona_pierwsza)
rjb_strona_piata = 'l5'
rjb_py_piata = dodaj_py(rjb_strona_piata)
rjb_strona_szosta = 'l6'
rjb_py_szosta = dodaj_py(rjb_strona_szosta)
rjb_strona_siodma = 'l7'
rjb_py_siodma = dodaj_py(rjb_strona_siodma)
rjb_strona_osma = 'l8'
rjb_py_osma = dodaj_py(rjb_strona_osma)

def fn_a_in_dwa(wersja_produkcyjna):
    if wersja_produkcyjna:
        wynik = 'inne'
    else:
        wynik = 'inne2'
    return wynik

def fn_adres_post(wersja_produkcyjna):
    return rjb_sam_slsh + fn_a_in_dwa(wersja_produkcyjna) + rjb_sam_slsh + dodaj_py('l2')

class TestConstantStrings(unittest.TestCase):
    def test_constant_strings(self):
        '''
        TestConstantStrings:
        '''
        self.assertEqual(rjb_sam_slsh, '/')
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
        self.assertEqual(url_kotw_ica, 'http://media.ciri.pl/inne')
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
        self.assertEqual(dodaj_py('a'), 'a.py')
        self.assertEqual(rjb_strona_pierwsza, 'l1')
        self.assertEqual(rjb_py_pierwsza, 'l1.py')
        self.assertEqual(rjb_strona_piata, 'l5')
        self.assertEqual(rjb_py_piata, 'l5.py')
        self.assertEqual(rjb_strona_szosta, 'l6')
        self.assertEqual(rjb_py_szosta, 'l6.py')
        self.assertEqual(rjb_strona_siodma, 'l7')
        self.assertEqual(rjb_py_siodma, 'l7.py')
        self.assertEqual(rjb_strona_osma, 'l8')
        self.assertEqual(rjb_py_osma, 'l8.py')
        self.assertEqual(fn_a_in_dwa(0), 'inne2')
        self.assertEqual(fn_a_in_dwa(1), 'inne')
        self.assertEqual(fn_adres_post(1), '/inne/l2.py')
        self.assertEqual(fn_adres_post(0), '/inne2/l2.py')
