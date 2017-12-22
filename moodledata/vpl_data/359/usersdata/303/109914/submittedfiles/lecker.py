# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de termos:'))
lista1=[]
for i in range(0,n,1):
    lista1.append(int(input('Digite o elemento:'))
cont=0
if n>1:
    if lista1[0]>lista1[1]:
        cont+=1
    for i in range(0,n,1):
        if i+2<n:
            if lista1[i]<lista1[i+1] and lista1[i+1]>lista1[i+2]:
                cont=+1
    if lista1[n-2]<lista1[n-1]:
        cont+=1
        
        
lista2=[]
for i in range(0,n,1):
    lista2.append(int(input('Digite o elemento:'))
cont2=0
if n>1:
    if lista2[0]>lista2[1]:
        cont2+=1
    for i in range(0,n,1):
        if i+2<n:
            if lista2[i]<lista2[i+1] and lista2[i+1]>lista2[i+2]:
                cont2=+1
    if lista2[n-2]<lista2[n-1]:
        cont2+=1

