# -*- coding: utf-8 -*-
from __future__ import division

a=[]
n=input('Digite a quantidade de componentes da lista:')
for i in range (0,n,1):
    a.append(input('Digite um termo para a lista:'))
def maiordegrau(lista):
    maior=0
    Nmaior=0
    Nmaior=maior
    for i in range (0,len(a),1):
        a[i]=maior
        if a[i]<a[i+1]:
            a[i+1]=Nmaior
            return Nmaior
            
print maiordegrau(a)