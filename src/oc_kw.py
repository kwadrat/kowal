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
if rq_kw.WersjaUbuntuRun:
    ##############################################################################
    adres_maszyny = '192.168.56.101'
    ##############################################################################
else:
    ##############################################################################
    adres_maszyny = 'media.ciri.pl'
    ##############################################################################
url_kotw_a_ica = url_ameryka_http + adres_maszyny
url_kotw_b_ica = url_kotw_a_ica + rjb_sam_slsh
konto_uzytkownika = 'kwadrat'
rjb_tld_kw_a_apl = rjb_sama_tylda + konto_uzytkownika
rjb_sciezka_kw = url_kotw_b_ica + rjb_tld_kw_a_apl
rjb_kt_dom_uzt = rjb_pocz_hm_dir + konto_uzytkownika
rjb_ph_uztk = rjb_kt_dom_uzt + rjb_do_pbl_ht + rjb_sam_slsh
rjb_sciezka_a_kw = rjb_sciezka_kw + rjb_sam_slsh
GenPicDir = 'gen_kowal/'
poczatek_gen = rjb_sciezka_a_kw + GenPicDir
SciezkaPlikow = rjb_ph_uztk + GenPicDir
EYK_lporz_fktr = 'lp_faktury'

def pelna_generowana_nazwa(nazwa):
    return poczatek_gen + nazwa

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
        self.assertEqual(adres_maszyny, 'media.ciri.pl')
        self.assertEqual(url_kotw_a_ica, 'http://media.ciri.pl')
        self.assertEqual(url_kotw_b_ica, 'http://media.ciri.pl/')
        self.assertEqual(konto_uzytkownika, 'kwadrat')
        self.assertEqual(rjb_tld_kw_a_apl, '~kwadrat')
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
