# -*- coding: utf-8 -*-
lista=[]
n=int(input('Digite a quantidade de termos da lista: '))
for i in range(0,n,1):
    num=int(input('Digite um numero para a lista: '))
    lista.append(num)

somai=0
somap=0
conti=0
contp=0
for num in range(0,n,1):
    if (lista[num]%2)==0:
        somap=somap+list[num]
        contp=contp+1
    else:
        somai=somai+lista[num]
        conti=conti+1
        
print(somai)
print(somap)
print(cont1)
print(contp)
print(lista)



