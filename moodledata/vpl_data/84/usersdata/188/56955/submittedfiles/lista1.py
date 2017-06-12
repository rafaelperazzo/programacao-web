# -*- coding: utf-8 -*-
n=int(input('Digite o número de elementos da lista:'))
lista=[]
i=0
for i in range (1,n+1,1):
    valor=float(input('Digite o elemento:'))
    lista.append(valor)
contp=0
conti=0
somap=0
somai=0
for i in range (0,len(lista),1):
    if lista[i]%==0:
        contp=contp+1
        soma=somap+1
    else:
        conti=conti+1
        somai=somai(lista[i])
print(somai)
print(somap)
print(conti)
print(contp)
print(lista)