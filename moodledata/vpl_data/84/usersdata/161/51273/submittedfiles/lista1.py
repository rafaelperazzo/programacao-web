# -*- coding: utf-8 -*-
lista[]
n=int(input('Digite n:'))
soma1=0
soma2=0
cont1=0
cont2=0
for i in range(1,n+1,1):
    numero=int(input('Digite um número:'))
    lista.append(numero)
for termo in range(0,len(lista),1):
    if lista[termo]%2==0:
        cont1=cont1+1
        soma1=soma1+termo
    else:
        cont=cont2+1
        soma2=soma2+termo
print(soma2)
print(soma1)
print(cont2)
print(cont1)
print(lista)
    
    

