# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite n:'))
soma1=0
soma2=0
cont1=0
cont2=0
for i in range(0,n,1):
    m=int(input('digite m:'))
    lista.append(m)
for i in range(0,len(lista),1):
    if lista[i]%2!=0:
        soma1=soma1+lista[i]
        cont1=cont1+1
    else:
        soma2=soma2+lista[i]
        cont2=cont2+1
print(soma1)
print(soma2)
print(cont1)
print(cont2)
print(lista)

