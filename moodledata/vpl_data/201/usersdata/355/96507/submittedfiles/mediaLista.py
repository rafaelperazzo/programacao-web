# -*- coding: utf-8 -*-
lista=[]
n= int(input('Digite a quantidade de números: '))
soma=0
for quant in range(0,n,1):
    num=int(input('Digite um valor: '))
    lista.append(num)
    soma=soma+num
print(lista(0))
print(lista(len(lista)-1))

print((soma)/(len(lista)))
