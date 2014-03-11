#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Wspólna klasa dla arkusza generowania raportu dla gazu W-5
i energii elektrycznej C-21
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
