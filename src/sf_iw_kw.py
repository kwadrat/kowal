#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import pprint

NazwyModulow = [wyrazy.split()[1] for wyrazy in '''\
import lk_kw
'''.splitlines()]

for i in NazwyModulow:
    if i == __name__.split('.')[-1]:
        raise RuntimeError('Modul laduje sam siebie?: %s' % repr(i))
    else:
        if i in globals():
            exec '%(modul)s = reload(%(modul)s)' % dict(modul = i)
        else:
            exec 'import %(modul)s' % dict(modul = i)

def ile_bajtow_pliku(nazwa):
    return os.path.getsize(nazwa)

def plik_istnieje(nazwa):
    return os.path.isfile(nazwa)

def kat_istnieje(nazwa_katalogu):
    return os.path.isdir(nazwa_katalogu)

def list_dir(nazwa_katalogu):
    wykaz = os.listdir(nazwa_katalogu)
    wykaz.sort()
    return wykaz

def rename(src, dst):
    os.rename(src, dst)
    return 1 # Sukces

def rmdir(src):
    os.rmdir(src)
    return 1 # Sukces

def unlink(src):
    os.unlink(src)
    return 1 # Sukces

def nazwa_katalogu_jest_poprawna(nazwa_katalogu):
    return len(nazwa_katalogu) > 0

def zrob_odpowiednie_prawa(nazwa):
    status = 1
    try:
        os.chmod(nazwa, lk_kw.PrawaDostepuPliku)
    except OSError:
        status = 0
    return status

def sprawdz_lub_utworz_katalog_logu(pelna_nazwa_klt_lgu):
    if not os.path.isdir(pelna_nazwa_klt_lgu):
        os.mkdir(pelna_nazwa_klt_lgu)

def create_dir_if_nonexistent(nazwa_katalogu):
    if not os.path.isdir(nazwa_katalogu):
        os.mkdir(nazwa_katalogu)
        zrob_odpowiednie_prawa(nazwa_katalogu)

def wczytaj_plik(nazwa):
    fd = open(nazwa, 'rb')
    dane = fd.read()
    fd.close()
    return dane

def otworz_do_zapisu(nazwa):
    return open(nazwa, 'wb')

def otworz_do_logowania(nazwa):
    return open(nazwa, 'a')

def zapisz_z_uchwytu(nazwa, src_fd):
    status = 1 # Poprawne wykonanie zapisu
    try:
        dst_fd = otworz_do_zapisu(nazwa)
        rozmiar = 16 * 1024
        src_fd.seek(0)
        while 1:
            porcja = src_fd.read(rozmiar)
            if porcja:
                dst_fd.write(porcja)
            else:
                break
        dst_fd.close()
    except IOError:
        status = 0
    return status

def domknij_zapisany_plik(nazwa, fd, verbose, mode):
    fd.close()
    if mode is not None:
        os.chmod(nazwa, mode)
    if verbose:
        print "Zapisano do pliku '%s'." % nazwa

def zapisz_plik(nazwa, dane, verbose = 0, mode = None):
    fd = otworz_do_zapisu(nazwa)
    fd.write(dane)
    domknij_zapisany_plik(nazwa, fd, verbose, mode)

def zapisz_ladnie(nazwa, dane, verbose=0, mode=None, prefix=None):
    fd = otworz_do_zapisu(nazwa)
    if prefix is not None:
        fd.write(prefix)
    pprint.pprint(dane, stream=fd)
    domknij_zapisany_plik(nazwa, fd, verbose, mode)

def zapisz_jawnie(nazwa, dane):
    zapisz_plik(nazwa, dane, verbose=1)

def zapisz_warunkowo(nazwa, dane):
    if dane:
        zapisz_jawnie(nazwa, dane)
