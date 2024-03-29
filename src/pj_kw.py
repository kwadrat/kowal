#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ckd_kw
import ckb_kw
import fv_kw

KSZ_Zmiennoprzecinkowa = 'zmiennoprzecinkowa z przecinkiem'

if ckd_kw.three_or_more:
    text_type_tpl = (str,)
else:
    text_type_tpl = (unicode, str)  # noqa: F821


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
                    if type(wynik) in text_type_tpl and '.' in wynik:
                        print('W kolumnie "%s" i wierszu "%s" zamiast kropki wpisz przecinek:' % (lb_col, wiersz))
                        print('Niepoprawnie jest: "%s"' % (wynik))
                        print('Powinno byc:       "%s"' % (wynik.replace('.', ',')))
                    else:
                        print('Nierozpoznany blad:')
                        if 1:
                            tmp_format = 'lb_col'
                            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
                        if 1:
                            tmp_format = 'wiersz'
                            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
                        if 1:
                            tmp_format = 'type(wynik)'
                            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
                        if 1:
                            tmp_format = 'wynik'
                            print('Eval: %s %s' % (tmp_format, eval(tmp_format)))
                    ckb_kw.both_input('Nacisnij Enter')
            else:
                raise RuntimeError("Nieznany ksztalt: %s" % repr(ksztalt))
        return wynik
