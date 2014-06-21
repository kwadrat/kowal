#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

class JestemObca(object):
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

class TestObcejFaktury(unittest.TestCase):

    def test_0_obcej_faktury(self):
        '''
        TestObcejFaktury:
        '''
        obk = JestemObca()
        obk.okresl_obcosc(obcosc=0, przykrycie=0)
        self.assertEqual(obk.jestem_specjalna(), 0)
        self.assertEqual(obk.jestem_przykryta(), 0)

    def test_1_obcej_faktury(self):
        '''
        TestObcejFaktury:
        '''
        obk = JestemObca()
        obk.okresl_obcosc(obcosc=0, przykrycie=1)
        self.assertEqual(obk.jestem_specjalna(), 1)
        self.assertEqual(obk.jestem_przykryta(), 1)

    def test_2_obcej_faktury(self):
        '''
        TestObcejFaktury:
        '''
        obk = JestemObca()
        obk.okresl_obcosc(obcosc=1, przykrycie=0)
        self.assertEqual(obk.jestem_specjalna(), 1)
        self.assertEqual(obk.jestem_przykryta(), 0)

    def test_3_obcej_faktury(self):
        '''
        TestObcejFaktury:
        '''
        obk = JestemObca()
        obk.okresl_obcosc(obcosc=1, przykrycie=1)
        self.assertEqual(obk.jestem_specjalna(), 1)
        self.assertEqual(obk.jestem_przykryta(), 1)
