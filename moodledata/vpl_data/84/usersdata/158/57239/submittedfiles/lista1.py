# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    x=int(input('digite um valor:'))
    a=a.append(x)
soma1=0
for i in range(0,len(lista),1):
    if lista[i]%2==1:
        soma1=soma1+lista[i]
print(soma1)
soma2=0
for i in range(0,len(lista),1):
    if lista[i]%2==0:
        soma2=soma2+lista[i]
print(soma2)
cont1=0
for i in range(0,len(lista),1):
    if lista[i]%2==1:
        cont1=cont1+lista[i]
print(cont1)
cont2=0
for i in range(0,len(lista),1):
    if lista[i]%2==0:
        cont2=cont2+lista[i]
print(cont2)
print(a)

