#!/usr/bin/python
# -*- coding: UTF-8 -*-

lxa_1_inst = """\
    %s serial,
"""
lxa_2_inst = """\
t_f_index"""
lxa_3_inst = """\
CREATE INDEX a ON t(f);"""
lxa_4_inst = """\
CREATE INDEX %(name)s ON %(table)s(%(field)s);"""
lxa_5_inst = """\
DROP INDEX a;"""
lxa_6_inst = """\
DROP INDEX %(name)s;"""
lxa_7_inst = """\
SELECT k_object FROM uu_object WHERE account='abc';"""
lxa_8_inst = """\
SELECT %(k_object)s FROM %(uu_object)s WHERE %(account)s='%(under_name)s';"""
lxa_9_inst = """\
SELECT k_sample, f_object, m_date, m_samples FROM uu_power WHERE f_object=123 AND m_date='2013-01-31';"""
lxa_10_inst = """\
SELECT %(e_fields)s FROM %(n_table)s WHERE %(e_object)s=%(f_object)d AND %(e_date)s='%(m_date)s';"""
lxa_13_inst = """\
SELECT uu_object.account,m_date,m_samples FROM uu_power,uu_object WHERE uu_power.f_object=uu_object.k_object;"""
lxa_14_inst = """\
SELECT %(uu_object)s.%(account)s,%(e_date)s,%(e_samples)s FROM %(table_name)s,%(uu_object)s WHERE %(table_name)s.%(e_object)s=%(uu_object)s.%(k_object)s;"""
lxa_15_inst = """\
INSERT INTO uu_object (account) VALUES ('n') RETURNING k_object;"""
lxa_16_inst = """\
INSERT INTO %(uu_object)s (%(account)s) VALUES ('%(under_name)s') RETURNING %(k_object)s;"""
lxa_17_inst = """\
INSERT INTO uu_power (f_object, m_date, m_samples) VALUES (123, '2013-01-31', '{NULL,NULL,NULL}');"""
lxa_18_inst = """\
INSERT INTO %(n_table)s (%(e_object)s, %(e_date)s, %(e_samples)s) VALUES (%(f_object)d, '%(m_date)s', %(m_samples)s);"""
lxa_19_inst = """\
git checkout -b akw_2013.01.31_23.59.00; git checkout master
cd ../dkw; git checkout -b akw_2013.01.31_23.59.00; git checkout master; cd ../bkw
vi co_kw.py
rm ../ckw/src/*.py; cp ../dkw/src/*.py ../ckw/src/; rm ../akw/*.py; cp *.py ../akw/; git checkout co_kw.py; touch ../akw/pw_kw.py
"""
lxa_20_inst = """\
cd ..;tar cjf bkw_2013.01.31_23.59.00.tar.bz2 bkw dkw;mv bkw_2013.01.31_23.59.00.tar.bz2 bkw; cd bkw
"""
lxa_21_inst = """\
UPDATE uu_power SET m_samples='{NULL,NULL,NULL}' WHERE k_sample=7 AND f_object=123 AND m_date='2013-01-31';"""
lxa_22_inst = """\
UPDATE %(n_table)s SET %(e_samples)s=%(m_samples)s WHERE %(e_key_sample)s=%(k_sample)d AND %(e_object)s=%(f_object)d AND %(e_date)s='%(m_date)s';"""
lxa_23_inst = """\
SELECT m_samples FROM %(my_table_name)s WHERE %(part_my_limits)s ORDER BY m_date;"""
lxa_24_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND m_date >= '2013-03-11' AND m_date < '2013-03-25' ORDER BY m_date;"""
lxa_25_inst = """\
SELECT m_samples FROM uu_energy WHERE m_date >= '2013-03-11' AND m_date < '2013-03-25' ORDER BY m_date;"""
lxa_26_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND m_date < '2013-03-25' ORDER BY m_date;"""
lxa_27_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND m_date >= '2013-03-11' ORDER BY m_date;"""
lxa_28_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND EXTRACT(dow FROM m_date)=0 ORDER BY m_date;"""
lxa_29_inst = """\
SELECT m_samples FROM uu_power WHERE f_object=1 AND EXTRACT(dow FROM m_date)=0 ORDER BY m_date;"""
lxa_30_inst = """\
SELECT m_samples FROM uu_power WHERE f_object=18 AND m_date='2013-01-31';"""
lxa_31_inst = """\
SELECT %(e_samples)s FROM %(table_name)s WHERE %(e_object)s=%(f_object)d AND %(e_date)s='%(m_date)s';"""
lxa_32_inst = """\
SELECT k_sample FROM %(table_name)s WHERE f_object=%(id_obiekt)d AND m_date='%(tvk_data)s';"""
lxa_33_inst = """\
SELECT k_sample FROM uu_power WHERE f_object=18 AND m_date='2013-01-31';"""
lxa_34_inst = """\
SELECT m_samples FROM %(table_name)s WHERE k_sample=%(nr_probki)d;"""
lxa_35_inst = """\
SELECT m_samples FROM uu_power WHERE k_sample=1860;"""
lxa_36_inst = """\
SELECT k_sample FROM uu_energy WHERE f_object=19 AND m_date='2013-02-01';"""
lxa_37_inst = """\
SELECT m_samples FROM uu_energy WHERE k_sample=1861;"""
lxa_38_inst = """\
SELECT m_date, m_samples FROM uu_energy WHERE f_object=7 ORDER BY m_date;"""
lxa_39_inst = """\
SELECT %(e_date)s, %(e_samples)s FROM %(table_name)s WHERE %(e_object)s=%(f_object)d ORDER BY %(e_date)s;"""
lxa_40_inst = """\
tabelkowiec"""
lxa_41_inst = """\
SELECT k_sample FROM uu_energy WHERE f_object=19;"""
lxa_42_inst = """\
SELECT k_sample FROM %(table_name)s WHERE f_object=%(id_obiekt)d;"""
lxa_43_inst = """\
formularz"""
