# -*- coding: utf-8 -*-
from __future__ import division

def somadiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,i]
    return soma