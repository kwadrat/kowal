#!/usr/bin/python
# -*- coding: UTF-8 -*-

def warn_halt(flag, text):
    if flag:
        raise RuntimeError(text)
    else:
        print text
