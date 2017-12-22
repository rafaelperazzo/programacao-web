# -*- coding: utf-8 -*-
lista=[]
n=int(input('Digite a quantidade de termos da lista: '))
for i in range(0,n,1):
    num=int(input('Digite um numero para a lista: '))
    lista.append(num)

soma1=0
cont1=0
soma2=0
cont2=0
for num in range(0,n-1,1):
    if lista[num]%2==0:
        soma1=soma1+(lista[num])
        cont1=cont1+1
    else:
        soma1=soma1+(lista[num])
        cont2=cont2+1
        
print(soma1)
print(soma2)
print(cont1)
print(cont2)
print(lista)



