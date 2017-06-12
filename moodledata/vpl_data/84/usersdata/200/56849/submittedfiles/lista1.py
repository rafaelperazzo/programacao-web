# -*- coding: utf-8 -*-
n=int(input('digite o tamanho da lista'))
a[]
i=0
somai=0
somap=0
ni=0
np=0
cont=0
while i<n:
    valor=int(input('digite um numero para a lista'))
    a.append(valor)
    i=i+1
cont=0
while cont<n:
    if a[cont]%2==0:
        np=np+1
        somap=somap+a[cont]
    else:
        ni=ni+1
        somai=somai+a[cont]
    cont=cont+1
print(somai)
print(somap)
print(ni)
print(np)
print(a)

