#!/usr/bin/python
# -*- coding: UTF-8 -*-

import lc_kw
import le_kw
import dd_kw

altered_names = {
    'SZKOLA_PODSTAWOWA_NR35_RYBNIK': 'SZKOLA_PODSTAWOWA_NR_35_RYBNIK_SLASKA',
    'ZESPOL_SZKOLNO_PRZEDSZK_RYBNIK_GLIWICKA': 'ZESPOL_SZKOLNO_PRZEDSZK_WIELOPOLE',
    }


def make_alias(name):
    name = altered_names.get(name, name)
    return name


def locate_object_key(dfb, under_name):
    under_name = make_alias(under_name)
    key_object = le_kw.dq_object_key(dfb, under_name)
    if not key_object:
        key_object = le_kw.dq_add_new_object_key(dfb, under_name)
    ret_size = len(key_object)
    if ret_size == 1:
        key_object = key_object[0][lc_kw.fq_k_object_qv]
    else:
        raise RuntimeError('ret_size = %d' % ret_size)
    return key_object


class CommonRdWr(object):
    def __init__(self, tvk_pobor, period_server):
        '''
        CommonRdWr:
        '''
        self.krt_pobor = dd_kw.CechaEnergii(tvk_pobor)
        self.table_of_samples = self.krt_pobor.krt_table
        self.period_server = period_server
