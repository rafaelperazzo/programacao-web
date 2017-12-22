# -*- coding: utf-8 -*-
n=[]
semr=[]
p=int(input('digite a quantidade de pedidos: '))
for i in range(0,p,1):
    n.append(int(input(1 digite o tamanho:  ')))
for i in n:
    if i not in semr:
        semr.append(i)
estoque=[]
for in range(0,len(semr),0):
    estoque.append(0)
fabricado=0
for in range(0,p,1):
    pos=semr.index(n[i])
    if estoque[pos]==0
        fabricado+=2
        estoque[pos]+=1
    elif estoque[pos]==1:
        estoque[pos]=0
print(fabricado)
