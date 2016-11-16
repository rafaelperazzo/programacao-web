# -*- coding: utf-8 -*-
from __future__ import division

def elementos(x,y):
    cont=0
    for i in range(0,len(y)-1,1):
        j=0
        while j<len(x)-1:
            if y[i]==x[j]:
                cont=cont+1
                break
    return cont    