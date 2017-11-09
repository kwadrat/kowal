#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import sys
import time

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def date_as_string(one_time):
    time_tuple = time.localtime(one_time)
    return time.strftime('%Y.%m.%d_%H.%M.%S', time_tuple)

class BaildonTime(object):
    def __init__(self):
        '''
        BaildonTime:
        '''

    def start_timing(self):
        '''
        BaildonTime:
        '''
        self.baildon_start = time.time()

    def till_now(self, one_label):
        '''
        BaildonTime:
        '''
        time_a = self.baildon_start
        self.baildon_start = time_b = time.time()
        total_seconds = time_b - time_a
        total_minutes, small_seconds = divmod(total_seconds, 60)
        total_hours, small_minutes = divmod(total_minutes, 60)
        txt_hms_diff = '%02d:%02d:%02d' % (
            total_hours,
            small_minutes,
            small_seconds,
            )
        txt_secs = '(%s s)' % total_seconds
        txt_secs = '%10s' % txt_secs
        all_text = ''.join([
            date_as_string(time_a),
            ' - ',
            date_as_string(time_b),
            ' ',
            txt_hms_diff,
            txt_secs,
            ' ',
            one_label,
            ])
        print >> sys.stderr, all_text

baildon_time = BaildonTime()

def hms_start():
    baildon_time.start_timing()

def hms_period(one_label):
    baildon_time.till_now(one_label)
