# -*- coding: utf-8 -*-
n=int(input('Digite o numero de elementos da lista: '))
lista=[]
for i in range(0,n,1):
    lista.append(int(input('Digite os elementos da lista: ')))

somaP=0
somaI=0
nP=0
nI=0

for i in range(0,len(lista),1):
    if lista[i]%2!=0:
        somaI+=lista[i]
        nI+=1
    if lista[i]%2==0:
        somaP+=lista[i]
        nP+=1  

print(somaI)
print(somaP)
print(nI)
print(nP)
print(lista)