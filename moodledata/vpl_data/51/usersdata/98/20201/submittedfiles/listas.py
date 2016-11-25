# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#DEFININDO A FUNÇÃO
def degrau(a):
    maior=0
    
    for i in range(0,len(a)-1,1):
        diferenca=a[i]-a[i+1]
        if diferenca<0:
            diferenca= -diferenca
        if diferenca>maior:
            maior=diferenca
    return maior

#CRIANDO A LISTA

n=input('Digite o numero de termos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor para a lista a: '))

print degrau(a)