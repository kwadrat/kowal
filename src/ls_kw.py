#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

old_pil_is_present = 0
try:
    import Image
    old_pil_is_present = 1
except ImportError:
    from PIL import Image

if old_pil_is_present:
    import ImageDraw
else:
    from PIL import ImageDraw


def prepare_new_image(size, color):
    im = Image.new('RGB', size, color)
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
