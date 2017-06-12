# -*- coding: utf-8 -*-
from __future__ import division

def lecker(n):
    i=0
    cont=0
    for i in range(1,len(n),1):
        if i==0:
            if n[i]>n[i+1]:
                cont=cont+1
        elif i==len(n)-1:
            if n[i]>n[i-1]:
                cont=cont+1
        else:
            if n[i]>n[i+1] and n[i]>n[i-1]:
                cont=cont+1
            
if cont==1:
    return(True)
    
else:
    return(False)

n=int(input('Digite o número:'))
a=[]
for i in range(0,n,1):
    valor1=float(input('Digite os elementos da lista 1:'))
a.append(valor1)

b=[]
for i in range(0,n,1):
    valor2=float(input('Digite os elementos da lista 2:'))
b.append(valor2)

if lecker(a):
    print('Sim')
else:
    print('Não')
if lecker(b):
    print('Sim')
else:
    print('Não')
    
        