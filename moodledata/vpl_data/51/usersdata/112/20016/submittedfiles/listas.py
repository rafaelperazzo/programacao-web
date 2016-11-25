# -*- coding: utf-8 -*-
from __future__ import division

a=[]
n=input('Digite a quantidade de componentes da lista:')
for i in range (0,n,1):
    a.append(input('Digite um termo para a lista:'))
def maiordegrau(lista):
    maior=0
    for i in range(0,len(lista),1):
        prox=a[i+1]
        atual=a[i]
        if prox!=atual:
            degrau1=prox-atual
            if degrau<0:
                degrau=degrau*(-1)
                return degrau
        
print maiordegrau(a)
        