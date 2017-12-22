# -*- coding: utf-8 -*-

lista=[]
n=int(input('Digite a quantidade de numeros da lista: '))
for i in range(0,n,1):
    num=int(input('Digite o numero da lista: '))
    lista.append(num)
    
somap=0
contp=0
somai=0
conti=0
for numero in range(0,n,1):
    if (((lista[numero])%2)==0):
        somap=soma+(lista[numero])
        contp=contp+1
    else:
        somai=somai+(lista[numero])
        conti=conti+1
        
print(somai)
print(somap)
print(conti)
print(contp)
