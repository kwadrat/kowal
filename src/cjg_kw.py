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
    if all_lines:
        size_x = max(map(len, all_lines))
        lines_ls = []
        for one_line in all_lines:
            new_line = [' '] * size_x
            for nr, the_char in enumerate(one_line):
                new_line[nr] = the_char
            lines_ls.append(new_line)
    else:
        lines_ls = None
    return lines_ls

def transpose_text(one_text):
    result = zip(*one_text)
    result = map(list, result)
    return result

def matrix_to_text(one_matrix):
    all_lines = map(lambda x: (''.join(x)).rstrip(), one_matrix)
    result_txt = '\n'.join(all_lines)
    return result_txt

def reverse_text(one_matrix):
    return map(lambda x: list(reversed(x)), one_matrix)

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
        self.assertEqual(rect_text(''), None)

    def test_transposed_text(self):
        '''
        TestRectangledText:
        '''
        self.assertEqual(transpose_text([
            ['a', 'c', 'e'],
            ['b', 'd', 'f'],
            ]), [
            ['a', 'b'],
            ['c', 'd'],
            ['e', 'f'],
            ])
        self.assertEqual(transpose_text([
            ['a', 'c', 'e'],
            ]), [
            ['a'],
            ['c'],
            ['e'],
            ])

    def test_text_from_matrix(self):
        '''
        TestRectangledText:
        '''
        self.assertEqual(matrix_to_text([
            ['a', 'b'],
            ['c', 'd'],
            ]), 'ab\ncd')
        self.assertEqual(matrix_to_text([
            ['a', ' '],
            ['c', 'd'],
            ]), 'a\ncd')

    def test_reversed_text(self):
        '''
        TestRectangledText:
        '''
        self.assertEqual(reverse_text([
            ['a', 'c', 'e'],
            ['b', 'd', 'f'],
            ]), [
            ['e', 'c', 'a'],
            ['f', 'd', 'b'],
            ])
