# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos das listas: '))
lista1=[]
lista2=[]
for i in range (0,n,1):
    for j in range (0,n,1):
        lista1.append(int(input('Digite o elemento da linha%.d e coluna%. da lista1: ' %(i,j))))
for i in range (0,n,1):
    for j in range (0,n,1):
        lista1.append(int(input('Digite o elemento da linha%.d e coluna%. da lista2: ' %(i,j))))
cont1=0
cont2=0
if lista1[0]<lista1[1]:
    cont1+=1
for i in range (0,n,1):
    if i+2<n:
        if lista1[i]>lista1[i+1] and lista1[i+1]<lista1[i+2]:
            cont1+=1
if lista1[n-2]>lista1[n-1]:
    cont+=1
if cont1==1:
    print('S')
if cont1>1:
    print('N')
if lista2[0]<lista2[1]:
    cont2+=1
for i in range (0,n,1):
    if i+2<n:
        if lista2[i]>lista2[i+1] and lista2[i+1]<lista2[i+2]:
            cont2+=1
if lista2[n-2]>lista2[n-1]:
    cont2+=1
if cont2==1:
    print('S')
if cont2>1:
    print('N')