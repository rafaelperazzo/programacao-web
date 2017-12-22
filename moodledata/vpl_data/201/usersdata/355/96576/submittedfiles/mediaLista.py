# -*- coding: utf-8 -*-
a=[]
n= int(input('Digite a quantidade de números: '))
soma=0
for quant in range(0,n,1):
    num=int(input('Digite um valor: '))
    a.append(num)
    soma=soma+num
print('%.2f'% a[0])

print('%.2f'% a[len(a)-1])

print('%.2f'% (soma)/(len(a)))

print(a)
