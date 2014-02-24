#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import jr_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

wykaz_pytan = '''\
'''

def wykonaj_zapytanie(dfb):
    pytanie_reczne = wykaz_pytan.splitlines()[-1]
    print repr(pytanie_reczne)
    wynik = dfb.query_old_dct(pytanie_reczne)
    for rekord in wynik:
        print rekord
    print jr_kw.non_wrapped_lines()
