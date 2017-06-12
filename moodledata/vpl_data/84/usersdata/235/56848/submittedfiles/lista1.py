# -*- coding: utf-8 -*-
a=[]
n=int(input('digite o numero de elementos:'))
somai=0
somap=0
ni=0
np=0
for i in range(1,n+1,1):
    x=int(input('digite os elementos da lista:'))
    a.append(x)
    
for i in range(0,len(a),1):
    if a[i]%2==0:
        somai=somai+a[i]
        ni=ni+1

    else:
        somap=somap+a[i]
        np=np+1
print(somai)
print(somap)
print(ni)
print(np)
print(a)
        

