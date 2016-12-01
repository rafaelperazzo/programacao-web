# -*- coding: utf-8 -*-
from __future__ import division

def vidas(p,e,s):
    a=0
    for i in range(e,s+1,1):
        a=a+p[i]
    return a


p=input('Digite a quantidade de 