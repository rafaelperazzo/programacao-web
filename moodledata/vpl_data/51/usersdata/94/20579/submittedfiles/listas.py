# -*- coding: utf-8 -*-
from __future__ import division
import math 

def modulo(c):
    modulo=((c**2)**0.5)
    return modulo
    
def variacao(lista):
    maior=0
    for i in range (0,len(lista)-1,1):
        degrau=(lista[i+1]-lista[i])
        if degrau > maior:
            maior=degrau
    return maior
    
a=[]
z=input('digite a quantidade de a:')
for i in range (0,z,1):
    a.append(input('digite o elemento:')
    
v=variacao(a)
print('%.d'%v)
    
