#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lc_kw
import jl_kw
import lw_kw
import gx_kw
import jc_kw
import nc_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

CommonWriter = nc_kw.CommonWriter

class EnergyWriter(CommonWriter):
    def __init__(self):
        '''
        EnergyWriter:
        '''
        period_server = jl_kw.HourServer()
        CommonWriter.__init__(self, lw_kw.Dm_Energy, period_server)

    def generate_for_a_day(self, xwg, my_data, base_data_line, day_nr):
        '''
        EnergyWriter:
        '''
        row = base_data_line + day_nr
        nkd = jc_kw.nr_of_day(my_data[lc_kw.fq_m_date_qv])
        jestem_weekend = jc_kw.wyznacz_weekend(nkd)
        dc_b_style = nc_kw.weekend_b_style(jestem_weekend)
        for sample_index, my_sample in enumerate(my_data[lc_kw.fq_m_samples_qv]):
            col = self.first_sample_column + sample_index
            xwg.zapisz_flt(row, col, my_sample, kl_miejsc=2, **dc_b_style)

    def generate_for_month(self, xwg, dane_bazy, nr_month, dost_wiersz):
        '''
        EnergyWriter:
        '''
        if nc_kw.month_enabled(nr_month):
            all_dates = nc_kw.unique_sorted(dane_bazy, lc_kw.fq_m_date_qv)
            all_hours = self.period_server.time_for_header
            first_line = dost_wiersz.zabierz_wiersze(len(all_dates) + 2)
            base_data_line = first_line + 1
            self.generate_dates_vertically(xwg, all_dates, base_data_line)
            self.generate_hours_horizontally(xwg, all_hours, first_line)
            for day_nr, my_data in enumerate(dane_bazy):
                self.generate_for_a_day(xwg, my_data, base_data_line, day_nr)

    def generate_for_object(self, xwg, dane_bazy, name, uu_maper):
        '''
        EnergyWriter:
        '''
        dost_wiersz = gx_kw.Wierszownik(0)
        xwg.add_a_sheet(uu_maper.get_short_name(name))
        selected_data = nc_kw.dla_podanej_nazwy(dane_bazy, name)
        self.setup_col_widths(xwg)
        month_dict, all_months = nc_kw.wyznacz_slownik_miesiaca(selected_data)
        for nr_month, moj_rm in enumerate(all_months):
            my_data = month_dict[moj_rm]
            self.generate_for_month(xwg, my_data, nr_month, dost_wiersz)

class TestEnergyParts(unittest.TestCase):
    def test_energy_parts(self):
        '''
        TestEnergyParts:
        '''
