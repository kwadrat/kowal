#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Prostokąt do narysowania na wykresie słupkowym, z możliwością zaznaczenia
przekroczenia mocy (moc pobrana jest większa niż moc zamówiona)
'''


class ProstokatDoRysowania(object):
    def __init__(self, x1, y1, x2, y2):
        '''
        ProstokatDoRysowania:
        '''
        self.wspolrzedne = (x1, y1, x2, y2)
        self.przekroczenie_a_umw = 0

    def zwroc_cztery_wsp(self):
        '''
        ProstokatDoRysowania:
        '''
        return self.wspolrzedne

    def zaznacz_przekroczenie(self, przekroczenie_a_umw):
        '''
        ProstokatDoRysowania:
        '''
        self.przekroczenie_a_umw = przekroczenie_a_umw
