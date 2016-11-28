# -*- coding: utf-8 -*-
from __future__ import division

#ENCONTRAR COLUNA DA ESQUERDA
def menor_coluna(a):
    for j in range(0, a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                return j
    


