# -*- coding: utf-8 -*-
from __future__ import division

def total(a):
    if a<0:
        a=a*(-1)
        return a
    else:
        return a
    
def pino_alto(a):
    pinoa=a[0]
    for i in range(0,len(a),1):
        if a[i]>pinoa:
            pinoa=a[i]
    return pinoa
    
def pino_baixo(a):
    pinom=a[0]
    for i in range(0,len(a),1):
        if a[i]<pinom:
            pinom=a[i]
    return pinom
    
def altura(a,alt):
    calculo=total(pino_alto(a)-alt)+total(pino_baixo(a)-alt)
    return calculo
    
n=input('digite a quantidade de pinos:')
m=input('digite a altura:')
a=[]

for i in range(0,n,1):
    a.append(input('digite o elemento:'))
print altura(a,m)
