#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

import hj_kw


class SpecifiedYears(object):
    def __init__(self, collected_years=None):
        '''
        SpecifiedYears:
        '''
        if collected_years is None:
            self.collected_years = []
        else:
            self.collected_years = collected_years
            self.sort_naturally()

    def get_length(self):
        '''
        SpecifiedYears:
        '''
        return len(self.collected_years)

    def add_one_year(self, the_year):
        '''
        SpecifiedYears:
        '''
        self.collected_years.append(the_year)
        self.sort_naturally()

    def reverse_but_last(self):
        '''
        SpecifiedYears:
        '''
        hj_kw.reverse_but_last(self.collected_years)

    def get_elements(self):
        '''
        SpecifiedYears:
        '''
        return self.collected_years

    def year_exists(self, the_year):
        '''
        SpecifiedYears:
        '''
        return the_year in self.collected_years

    def first_year(self):
        '''
        SpecifiedYears:
        '''
        return self.collected_years[0]

    def last_year(self):
        '''
        SpecifiedYears:
        '''
        return self.collected_years[-1]

    def new_extended_span(self):
        '''
        SpecifiedYears:
        '''
        specified_years = SpecifiedYears(range(self.first_year(), self.last_year() + 2 + 1))
        return specified_years

    def sort_naturally(self, reverse=0):
        '''
        SpecifiedYears:
        '''
        self.collected_years.sort(reverse=reverse)

    def enum_pairs(self):
        '''
        SpecifiedYears:
        '''
        return enumerate(self.collected_years)

    def add_year_if_missing(self, the_year):
        '''
        SpecifiedYears:
        '''
        if not self.year_exists(the_year):
            self.add_one_year(the_year)

    def get_cont_elements(self):
        '''
        SpecifiedYears:
        '''
        return range(self.first_year(), self.last_year() + 1)


class TestYearCollection(unittest.TestCase):
    def test_construction_sql(self):
        '''
        TestYearCollection:
        '''
        obk = SpecifiedYears()
        self.assertEqual(obk.get_length(), 0)
        obk.add_one_year(2012)
        self.assertEqual(obk.get_length(), 1)
        obk.add_one_year(2013)
        obk.add_one_year(2014)
        self.assertEqual(obk.first_year(), 2012)
        self.assertEqual(obk.last_year(), 2014)
        obk2 = obk.new_extended_span()
        self.assertEqual(obk2.get_elements(), [2012, 2013, 2014, 2015, 2016])
        obk.reverse_but_last()
        self.assertEqual(obk.get_elements(), [2013, 2012, 2014])
        self.assertEqual(obk.year_exists(2012), 1)
        self.assertEqual(obk.year_exists(2011), 0)
        obk.sort_naturally()
        self.assertEqual(obk.get_elements(), [2012, 2013, 2014])
        obk.sort_naturally(reverse=True)
        self.assertEqual(obk.get_elements(), [2014, 2013, 2012])

    def test_predefined_years(self):
        '''
        TestYearCollection:
        '''
        obk = SpecifiedYears([2014, 2013])
        self.assertEqual(obk.get_elements(), [2013, 2014])
        self.assertEqual(list(obk.enum_pairs()), [(0, 2013), (1, 2014)])
        obk.add_one_year(2012)
        self.assertEqual(obk.get_elements(), [2012, 2013, 2014])

    def test_add_lacking_year(self):
        '''
        TestYearCollection:
        '''
        obk = SpecifiedYears()
        obk.add_year_if_missing(2012)
        self.assertEqual(obk.get_elements(), [2012])
        obk.add_year_if_missing(2012)
        self.assertEqual(obk.get_elements(), [2012])

    def test_continuous_fill(self):
        '''
        TestYearCollection:
        '''
        obk = SpecifiedYears()
        obk.add_one_year(2010)
        obk.add_one_year(2012)
        self.assertEqual(obk.get_cont_elements(), [2010, 2011, 2012])
