# -*- coding: utf-8 -*-
from __future__ import division

a=[]
n=input('Digite a quantidade de componentes da lista:')
for i in range (0,n,1):
    a.append(input('Digite um termo para a lista:'))
def maiordegrau(lista):
    novaLista=[]
    for i in range(0,len(lista)-1,1):
        if a[i]>a[i+1]:
            degrau= a[i]-a[i+1]
        else:
            degrau*(-1)
        novaLista.append(degrau)
        maiordegrau=0
        for j in range(0,len(novaLista),1):
            if novaLista[i]>maiordegrau:
                maiordegrau=novaLista[i]
        return maiordegrau
    
        
print maiordegrau(a)
        