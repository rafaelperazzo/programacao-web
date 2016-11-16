# -*- coding: utf-8 -*-
from __future__ import division

def congruencias(a,b,m,x0,n):
    x = []
    x.append(x0)
    
    for i in range(0,n,1):
        valor = ((a*x[i]+b)%m)/m
        x.append(valor)
    
    del(x[0])
    return x


a = input('Digite o valor de a: ')
b = input('Digite o valor de b: ')
m = input('Digite o valor de m: ')
x0 = input('Digite o valor de x0: ')
n = input('Digite o valor de n: ')


        
    
    
    
        
    





    
    
    