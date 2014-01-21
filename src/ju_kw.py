#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

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

rh_ozncz_zst_a = 'ZST'
rh_ozncz_plw_a = 'PLW'
rh_ozncz_jdo_a = 'JDO'
rh_ozncz_cki_a = 'CKI'
rh_kol_data_dla_plyw_judo = ['AG', 'AH', 'AG']
rh_etk_daty_plyw_judo = u'Data Noty Księgowej         dla           Kryta Pływalnia i Pawilon Judo'

legalne_wzory_sumy_brutto = frozenset([
    u'Wartość brutto          [zł]',
    u'Koszt brutto z faktury Vattenfall S/D [zł]',
    u'Wartość brutto z faktury S/D [zł]',
    ])

def sprawdz_ogolnie_zgodnosc(elem, zbior, dodatkowy=None):
    if elem not in zbior:
        tmp_format = 'elem'; print 'Eval:', tmp_format, eval(tmp_format)
        tmp_format = 'repr(elem)'; print 'Eval:', tmp_format, eval(tmp_format)
        tmp_format = 'zbior'; print 'Eval:', tmp_format, eval(tmp_format)
        if dodatkowy is not None:
            tmp_format = 'dodatkowy'; print 'Eval:', tmp_format, eval(tmp_format)
        raise RuntimeError('Nieznany')
