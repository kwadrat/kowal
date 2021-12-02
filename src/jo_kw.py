#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


class JestemObca(object):
    '''Informuje, że faktura jest obca'''

    def __init__(self):
        '''
        JestemObca:
        '''
        self.mam_obcosc = False

    def okresl_obcosc(self, obcosc):
        '''
        JestemObca:
        '''
        self.mam_obcosc = obcosc

    def jestem_specjalna(self):
        '''
        JestemObca:
        '''
        return self.mam_obcosc

    def tekst_opisu(self):
        '''
        JestemObca:
        '''
        if self.mam_obcosc:
            tmp_opis = 'Jestem_obcy'
        else:
            tmp_opis = ''
        return tmp_opis

ob_fjo = JestemObca()


class TestObcejFaktury(unittest.TestCase):

    def test_0_obcej_faktury(self):
        '''
        TestObcejFaktury:
        '''
        obk = JestemObca()
        obk.okresl_obcosc(obcosc=0)
        self.assertEqual(obk.jestem_specjalna(), 0)
        self.assertEqual(obk.tekst_opisu(), '')

    def test_1_obcej_faktury(self):
        '''
        TestObcejFaktury:
        '''
        obk = JestemObca()
        obk.okresl_obcosc(obcosc=1)
        self.assertEqual(obk.jestem_specjalna(), 1)
        self.assertEqual(obk.tekst_opisu(), 'Jestem_obcy')
