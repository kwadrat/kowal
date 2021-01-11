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
SELECT k_sample, f_object, m_date, m_samples FROM uu_power WHERE f_object=123 AND m_date = '2013-01-31' ORDER BY m_date;"""
lxa_10_inst = """\
    %s integer NOT NULL,
"""
lxa_11_inst = """\
SELECT """
lxa_12_inst = """\
 FROM """
lxa_13_inst = """\
SELECT uu_object.account,m_date,m_samples FROM uu_power,uu_object WHERE uu_power.f_object=uu_object.k_object ORDER BY uu_power.f_object, uu_power.m_date;"""
lxa_14_inst = """\
SELECT %(uu_object)s.%(account)s,%(e_date)s,%(e_samples)s FROM %(table_name)s,%(uu_object)s WHERE %(polaczony_warunek)s ORDER BY %(table_name)s.%(e_object)s, %(table_name)s.%(e_date)s;"""
lxa_15_inst = """\
INSERT INTO uu_object (account) VALUES ('n') RETURNING k_object;"""
lxa_16_inst = """\
INSERT INTO %(uu_object)s (%(account)s) VALUES ('%(under_name)s') RETURNING %(k_object)s;"""
lxa_17_inst = """\
INSERT INTO uu_power (f_object, m_date, m_samples, m_none, m_zero, m_sum) VALUES (123, '2013-01-31', '{NULL,0,0,1.5,2.5,3}', 1, 2, 7.0);"""
lxa_18_inst = """\
INSERT INTO %(n_table)s (%(e_object)s, %(e_date)s, %(e_samples)s, %(e_none)s, %(e_zero)s, %(e_sum)s) VALUES (%(f_object)d, '%(m_date)s', %(m_samples)s, %(v_none)s, %(v_zero)s, %(v_sum)s);"""
lxa_19_inst = """\
git checkout -b akw_2013.01.31_23.59.00; git checkout master
cd ../dkw; git checkout -b akw_2013.01.31_23.59.00; git checkout master; cd ../bkw
vi ../dkw/src/rq_kw.py
rm ../ckw/src/*.py; cp ../dkw/src/*.py ../ckw/src/; rm ../akw/*.py; cp *.py ../akw/; cd ../dkw; git checkout src/rq_kw.py; cd ../bkw; touch ../akw/pw_kw.py
"""
lxa_20_inst = """\
cd ..;tar cjf bkw_2013.01.31_23.59.00.tar.bz2 bkw dkw;mv bkw_2013.01.31_23.59.00.tar.bz2 bkw; cd bkw
"""
lxa_21_inst = """\
UPDATE uu_power SET m_samples='{NULL,0,0,1.5,2.5,3}', m_none=1, m_zero=2, m_sum=7.0 WHERE k_sample=8 AND f_object=123 AND m_date='2013-01-31';"""
lxa_22_inst = """\
UPDATE %(n_table)s SET %(e_samples)s=%(m_samples)s, %(e_none)s=%(v_none)s, %(e_zero)s=%(v_zero)s, %(e_sum)s=%(v_sum)s WHERE %(e_key_sample)s=%(k_sample)d AND %(e_object)s=%(f_object)d AND %(e_date)s='%(m_date)s';"""
lxa_23_inst = """\
 WHERE """
lxa_24_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND m_date >= '2013-03-11' AND m_date < '2013-03-25' ORDER BY m_date;"""
lxa_25_inst = """\
SELECT m_samples FROM uu_energy WHERE m_date >= '2013-03-12' AND m_date < '2013-03-26' ORDER BY m_date;"""
lxa_26_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND m_date < '2013-03-25' ORDER BY m_date;"""
lxa_27_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND m_date >= '2013-03-11' ORDER BY m_date;"""
lxa_28_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=1 AND EXTRACT(dow FROM m_date)=0 ORDER BY m_date;"""
lxa_29_inst = """\
SELECT m_samples FROM uu_power WHERE f_object=1 AND EXTRACT(dow FROM m_date)=1 ORDER BY m_date;"""
lxa_30_inst = """\
23"""
lxa_33_inst = """\
SELECT m_samples FROM uu_power WHERE f_object=18 AND m_date = '2013-01-31' ORDER BY m_date;"""
lxa_36_inst = """\
SELECT m_samples FROM uu_energy WHERE f_object=19 AND m_date = '2013-02-01' ORDER BY m_date;"""
lxa_38_inst = """\
SELECT m_date, m_none, m_zero, m_sum FROM uu_energy WHERE f_object=7 ORDER BY m_date;"""
lxa_39_inst = """\
SELECT %(part_my_fields)s FROM %(my_table_name)s%(part_my_limits)s ORDER BY %(e_date)s;"""
lxa_40_inst = "tabelkowiec"
lxa_43_inst = 'formularz'
lxa_44_inst = '''\
selwyborca'''
lxa_45_inst = '''\
this.form.submit();'''
lxa_46_inst = '''\
Dziękujemy za wpisywanie faktur za wodę i kanalizację, od 1 lutego 2010 roku nie trzeba wpisywać nowych faktur, są one automatycznie wczytywane do systemu.
'''
lxa_47_inst = '''\
<script type="text/javascript">
Calendar.setup({
inputField  : "data",
electric    : false,
ifFormat    : "%Y-%m-%d",
weekNumbers: false
});

var wzor_data = "regexp=^[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]$";
var kmnt_data = "Podaj datę w postaci RRRR-MM-DD (albo kliknij dla otwarcia kalendarza)";
frmvld = new Validator("formularz");
frmvld.addValidation("data", "req", "Potrzebuję daty");
frmvld.addValidation("data", wzor_data, kmnt_data);
</script>'''
lxa_48_inst = """\
SELECT k_sample, m_samples FROM uu_energy ORDER BY m_date;"""
lxa_50_inst = """\
UPDATE uu_power SET m_none=1, m_zero=2, m_sum=7.0 WHERE k_sample=8;"""
lxa_51_inst = """\
UPDATE %(n_table)s SET %(e_none)s=%(v_none)s, %(e_zero)s=%(v_zero)s, %(e_sum)s=%(v_sum)s WHERE %(e_key_sample)s=%(k_sample)d;"""
lxa_52_inst = """\
SELECT m_date, m_none, m_zero, m_sum FROM uu_energy WHERE f_object=8 ORDER BY m_date;"""
lxa_53_inst = """\
SELECT m_date, m_none, m_zero, m_sum FROM uu_power WHERE f_object=8 ORDER BY m_date;"""
lxa_54_inst = """\
SELECT m_date, m_none, m_zero, m_sum FROM uu_energy ORDER BY m_date;"""
lxa_55_inst = """\
SELECT m_samples FROM uu_power ORDER BY m_date;"""
lxa_56_inst = """\
suma narastająco"""
lxa_57_inst = """\
moc maksymalna"""
lxa_58_inst = """\
SELECT m_date, m_sum FROM uu_energy WHERE f_object=19 AND m_date >= '2013-02-01' AND m_date < '2013-03-01' ORDER BY m_date;"""
lxa_59_inst = """\
SELECT m_date, m_sum FROM uu_energy WHERE f_object=19 AND m_date >= '2013-01-01' AND m_date < '2014-01-01' ORDER BY m_date;"""
lxa_60_inst = """\
0"""
lxa_61_inst = """\
SELECT uu_object.account,m_date,m_samples FROM uu_power,uu_object WHERE uu_power.f_object=uu_object.k_object AND uu_object.k_object=123 ORDER BY uu_power.f_object, uu_power.m_date;"""
lxa_62_inst = """\
SELECT uu_object.account,m_date,m_samples FROM uu_power,uu_object WHERE uu_power.f_object=uu_object.k_object AND uu_object.k_object=123 AND uu_power.m_date >= '2013-01-01' AND uu_power.m_date < '2013-02-01' ORDER BY uu_power.f_object, uu_power.m_date;"""
lxa_63_inst = """\
SELECT k_sample, m_samples FROM uu_power ORDER BY m_date;"""
lxa_64_inst = """\
SELECT k_object, account FROM uu_object ORDER BY k_object;"""
lxa_65_inst = """\
SELECT %(k_object)s, %(account)s FROM %(uu_object)s ORDER BY %(k_object)s;"""
