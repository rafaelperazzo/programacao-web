# -*- coding: utf-8 -*-
lista=[]
n=int(input('Digite a quantidade de números da lista: '))
for i in range(0,n,1):
    num=int(input('Digitem o numero da lista: '))
    lista.append(num)
    
for numero in range(0,n,1):
    somap=0
    contp=0
    somai=0
    conti=0
    if (((lista[numero])%2)==0) :
        somap=somap+(lista[numero])
        contp=contp+1
    else:
        somai=somai+(lista[numero])
        conti=conti+1
        
print(somai)
print(somap)
print(conti)
print(contp)
print(lista)
