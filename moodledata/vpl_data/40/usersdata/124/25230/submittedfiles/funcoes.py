# -*- coding: utf-8 -*-
from __future__ import division
#ARQUIVO COM SUAS FUNCOES
def vabsol(x):
    if 0 > x:
        x = -1*x
    return x
    
def calculopi(m):
    pi = 3
    d = 2
    c = 0
    for i in range (0, m, 1):
        if i%2 != 0:
            c = c - (4/(d*(d+1)*(d+2)))
        else:
            c = c + (4/(d*(d+1)*(d+2)))
        d = d + 2
    
    return c+pi
    
def fatorial(a):
    fat = 1
    for i in range (a, 0, -1):
        fat = fat*i
    return fat

def cos(z, epsilon):
    cosz = 1
    v = []
    cont = 1
    fatores = 2
    while (z**fatores)/fatorial(fatores) >= epsilon:
        v.append(fatores)
        fatores = fatores + 2
        
    for i in range (0, len(v), 1):
        if cont%2 != 0:
            cosz = cosz - (z**v[i])/fatorial(v[i])
        else:
            cosz = cosz + (z**v[i])/fatorial(v[i])
        cont = cont + 1
 
    return cosz
    
def razaurea(m, epsilon):
    pi = calculopi(m)
    fi = 2*cos(pi/5, epsilon)
    return fi