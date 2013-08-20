#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Analiza poboru - pomiarowy szereg list dla miesięcy w ciągu roku
'''

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import lm_kw
import ze_kw
import dn_kw
import le_kw
import lw_kw
import lq_kw
import lh_kw
import jb_kw
import ox_kw
import wn_kw
import gc_kw
import lt_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

OgolnySzeregListPoborow = lt_kw.OgolnySzeregListPoborow

class PomiaryPoborowMiesiecznie(OgolnySzeregListPoborow):
    def __init__(self, tgk, dfb, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        '''
        aqr = ox_kw.SzkieletMiesiecznyDlaPoborow(krt_pobor)
        OgolnySzeregListPoborow.__init__(self, tgk, aqr, dfb, krt_pobor)

    def html_szeregu_poborow(self, krt_pobor):
        '''
        PomiaryPoborowMiesiecznie:
        qaz - powielenie z gd_kw.py
        '''
        lst_h = lh_kw.ListaHTML()
        tvk_data = self.tgk.wez_date()
        fvk_rok, fvk_miesiac = dn_kw.rok_mies_z_napisu(tvk_data)
        zbiornik_przedzialow = {}
        result = le_kw.dq_liczniki_poboru_w_roku(self.dfb, self.table_name, self.id_obiekt, fvk_rok)
        for single_record in result:
            fvk_rok, fvk_miesiac = dn_kw.rok_mies_z_napisu(str(single_record[lc_kw.fq_m_date_qv]))
            if fvk_miesiac not in zbiornik_przedzialow:
                zbiornik_przedzialow[fvk_miesiac] = []
            zbiornik_przedzialow[fvk_miesiac].append(single_record[lc_kw.fq_m_sum_qv])
        all_keys = zbiornik_przedzialow.keys()
        all_keys.sort()
        for single_key in all_keys:
            akt = single_key - 1
            nast = akt + 1
            list_of_values = zbiornik_przedzialow[single_key]
            kwota = lq_kw.sum_of_not_nones(krt_pobor.krt_vl_fnctn, list_of_values)
            kwota = lm_kw.dec2flt(kwota)
            slownik_qm = wn_kw.KlasaSlownika()
            slownik_qm.jh_ustaw_kwt_qm(kwota)
            self.dnw.odcinki_bazowe.app_end(jb_kw.JedenOdcinekBazowy(2 * akt, 2 * nast, slownik_qm))
        vert_axis = self.dnw.odcinki_bazowe.zakres_pionowy()
        ms = gc_kw.PoboroweOgolneSlupki(self.tgk, self.aqr, self.dnw, lw_kw.PDS_Miesiace)
        ms.wyznacz_poborowe_slupki(vert_axis, krt_pobor)
        moja_suma = krt_pobor.cumulative_value
        moja_jednostka = krt_pobor.krt_jedn
        opis_dotyczy = []
        # qaz - duplikat
        opis_dotyczy.append(ze_kw.sp_stl(
            krt_pobor.krt_etykieta,
            lm_kw.rzeczywista_na_napis(moja_suma),
            moja_jednostka))
        # qaz - duplikat
        if vert_axis.MaxY:
            ms.podpisz_obie_osie(vert_axis, krt_pobor)
            on_mouse = {}
            kod_html = ms.wykreslanie_slupkow(on_mouse)
            lst_h.ddj(''.join(opis_dotyczy))
            lst_h.ddj(kod_html)
        else:
            lst_h.ddj('Brak zróżnicowania danych w pionie, MaxY=%s' % repr(vert_axis.MaxY))
        return lst_h.polacz_html()
