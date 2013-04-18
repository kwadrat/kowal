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
SELECT * FROM t WHERE f_object=123 AND m_date='2013-01-31' AND m_time='23:34';"""
lxa_10_inst = """\
SELECT * FROM %(n_table)s WHERE %(e_object)s=%(f_object)d AND %(e_date)s='%(m_date)s' AND %(e_time)s='%(m_time)s';"""
lxa_11_inst = """\
INSERT INTO t (f_object, m_date, m_time, m_value) VALUES (123, '2013-01-31', '23:34', 0.000000);"""
lxa_12_inst = """\
INSERT INTO %(n_table)s (%(e_object)s, %(e_date)s, %(e_time)s, %(e_value)s) VALUES (%(f_object)d, '%(m_date)s', '%(m_time)s', %(m_value)f);"""
lxa_13_inst = """\
SELECT uu_object.account,m_date,m_time,m_value FROM t,uu_object WHERE t.f_object=uu_object.k_object;"""
lxa_14_inst = """\
SELECT %(uu_object)s.%(account)s,%(e_date)s,%(e_time)s,%(e_value)s FROM %(table_name)s,%(uu_object)s WHERE %(table_name)s.%(e_object)s=%(uu_object)s.%(k_object)s;"""
lxa_15_inst = """\
INSERT INTO uu_object (account) VALUES ('n') RETURNING k_object;"""
lxa_16_inst = """\
INSERT INTO %(uu_object)s (%(account)s) VALUES ('%(under_name)s') RETURNING %(k_object)s;"""
