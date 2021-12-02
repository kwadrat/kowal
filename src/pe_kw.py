#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Udawanie żądania WWW podczas wykonywania testów
'''

import oc_kw

class PseudoReq(object):
    def __init__(self, lokalny_the_building=None):
        '''
        PseudoReq:
        '''
        self.lokalny_the_building = lokalny_the_building

    def get_remote_host(self):
        '''
        PseudoReq:
        '''
        return oc_kw.rjb_klnt_ip

    def write(self, dane):
        '''
        PseudoReq:
        '''
        open('/tmp/wyjscie_z_aplikacji_kw.html', 'ab').write(dane)

    def int_num_dflt_post(self, etyk):
        '''
        PseudoReq:
        '''
        return self.lokalny_the_building

    def s_dflt_get(self, etyk, domyslnie=None):
        '''
        PseudoReq:
        '''
        return domyslnie

    def posiadane_etykiety(self):
        '''
        PseudoReq:
        '''
        return []
