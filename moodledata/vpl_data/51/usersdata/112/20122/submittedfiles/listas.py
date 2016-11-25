# -*- coding: utf-8 -*-
from __future__ import division

a=[]
n=input('Digite a quantidade de componentes da lista:')
for i in range (0,n,1):
    a.append(input('Digite um termo para a lista:'))
def maiordegrau(lista):
    for i in range(0len(lista)-1,1):
        if a[i]>a[i+1]:
            degrau= a[i]-a[i+1]
        if a[i]<a[i+1]:
            degrau= a[i+1]-a[i]
    novaLista=[]
        novaLista.append(degrau)
        maiordegrau=0
        for j in range(0,len(novaLista),1):
            if novaLista[i]>maiordegrau:
                maiordegrau=navalista[i]
        return maiordegrau
    
        
print maiordegrau(a)
        