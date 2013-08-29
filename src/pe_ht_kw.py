#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Udawanie żądania WWW podczas wykonywania testów
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import oc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

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
        return 5

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
