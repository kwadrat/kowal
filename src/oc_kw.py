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
rjb_havn_ip = '78.31.136.60'

mthd_get = 'GET'
mthd_post = 'POST'

rjb_pocz_hm_dir = '/home/'
rjb_do_pbl_ht = lk_kw.rjb_sam_slsh + 'public_html'
rjb_sama_tylda = '~'
PoczObrazka = 'plik_'
RozszerzenieObrazka = '.png'
url_ameryka_http = 'http://'
rjb_hs_pocz = 'https://'
kj_beaker_dot_session = 'beaker.session'
kj_wsgi_dot_input = 'wsgi.input'

class CoreResolver(object):
    def __init__(self, adres_maszyny, adres_przystani, adres_auth):
        '''
        CoreResolver:
        '''
        self.adres_maszyny = adres_maszyny
        self.adres_przystani = adres_przystani
        self.adres_auth = adres_auth

if rq_kw.WersjaUbuntuRun:
    ##############################################################################
    if rq_kw.DocelowoElastycznyHostname:
        ##############################################################################
        core_resolver = CoreResolver('192.168.56.102', '192.168.56.102', 'havn.ciri.pl')
        ##############################################################################
    else:
        ##############################################################################
        core_resolver = CoreResolver('192.168.56.102', '192.168.56.102', 'havn.ciri.pl')
        ##############################################################################
    ##############################################################################
else:
    ##############################################################################
    if rq_kw.DocelowoElastycznyHostname:
        ##############################################################################
        core_resolver = CoreResolver('havn.ciri.pl', 'havn.ciri.pl', 'havn.ciri.pl')
        ##############################################################################
    else:
        ##############################################################################
        core_resolver = CoreResolver('media.ciri.pl', 'media.ciri.pl', 'havn.ciri.pl')
        ##############################################################################
    ##############################################################################
if rq_kw.DocelowoElastycznyHostname:
    ##############################################################################
    adres_przystani = core_resolver.adres_przystani
    ##############################################################################
else:
    ##############################################################################
    pass
    ##############################################################################
url_kotw_a_ica = url_ameryka_http + core_resolver.adres_maszyny
if rq_kw.DocelowoElastycznyHostname:
    ##############################################################################
    rjb_hs_pcztk_sam = rjb_hs_pocz + adres_przystani
    ##############################################################################
else:
    ##############################################################################
    rjb_hs_pcztk_sam = rjb_hs_pocz + core_resolver.adres_maszyny
    ##############################################################################
url_kotw_b_ica = url_kotw_a_ica + lk_kw.rjb_sam_slsh
rjb_fg_tld_d_apl = 'inne'
rjb_fg_tld_e_apl = '2'
rjb_fg_tld_f_apl = rjb_fg_tld_d_apl + rjb_fg_tld_e_apl
konto_uzytkownika = 'kwadrat'
rjb_fg_tld_a_apl = rjb_sama_tylda + konto_uzytkownika
rjb_fg_tld_b_apl = lk_kw.rjb_sam_slsh + rjb_sama_tylda + konto_uzytkownika
rjb_sciezka_kw = url_kotw_b_ica + rjb_fg_tld_a_apl
rjb_kt_dom_uzt = rjb_pocz_hm_dir + konto_uzytkownika
rjb_wsp_cr_md = rjb_kt_dom_uzt + '/ciri/media/'
rjb_ph_uztk = rjb_kt_dom_uzt + rjb_do_pbl_ht + lk_kw.rjb_sam_slsh
rjb_sciezka_a_kw = rjb_sciezka_kw + lk_kw.rjb_sam_slsh
GenPicDir = 'gen_kowal/'
poczatek_gen = rjb_sciezka_a_kw + GenPicDir
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

def pelna_generowana_nazwa(nazwa):
    return poczatek_gen + nazwa

def dodaj_py(nazwa):
    return nazwa + rjb_fg_tld_g_apl

def fn_a_in_dwa(wersja_produkcyjna):
    if wersja_produkcyjna:
        wynik = rjb_fg_tld_d_apl
    else:
        wynik = rjb_fg_tld_f_apl
    return wynik

class TestConstantStrings(unittest.TestCase):
    def test_constant_strings(self):
        '''
        TestConstantStrings:
        '''
        if rq_kw.DocelowoElastycznyHostname:
            ##############################################################################
            obk = CoreResolver('media.ciri.pl', 'havn.ciri.pl', 'havn.ciri.pl')
            ##############################################################################
        else:
            ##############################################################################
            obk = CoreResolver('media.ciri.pl', 'media.ciri.pl', 'havn.ciri.pl')
            ##############################################################################
        self.assertEqual(mthd_get, 'GET')
        self.assertEqual(mthd_post, 'POST')
        self.assertEqual(rjb_dla_drukowania, 'print')
        self.assertEqual(rjb_pocz_hm_dir, '/home/')
        self.assertEqual(rjb_do_pbl_ht, '/public_html')
        self.assertEqual(rjb_sama_tylda, '~')
        self.assertEqual(PoczObrazka, 'plik_')
        self.assertEqual(RozszerzenieObrazka, '.png')
        self.assertEqual(url_ameryka_http, 'http://')
        self.assertEqual(rjb_hs_pocz, 'https://')
        self.assertEqual(obk.adres_maszyny, 'media.ciri.pl')
        self.assertEqual(obk.adres_auth, 'havn.ciri.pl')
        if rq_kw.DocelowoElastycznyHostname:
            ##############################################################################
            self.assertEqual(obk.adres_przystani, 'havn.ciri.pl')
            ##############################################################################
        else:
            ##############################################################################
            pass
            ##############################################################################
        self.assertEqual(url_kotw_a_ica, 'http://media.ciri.pl')
        if rq_kw.DocelowoElastycznyHostname:
            ##############################################################################
            self.assertEqual(rjb_hs_pcztk_sam, 'https://havn.ciri.pl')
            ##############################################################################
        else:
            ##############################################################################
            self.assertEqual(rjb_hs_pcztk_sam, 'https://media.ciri.pl')
            ##############################################################################
        self.assertEqual(url_kotw_b_ica, 'http://media.ciri.pl/')
        self.assertEqual(konto_uzytkownika, 'kwadrat')
        self.assertEqual(rjb_fg_tld_a_apl, '~kwadrat')
        self.assertEqual(rjb_fg_tld_b_apl, '/~kwadrat')
        self.assertEqual(rjb_kt_dom_uzt, '/home/kwadrat')
        self.assertEqual(rjb_wsp_cr_md, '/home/kwadrat/ciri/media/')
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
        self.assertEqual(rjb_fg_tld_g_apl, '.py')
        self.assertEqual(dodaj_py('a'), 'a.py')
        self.assertEqual(fn_a_in_dwa(0), 'inne2')
        self.assertEqual(fn_a_in_dwa(1), 'inne')
        self.assertEqual(rjb_fg_tld_d_apl, 'inne')
        self.assertEqual(rjb_fg_tld_e_apl, '2')
        self.assertEqual(rjb_fg_tld_f_apl, 'inne2')
