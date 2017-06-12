# -*- coding: utf-8 -*-
n=int(input('digite o numero de termo:'))
lista=[]
somai=0
somap=0
conti=0
contp=0
for i in range(0,n,1):
    x=int(input('numeros da lista:'))
    lista.append(x)
for j in range(0,len(list),1):
    if lista[j]%2!=0:
        somaai=somai+lista[j]
        conti=conti+1
    else:
        somap=somap+lista[j]
        contp=contp+1
print (somai)
print (somap)
print (conti)
print (contp)
print (lista)
