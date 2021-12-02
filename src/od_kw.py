#!/usr/bin/python
# -*- coding: UTF-8 -*-

import oj_kw

CommonTGK = oj_kw.CommonTGK

class PseudoTGK(CommonTGK):
    def __init__(self):
        '''
        PseudoTGK:
        '''
        CommonTGK.__init__(self)
        self.qparam = {}
