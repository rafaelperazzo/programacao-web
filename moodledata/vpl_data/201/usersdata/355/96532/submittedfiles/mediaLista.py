# -*- coding: utf-8 -*-
a=[]
n= int(input('Digite a quantidade de números: '))
soma=0
for quant in range(0,n,1):
    num=int(input('Digite um valor: '))
    a.append(num)
    soma=soma+num
print(a(0))

print(a(len(a)-1))

print((soma)/(len(a)))
