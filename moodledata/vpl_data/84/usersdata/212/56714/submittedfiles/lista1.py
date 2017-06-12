# -*- coding: utf-8 -*-
n=int(input('digite tamanho da lista'))
a=[]
i=0
soma0=0
somap=0
ni=0
np=0
cont=0
while i<n:
    valor=int(input('digite um nmero para a lista'))
    a.append(valor)
    i=i+1
while cont<n:
    if a[i]%2==0:
        np=np+1
        somap=somap+a[i]
    else:
        ni=ni+1
        somai=somai+a[i]
    cont=cont+1
print(somai)
print(somap)
print(ni)
print(np)