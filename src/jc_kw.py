#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import gv_kw
import lm_kw
import dn_kw

dc_d_style = dict(fore_colour=gv_kw.ECR_red)
dc_e_style = dict(fore_colour=gv_kw.ECR_yellow)
dc_f_style = dict(fore_colour=gv_kw.ECR_light_turquoise)

def wyznacz_weekend(nkd):
    jestem_weekend = not dn_kw.RoboczyDnia(nkd)
    return jestem_weekend

def nr_of_day(one_date):
    nkd = dn_kw.napis_na_numer_dnia(str(one_date))
    return nkd

def obtain_cell_color(moc_um_dec, ten_treshold, jestem_weekend, my_sample):
    if my_sample > moc_um_dec:
        dc_b_style = dc_d_style
    elif my_sample >= ten_treshold:
        dc_b_style = dc_e_style
    elif jestem_weekend:
        dc_b_style = dc_f_style
    else:
        dc_b_style = {}
    return dc_b_style

class CellDesc(object):
    def __init__(self, moc_um_dec, ten_treshold, jestem_weekend):
        '''
        CellDesc:
        '''
        self.moc_um_dec = moc_um_dec
        self.ten_treshold = ten_treshold
        self.jestem_weekend = jestem_weekend

class TestCellFeatures(unittest.TestCase):
    def test_dec_type(self):
        '''
        TestCellFeatures:
        '''
        moc_um_dec = lm_kw.a2d('30')
        ten_treshold = lm_kw.a2d('3.1104')
        jestem_weekend = True
        obk = CellDesc(moc_um_dec, ten_treshold, jestem_weekend)
