#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import lk_kw
import rq_kw

# Nie ujednolicaj adresu IP z nazwą, bo na razie chcemy synchronizować różne treści
rjb_klnt_ip = '87.101.66.154'
rjb_havn_ip = '78.31.136.60'

mthd_get = 'GET'
mthd_post = 'POST'
mthd_head = 'HEAD'

rjb_pocz_hm_dir = '/home/'
rjb_do_pbl_ht = lk_kw.rjb_sam_slsh + 'public_html'
rjb_sama_tylda = '~'
PoczObrazka = 'plik_'
RozszerzenieObrazka = '.png'
url_ameryka_http = 'https://'
rjb_hs_pocz = 'https://'
kj_beaker_dot_session = 'beaker.session'
kj_wsgi_dot_input = 'wsgi.input'
konto_uzytkownika = 'kwadrat'
rjb_fg_tld_a_apl = rjb_sama_tylda + konto_uzytkownika
GenPicDir = 'gen_kowal/'


class CoreResolver(object):
    def __init__(self, adres_maszyny, port_nr=None):
        '''
        CoreResolver:
        '''
        if port_nr is None or port_nr == 443:
            wstawka_portu = ''
        else:
            wstawka_portu = ':%(port_nr)d' % dict(port_nr=port_nr)
        self.adres_maszyny = adres_maszyny + wstawka_portu
        self.rjb_hs_pcztk_sam = rjb_hs_pocz + self.adres_maszyny
        self.rjb_hs_pcztk_slsh = self.rjb_hs_pcztk_sam + lk_kw.rjb_sam_slsh
        self.url_kotw_b_ica = url_ameryka_http + self.adres_maszyny + lk_kw.rjb_sam_slsh
        self.rjb_sciezka_kw = self.url_kotw_b_ica + rjb_fg_tld_a_apl
        self.rjb_sciezka_a_kw = self.rjb_sciezka_kw + lk_kw.rjb_sam_slsh
        self.poczatek_gen = self.rjb_sciezka_a_kw + GenPicDir

    def pelna_generowana_nazwa(self, nazwa):
        '''
        CoreResolver:
        '''
        return self.poczatek_gen + nazwa


if rq_kw.WersjaUbuntuRun:
    ##############################################################################
    core_resolver = CoreResolver('media.ciri.pl')
    ##############################################################################
else:
    ##############################################################################
    core_resolver = CoreResolver('media.ciri.pl')
    ##############################################################################
rjb_fg_tld_d_apl = 'inne'
rjb_fg_tld_e_apl = '2'
rjb_fg_tld_f_apl = rjb_fg_tld_d_apl + rjb_fg_tld_e_apl
rjb_fg_tld_b_apl = lk_kw.rjb_sam_slsh + rjb_sama_tylda + konto_uzytkownika
rjb_kt_dom_uzt = rjb_pocz_hm_dir + konto_uzytkownika
rjb_wsp_cr_md = rjb_kt_dom_uzt + '/ciri/media/'
rjb_ph_uztk = rjb_kt_dom_uzt + rjb_do_pbl_ht + lk_kw.rjb_sam_slsh
SciezkaPlikow = rjb_ph_uztk + GenPicDir
EYK_lporz_fktr = 'lp_faktury'
rjb_kwl_sam = 'kowal'
rjb_sczk_do_kwl = rjb_kt_dom_uzt + lk_kw.rjb_sam_slsh + rjb_kwl_sam
LogDir = rjb_sczk_do_kwl + '/log'
rjb_fg_tld_g_apl = '.py'
fq_kx_qv = 'kx'
fq_ky_qv = 'ky'
fq_px_qv = 'px'
fq_py_qv = 'py'
fq_nowy_this_qv = 'nowy_this'
rjb_dla_drukowania = 'print'


def dodaj_py(nazwa):
    return nazwa + rjb_fg_tld_g_apl


def fn_a_in_dwa(wersja_produkcyjna):
    if wersja_produkcyjna:
        wynik = rjb_fg_tld_d_apl
    else:
        wynik = rjb_fg_tld_f_apl
    return wynik


def core_for_testing(port_nr=None):
    return CoreResolver('work.ciri.pl', port_nr)


class TestConstantStrings(unittest.TestCase):
    def test_constant_strings(self):
        '''
        TestConstantStrings:
        '''
        obk = core_for_testing()
        self.assertEqual(mthd_get, 'GET')
        self.assertEqual(mthd_post, 'POST')
        self.assertEqual(mthd_head, 'HEAD')
        self.assertEqual(rjb_dla_drukowania, 'print')
        self.assertEqual(rjb_pocz_hm_dir, '/home/')
        self.assertEqual(rjb_do_pbl_ht, '/public_html')
        self.assertEqual(rjb_sama_tylda, '~')
        self.assertEqual(PoczObrazka, 'plik_')
        self.assertEqual(RozszerzenieObrazka, '.png')
        self.assertEqual(url_ameryka_http, 'https://')
        self.assertEqual(rjb_hs_pocz, 'https://')
        self.assertEqual(obk.adres_maszyny, 'work.ciri.pl')
        self.assertEqual(obk.rjb_hs_pcztk_sam, 'https://work.ciri.pl')
        self.assertEqual(obk.rjb_hs_pcztk_slsh, 'https://work.ciri.pl/')
        self.assertEqual(obk.url_kotw_b_ica, 'https://work.ciri.pl/')
        self.assertEqual(konto_uzytkownika, 'kwadrat')
        self.assertEqual(rjb_fg_tld_a_apl, '~kwadrat')
        self.assertEqual(rjb_fg_tld_b_apl, '/~kwadrat')
        self.assertEqual(rjb_kt_dom_uzt, '/home/kwadrat')
        self.assertEqual(rjb_wsp_cr_md, '/home/kwadrat/ciri/media/')
        self.assertEqual(rjb_ph_uztk, '/home/kwadrat/public_html/')
        self.assertEqual(obk.rjb_sciezka_kw, 'https://work.ciri.pl/~kwadrat')
        self.assertEqual(obk.rjb_sciezka_a_kw, 'https://work.ciri.pl/~kwadrat/')
        self.assertEqual(GenPicDir, 'gen_kowal/')
        self.assertEqual(obk.poczatek_gen, 'https://work.ciri.pl/~kwadrat/gen_kowal/')
        self.assertEqual(SciezkaPlikow, '/home/kwadrat/public_html/gen_kowal/')
        self.assertEqual(obk.pelna_generowana_nazwa('tmp.png'), 'https://work.ciri.pl/~kwadrat/gen_kowal/tmp.png')
        self.assertEqual(obk.pelna_generowana_nazwa('inny.jpg'), 'https://work.ciri.pl/~kwadrat/gen_kowal/inny.jpg')
        self.assertEqual(rjb_klnt_ip, '87.101.66.154')
        self.assertEqual(rjb_kwl_sam, 'kowal')
        self.assertEqual(rjb_sczk_do_kwl, '/home/kwadrat/kowal')
        self.assertEqual(LogDir, '/home/kwadrat/kowal/log')
        self.assertEqual(rjb_fg_tld_g_apl, '.py')
        self.assertEqual(dodaj_py('a'), 'a.py')
        self.assertEqual(fn_a_in_dwa(0), 'inne2')
        self.assertEqual(fn_a_in_dwa(1), 'inne')
        self.assertEqual(rjb_fg_tld_d_apl, 'inne')
        self.assertEqual(rjb_fg_tld_e_apl, '2')
        self.assertEqual(rjb_fg_tld_f_apl, 'inne2')
