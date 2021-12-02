#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ib_kw
import fy_kw
import ze_kw

class FormularzBazowySkrawkow(object):
    def __init__(self, strona_bazowa):
        '''
        FormularzBazowySkrawkow:
        '''
        self.strona_bazowa = strona_bazowa

    def zbierz_2html(self, tgk, dfb):
        '''
        FormularzBazowySkrawkow:
        Wartość zwracana:
        - lista kawałków strony HTML
        '''
        w = []

        w.append(ze_kw.op_fmd(adres=self.strona_bazowa, name=fy_kw.lxa_43_inst))
        for elem in self.moj_form:
            w.append(elem.zbierz_html(tgk, dfb))
        w.append(ze_kw.formularz_1c_kon_formularza)
        return w

    def get_from_form(self, tgk, klucz):
        '''
        FormularzBazowySkrawkow:
        '''
        for elem in self.moj_form:
            if ib_kw.AimToObjectFieldName:
                ##############################################################################
                if elem.moje_pole == klucz:
                    return elem.pobierz_wartosc(tgk)
                ##############################################################################
            else:
                ##############################################################################
                if elem.moje_pole == klucz:
                    return elem.pobierz_wartosc(tgk)
                ##############################################################################
        raise RuntimeError('Nieznany klucz: %s %s' % (repr(klucz), repr(self.moj_form)))

    def mamy_wspolny_komplet_pol(self, tgk, dfb):
        '''
        FormularzBazowySkrawkow:
        Wartość zwrotna (logiczna) mówi, czy mamy komplet wszystkich
        potrzebnych danych z formularza
        '''
        nasz_zbior = set() # Zbiór nazw wypełnionych pól
        for elem in self.moj_form:
            wynik = elem.analiza_parametrow(tgk, dfb)
            # Dopiero po analizie pole wartości będzie wypełnione
            # i dopiero teraz można pobrać wartość pola
            if wynik: # Sprawdź, czy mieliśmy to pole w formularzu
                nasz_zbior.add(elem.moje_pole) # Dostaliśmy wartość tego pola
        brakujace_pola = self.potrzebne_mi_pola - nasz_zbior
        return not brakujace_pola
