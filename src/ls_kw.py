#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Image
import ImageDraw

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

def prepare_new_image(mode, size, color):
    im = Image.new(mode, size, color)
    draw = ImageDraw.Draw(im)
    return im, draw

def copy_existing_image(im):
        im2 = im.copy()
        draw2 = ImageDraw.Draw(im2)
        return im2, draw2
