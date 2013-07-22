#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import fy_kw
import dv_kw
import dn_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

class BuilderBash(object):
    def __init__(self, this_time=None):
        '''
        BuilderBash:
        '''
        self.src_dir = 'bkw'
        self.src_d_dir = 'dkw'
        if this_time is None:
            self.this_time = dn_kw.SekTeraz()
        else:
            self.this_time = this_time

    def deploy_by_hand(self):
        '''
        BuilderBash:
        '''
        cm_name = 'akw_%s' % self.this_time
        return ''.join([
            'git checkout -b %s; git checkout master\n' % cm_name,
            'cd ../dkw; git checkout -b %s; git checkout master; cd ../bkw\n' % cm_name,
            'vi ../dkw/src/rq_kw.py\n',
            'rm ../ckw/src/*.py; cp ../dkw/src/*.py ../ckw/src/; rm ../akw/*.py; cp *.py ../akw/; git checkout co_kw.py; touch ../akw/pw_kw.py\n',
            ])

    def code_snapshot(self):
        '''
        BuilderBash:
        '''
        file_name = '%(src_dir)s_%(this_time)s.tar.bz2' % dict(
            src_dir=self.src_dir,
            this_time=self.this_time,
            )
        return 'cd ..;tar cjf %(file_name)s %(src_dir)s %(src_d_dir)s;mv %(file_name)s %(src_dir)s; cd %(src_dir)s\n' % dict(
            src_dir=self.src_dir,
            src_d_dir=self.src_d_dir,
            file_name=file_name,
            )

class TestBashBuilder(unittest.TestCase):
    vassertEqual = dv_kw.vassertEqual
    def test_bash_builder(self):
        '''
        TestBashBuilder:
        '''
        obk = BuilderBash('2013.01.31_23.59.00')
        self.assertEqual(obk.deploy_by_hand(), fy_kw.lxa_19_inst)
        self.assertEqual(obk.code_snapshot(), fy_kw.lxa_20_inst)
