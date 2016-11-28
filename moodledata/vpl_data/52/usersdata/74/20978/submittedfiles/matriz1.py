# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def reduzir(a):
    l = a.shape[0]
    c = a.shape[1]
    i = 0
    j = 0
    x = 1
    y = 1
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    
    if a[0,0] == 0:
        while cont1 == 0 and cont2 == 0:
            while (l-1)>=i:
                while (c-1)>j:
                    if a[i,j] == 1:
                        cont1 = i
                        cont2 = j
                    j = j+1
                i = i+1
                j = 0
    
    while cont3 == 0 and cont4 == 0:
        while l>=x:
            while c>=y:
                if a[l-x,c-y] == 1:
                    cont3 = l-x
                    cont4 = c-y
                y = y+1
            x = x+1
            y = 0
    nl = cont3-cont1
    nc = cont4-cont2
    
    c = np.zeros((nl,nc))
    w = 0
    z = 0
    p = cont2
    
    while (nl-1)>w:
        while(nc-1)>z:
            c[w,z]=a[cont1,cont2]
            z = z+1
            cont2 = cont2+1
        w = w+1
        cont = cont+1
        z = 0
        cont2 = p
    return c
        
l = input('Digite quantidades de linha: ')
c = input('Digite quantidades de coluna: ')

b = np.zeros((l,c))
u = 0
v = 0

while (l-1)>=u:
    while (c-1)>=v:
        b[u,v]=input('Digite o elemento: ')
        v = v+1
    u = u+1
    v = 0
    
print b
reduzir(b)


