# -*- coding: utf-8 -*-
from __future__ import division
import math
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
    
def fatorial(a):
    fat = 1
    for i in range (a, 0, -1):
        fat = fat*i
    return fat

def cos(z, epsilon):
    cosz = 1
    v = 2
    cont = 1

    d = (z**v)/fatorial(v)

    if cont%2 != 0:
        cosz = cosz - d
    elif cont%2 == 0:
        cosz = cosz + d
    while True:
        if epsilon <= d:
            v = v + 2
            cont = cont + 1
            d = 0
        else:
            break

    return cosz
    
def ncos(z, epsilon):
    v = 2
    cosz = 1
    cont = 0
    
    d = (z**v)/fatorial(v)
    while True:
        if epsilon <= d:
            if cont%2 == 0:
                cosz = cosz - (z**v)/fatorial(v)
            elif cont%2 != 0:
                cosz = cosz + (z**v)/fatorial(v)
            v = v + 2
            cont = cont + 1
        else:
            break
    
    return cosz
    
def razaurea(m, epsilon):
    pi = calculopi(m)
    fi = ncos(pi/5, epsilon)
    return fi
    
m = int(input('Digite o número m de termos da fórmula de pi:  '))
epsilon = input('Digite o epsilon para o cálculo da razão áurea: ')

m = vabsol(m)
print('Valor aproximado de pi: %.15f' %calculopi(m))
print('Valor aproximado da razão áurea: %.15f' %razaurea(m, epsilon))