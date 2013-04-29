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

def to_jest_poprawny_plik_obrazu(fd):
    '''
    fd - otwarty deskryptor do zapisanego pliku,
    może też być to nazwa pliku na dysku
    Wartość zwrotna:
    - 0 - to nie obraz lub wystąpił inny problem
    - uchwyt do obrazu - w przypadku sukcesu
    '''
    try:
        im = Image.open(fd)
    except IOError:
        im = 0
    return im

def wykonaj_mniejsza_wersje(source_file, target_path, width):
    status = 1
    src_im = to_jest_poprawny_plik_obrazu(source_file)
    if src_im:
        src_width, src_height = src_im.size
        height = int(width * src_height / src_width)
        src_im.thumbnail((width, height))
        src_im.save(target_path)
    else:
        status = 0
    return status
