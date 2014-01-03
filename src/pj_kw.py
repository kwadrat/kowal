#!/usr/bin/python
# -*- coding: UTF-8 -*-

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fv_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

KSZ_Zmiennoprzecinkowa = 'zmiennoprzecinkowa z przecinkiem'

class ArkuszExcel(object):
    def __init__(self, sh):
        '''
        ArkuszExcel:
        '''
        self.sh = sh

    def vx_odczyt(self, lb_col, wiersz, ksztalt=None):
        '''
        ArkuszExcel:
        '''
        wynik = self.sh.Cells(wiersz, fv_kw.vx_one.vx_lt(lb_col)).Value
        if ksztalt is not None:
            if ksztalt == KSZ_Zmiennoprzecinkowa:
                if type(wynik) is not float:
                    if type(wynik) in (unicode, str) and '.' in wynik:
                        print 'W kolumnie "%s" i wierszu "%s" zamiast kropki wpisz przecinek:' % (lb_col, wiersz)
                        print 'Niepoprawnie jest: "%s"' % (wynik)
                        print 'Powinno byc:       "%s"' % (wynik.replace('.', ','))
                    else:
                        print 'Nierozpoznany blad:'
                        tmp_format = "lb_col"; print 'Eval:', tmp_format, repr(eval(tmp_format))
                        tmp_format = "wiersz"; print 'Eval:', tmp_format, repr(eval(tmp_format))
                        tmp_format = "type(wynik)"; print 'Eval:', tmp_format, repr(eval(tmp_format))
                        tmp_format = "wynik"; print 'Eval:', tmp_format, repr(eval(tmp_format))
                    raw_input('Nacisnij Enter')
            else:
                raise RuntimeError("Nieznany ksztalt: %s" % repr(ksztalt))
        return wynik
