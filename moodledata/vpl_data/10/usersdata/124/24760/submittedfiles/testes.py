# -*- coding: utf-8 -*-
from __future__ import division

def vabsol(x):
    if x < 0:
        x = -1*x
    return x

def calculopi(y):
    c = 3
    d = 2
    
    for i in range (0, y, 1):
        if i%2 != 0:
            c = c - (4/(d*(d+1)*(d+2)))
        elif i%2 == 0:
            c = c + (4/(d*(d+1)*(d+2)))
        d = d + 2
        
    return c
    
def cos(z, epsilon):
    cosz = 1
    v = 2
    fat = 1
    o = 1
    
    for i in range (v, 0, -1):
        fat = fat*i
        
    d = (z**2)/fat
    
    if o%2 != 0:
        cosz = cosz - d
    elif o%2 == 0:
        cosz = cosz + d
   
    while True:
        if epsilon < d:
            v = v + 2
            fat = 1
            o = o + 1
        else:
            break
    
    return cosz
    
def razaurea(m, epsilon):
    pi = calculopi(m)
    x = pi/5
    f = cos(pi/5, epsilon)
    ra = 2*f
    return ra
    
m = int(input('Digite o número m de termos da fórmula de pi:  '))
epsilon = input('Digite o epsilon para o cálculo da razão áurea: ')

m = vabsol(m)
print('Valor aproximado de pi: %.15f' %calculopi(m))
print('Valor aproximado da razão áurea: %.15f' %razaurea(m, epsilon))