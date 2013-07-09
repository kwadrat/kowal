#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JestemObca:
    '''Informuje, że faktura jest obca lub przykryta fakturą korygującą'''

    def __init__(self):
        '''
        JestemObca:
        '''
        self.mam_obcosc = False
        self.mam_przykrycie = False

    def okresl_obcosc(self, obcosc, przykrycie):
        '''
        JestemObca:
        '''
        self.mam_obcosc = obcosc
        self.mam_przykrycie = przykrycie

    def jestem_specjalna(self):
        '''
        JestemObca:
        '''
        return self.mam_obcosc or self.mam_przykrycie

    def jestem_przykryta(self):
        '''
        JestemObca:
        '''
        return self.mam_przykrycie

    def tekst_opisu(self):
        '''
        JestemObca:
        '''
        wynik = []
        if self.mam_obcosc:
            wynik.append('Jestem_obcy')
        if self.mam_przykrycie:
            wynik.append('Jestem_przykryty')
        return ' '.join(wynik)

ob_fjo = JestemObca()
