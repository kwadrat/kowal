#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesięcy w ciągu roku
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import dn_kw
import lh_kw
import lt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

OgolnySzeregListPoborow = lt_kw.OgolnySzeregListPoborow

class PomiaryPoborowMiesiecznie(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        tvk_data = tgk.wez_date()
        my_year, my_month = dn_kw.rok_mies_z_napisu(tvk_data)
        my_start_day, my_end_day = dn_kw.ZakresMiesiaca(my_year, my_month)
        aqr = None
        OgolnySzeregListPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        lst_h = lh_kw.ListaHTML()
        return lst_h.polacz_html()
