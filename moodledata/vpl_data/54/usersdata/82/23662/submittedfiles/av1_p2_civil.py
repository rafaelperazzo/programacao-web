# -*- coding: utf-8 -*-
from __future__ import division

def pinos(a):
    if a<0:
        a=a*(-1)
        return a
    else:
        return a

def cima(a):
    cima=l[0]
    for i in range (0,len(l),1):
        if a[i]>cima:
            cima=l[i]
    return maior

def baixo(a):
    baixo=a[i]
    for i in range (0,len(a),1):
        if a[i]<baixo:
            baixo=a[i]
    return baixo

def altura (a,altura):
    soma=pinos(cima(a)-altura) + pinos(menos(a)-altura)
return soma
