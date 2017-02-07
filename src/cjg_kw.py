#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

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

def rect_text(one_text):
    all_lines = one_text.splitlines()
    size_x = max(map(len, all_lines))
    lines_ls = []
    for one_line in all_lines:
        new_line = [' '] * size_x
        for nr, the_char in enumerate(one_line):
            new_line[nr] = the_char
        lines_ls.append(new_line)
    return lines_ls

class TestRectangledText(unittest.TestCase):
    def test_rectangled_text(self):
        '''
        TestRectangledText:
        '''
        self.assertEqual(rect_text('ab\ncd'), [
            ['a', 'b'],
            ['c', 'd'],
            ])
        self.assertEqual(rect_text('ab\nc'), [
            ['a', 'b'],
            ['c', ' '],
            ])
        self.assertEqual(rect_text('a\ncd'), [
            ['a', ' '],
            ['c', 'd'],
            ])
