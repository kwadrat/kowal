#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Wspólna klasa dla arkusza generowania raportu dla gazu W-5
i energii elektrycznej C-21
'''


class OgolnyObszarArkusza(object):
    def __init__(self):
        '''
        OgolnyObszarArkusza:
        '''

    def assign_column_numbering(self):
        '''
        OgolnyObszarArkusza:
        '''
        for kl_assigned_col, jedna_kolumna in enumerate(self.wszystkie_moje_kolumny()):
            jedna_kolumna.assign_target_column(kl_assigned_col)

    def samo_przepisanie_kolumn(self, xwg):
        '''
        OgolnyObszarArkusza:
        '''
        for jedna_kolumna in self.wszystkie_moje_kolumny():
            jedna_kolumna.przepisz_kolumne_do_arkusza(xwg, self.wiersz_bazowy_miesiecy)

    def posumuj_miesiacami_w_pionie(self):
        '''
        OgolnyObszarArkusza:
        '''
        for jedna_kolumna in self.wszystkie_moje_kolumny():
            jedna_kolumna.add_vertical_sum(self.wiersz_bazowy_miesiecy)
