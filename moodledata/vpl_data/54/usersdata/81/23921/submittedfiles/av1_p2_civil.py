# -*- coding: utf-8 -*-
from __future__ import division

def menor(lista):
    t=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]<t:
            t=lista[i]
    return t
    
def maior(lista):
    t=lista[0]
    for i in range(0,çen(lista),1):
        if lista[i]>t:
            t=lista[i]
    return t