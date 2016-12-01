# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Funçoes
def somaLinha(a):
    somal=0
    somafl=0
    for j in range (0,a.shape[1],1):
        somal=somal+a[x,j]
    somafl=somal-a[x,y]
    
    return somafl
    
def somaColuna(a):
    somal=0
    somafc=0
    for i in range (0,a.shape[0],1):
        somal=somal+a[i,y]
    somafc=somal-a[x,y]
    
    return somafc

def somaTotal(a):
    somaT=somaLinha(a)+somaColuna(a)


#Entrada
n=input('Digite e dimensão da matriz: ')
a=np.zeros( (n,n) )
x=input('Digite o valor de x: ')
y=input('Digite o valor de y: ')


for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento: ')
        
#Saida
print ('%.d'%somaTotal(a))