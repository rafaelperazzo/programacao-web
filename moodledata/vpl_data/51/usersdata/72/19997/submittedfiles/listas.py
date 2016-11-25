# -*- coding: utf-8 -*-
from __future__ import division

def maior(lista):
    cont=0
    for i range(0,len(lista),1):
        if len(lista[i])>len(lista[i+1]):
            x=lista[i]-lista[i+1]
            cont=cont+1
        if x>len(lista):
            return x
