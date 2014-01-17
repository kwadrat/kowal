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
