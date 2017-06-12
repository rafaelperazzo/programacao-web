# -*- coding: utf-8 -*-
n=int(input('Digite o número de elementos da lista:'))
a=[]
i=0
for i in range (1,n+1,1):
    valor=int(input('Digite o elemento:'))
    a.append(valor)
contp=0
conti=0
somap=0
somai=0
for i in range(0,len(a),1):
    if a[i]%2==0:
        contp=contp+1
        somap=somap+(a[i])
    else:
        conti=conti+1
        somai=somai+(a[i])
print(somai)
print(somap)
print(conti)
print(contp)
print(a)