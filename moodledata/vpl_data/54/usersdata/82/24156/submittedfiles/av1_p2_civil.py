# -*- coding: utf-8 -*-
from __future__ import division

def absoluto(a):
    if a<0:
        return a*(-1)
    else:
        return a

def cima(a):
    cima=a[0]
    for i in range (0,len(a),1):
        if a[i]>cima:
            cima=a[i]
    return maior

def baixo(a):
    baixo=a[0]
    for i in range (0,len(a),1):
        if a[i]<baixo:
            baixo=a[i]
    return baixo

def altura(a,altura):
    soma=(absoluto(cima(a)-altura)+absoluto(baixo(a)-altura))
    return soma

n = input ('Digite o valor de n:')
m = input ('Digite o valor da m:')

b=[]

for i in range (0,n,1):
    b.append(input('Digite os elementos:'))
    
print ((altura(b,m))) 