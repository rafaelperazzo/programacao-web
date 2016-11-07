# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
def Desvio(l):
    soma=0
    soma2=0
    for i in range(0,len(l),1):
        soma=soma+l[i]
    media:(soma/len(l))
    for i in range(0,len(l),1):
        soma2=soma2+((l[i]-media)**2)
    s=(soma2/(len(l)-1))**0,5
    return (s)

n=input('Digite a quantidade de termos da lista: ')
l=[]

for i in range(0,n,1):
    l.append(input('Digite um valor: ))
    
print Desvio(l)