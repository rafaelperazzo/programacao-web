# -*- coding: utf-8 -*-
n=[]
estoque=[]
p=int(input('digite a quantidade de pedidos: '))
for i in range(0,p):
    n.append(int(input('digite o tamanho: ')))
    
for i in n:
    if i not in estoque:
        estoque.append(i)
print(estoque)

