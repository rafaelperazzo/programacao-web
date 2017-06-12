# -*- coding: utf-8 -*-
n=int(input('tamanho da lista:'))
a=[]
soma=0
for i in range (0,n,1):
    a.append(int(input('valores da lista:')))
    soma=soma+a[i]
    media=soma/(len(a))
print('%f'%a[0])
print('%f'&a[len(a)-1])
print(a[i])

