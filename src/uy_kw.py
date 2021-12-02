#!/usr/bin/python
# -*- coding: UTF-8 -*-

import dv_kw
import ux_kw


def tassertEqual(self, odp, wzor):
    if odp != wzor:
        dv_kw.zapisz_dla_diagnostyki(odp, wzor)
    self.assertTrue(odp == wzor)


def jdn_ogol_ltra(fnc_x, *args, **kwargs):
    lnc_x = ux_kw.LancOgolOgniw()
    fnc_x(lnc_x, *args, **kwargs)
    return lnc_x.polaczona_tresc()


def nassertEqual(self, fnc_a, wzor, *args, **kwargs):
    odp = jdn_ogol_ltra(fnc_a, *args, **kwargs)
    if odp != wzor:
        dv_kw.zapisz_dla_diagnostyki(odp, wzor)
    self.assertTrue(odp == wzor)
