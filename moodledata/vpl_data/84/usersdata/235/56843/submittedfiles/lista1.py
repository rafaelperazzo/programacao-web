# -*- coding: utf-8 -*-
a=[]
n=int(input('digite o numero de elementos:'))

for i in range(1,n+1,1):
    x=int(input('digite os elementos da lista:'))
    a.append(x)
somai=0
somap=0
ni=0
np=0
for i in range(0,len(a),1):
    if lista[i]%2==0:
        somai=somai+lista[i]
        ni=ni+1
for i in range(0,len(a),1):
    if lista[i]/2==0:
        somap=somap+lista[i]
        np=np+1
print(somai)
print(somap)
print(ni)
print(np)
print(a)
        

