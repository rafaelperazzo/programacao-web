# -*- coding: utf-8 -*-
from __future__ import division

def pinos(a):
    if a<0:
        a=a*(-1)
        return a
    else:
        return a

def cima(a):
    cima=a[0]
    for i in range (0,len(a),1):
        if a[i]>cima:
            cima=a[i]
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

x = input ('Digite o valor de x:')
y = input ('Digite o valor de y:')

a=[]
for i in range (0,n,1):
    a.append (input('Digite um elemento:'))
print ('%d' (altura(a,y)) 
