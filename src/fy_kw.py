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
select k_object from uu_object where account='abc';"""
lxa_8_inst = """\
select %(k_object)s from %(uu_object)s where %(account)s='%(under_name)s';"""
lxa_9_inst = """\
select * from t where f_object=123 and m_date='2013-01-31' and m_time='23:34';"""
lxa_10_inst = """\
select * from %(n_table)s where %(e_object)s=%(f_object)d and %(e_date)s='%(m_date)s' and %(e_time)s='%(m_time)s';"""
lxa_11_inst = """\
insert into t (f_object, m_date, m_time, m_value) values (123, '2013-01-31', '23:34', 0.000000);"""
lxa_12_inst = """\
insert into %(n_table)s (%(e_object)s, %(e_date)s, %(e_time)s, %(e_value)s) values (%(f_object)d, '%(m_date)s', '%(m_time)s', %(m_value)f);"""
lxa_13_inst = """\
select uu_object.account,m_date,m_time,m_value from t,uu_object where t.f_object=uu_object.k_object;"""
lxa_14_inst = """\
select %(uu_object)s.%(account)s,%(e_date)s,%(e_time)s,%(e_value)s from %(table_name)s,%(uu_object)s where %(table_name)s.%(e_object)s=%(uu_object)s.%(k_object)s;"""
lxa_15_inst = """\
insert into uu_object (account) values ('n') returning k_object;"""
lxa_16_inst = """\
insert into %(uu_object)s (%(account)s) values ('%(under_name)s') returning %(k_object)s;"""
