#!/usr/bin/python
# -*- coding: UTF-8 -*-

wykaz_pytan = '''\
'''

def wykonaj_zapytanie(dfb):
    pytanie_reczne = wykaz_pytan.splitlines()[-1]
    print repr(pytanie_reczne)
    wynik = dfb.query_old_dct(pytanie_reczne)
    for rekord in wynik:
        print rekord
    print '# ' 'v' 'i' 'm' ': nowrap'
