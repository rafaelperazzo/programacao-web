# -*- coding: utf-8 -*-
from __future__ import division

a=[]
n=input('Digite a quantidade de componentes da lista:')
for i in range (0,n,1):
    a.append(input('Digite um termo para a lista:'))
def maiordegrau(lista):
    maior=0
    for i in range (0,len(a),1):
        a[i]=maior
        a[i+1]=prox
        a[i-1]=ant
        if maior>prox and maior>ant:
            print maior
            
print maiordegrau(a)