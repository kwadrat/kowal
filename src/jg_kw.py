#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ze_kw
import hd_kw

class JedenWiersz(object):
    def set_color(self, barwa_wiersza):
        '''
        JedenWiersz:
        '''
        self.barwa_wiersza = barwa_wiersza

    def __init__(self, nazwa, table_row):
        '''
        JedenWiersz:
        '''
        self.nazwa = nazwa
        self.table_row = table_row
        self.set_color(None)

    def get_line_name(self):
        '''
        JedenWiersz:
        '''
        return self.nazwa

    def get_line_row(self):
        '''
        JedenWiersz:
        '''
        return self.table_row

    def to_comma(self):
        '''
        JedenWiersz:
        '''
        self.table_row = map(hd_kw.przecinkowane_pole, self.table_row)

    def use_color(self):
        '''
        JedenWiersz:
        '''
        if self.barwa_wiersza:
            self.table_row = map(
                lambda x: ze_kw.pokoloruj(x, self.barwa_wiersza),
                self.table_row)
