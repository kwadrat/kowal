#!/usr/bin/python
# -*- coding: UTF-8 -*-

class KlasaBleduBazy(object):
    def ustaw_przyczyne(self, napis):
        '''
        KlasaBleduBazy:
        '''
        self.napis_przyczyny = napis

    def __init__(self):
        '''
        KlasaBleduBazy:
        '''
        self.ustaw_przyczyne('')

    def last_error(self):
        '''
        KlasaBleduBazy:
        '''
        return self.napis_przyczyny


egz_bbd = KlasaBleduBazy()
