# -*- coding: utf-8 -*-
n=[]
sem_repetir=[]
p=int(input('Digite a quantidade de pedidos: '))
for i in range (0,p):
    n.append(int(input('digite o tamanho: ')))
    
for i in n:
    if i not in sem_repetir:
        sem_repetir.append(i)
        
estoque=[]
for i in range (0,len(sem_repetir)):
    estoque.append(0)
    
fabricado=0
for i in range (0,p):
    pos=sem_repetir.index(n[i])
    if estoque[pos]==0:
        fabricado+=2
        estoque[pos]+=1
    elif estoque[pos]==1:
        estoque[pos]=0
    print(fabricado)
        
