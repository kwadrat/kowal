#!/usr/bin/python
# -*- coding: UTF-8 -*-

import inspect

# Do ilu poziomów pokazujemy zagnieżdżenie przy diagnozowaniu klas
TymczasowoGlebokosc = 0

class GlebiaZagniezdzenia:
    def __init__(self, poziom):
        '''
        GlebiaZagniezdzenia:
        '''
        self.poziom_glebokosci_zagn = poziom

    def glebokosc_zagn(self, dodatek = None):
        '''
        GlebiaZagniezdzenia:
        '''
        if self.poziom_glebokosci_zagn <= TymczasowoGlebokosc:
            napis = inspect.stack()[1][3]
            napis = eval('self.%s.__doc__' % napis)
            napis = napis.lstrip() # Dla sklejenia w jednej linii
            lista_napisu = [
            'GlZagnFn',
            ': ',
            napis,
            ]
            if dodatek is not None:
                lista_napisu.append(dodatek)
            polaczony_napis = ''.join(lista_napisu)
            print polaczony_napis
