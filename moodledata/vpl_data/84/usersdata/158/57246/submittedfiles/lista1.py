# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    x=int(input('digite um valor:'))
    lista.append(x)
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
soma3=0
for i in range(0,len(lista),1):
    if lista[i]%2==1:
        soma3=soma3+1
print(soma3)
soma4=0
for i in range(0,len(lista),1):
    if lista[i]%2==0:
        soma4=soma4+1
print(soma4)
print(lista)

