# -*- coding: utf-8 -*-
from __future__ import division
def lecker(n):
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
        print(False)

n=int(input('Digite o número:'))
a=[]
valor1=int(input('Digite os elementos da lista 2:'))
a.append(valor1)

b=[]
valor2=int(input('Digite os elementos da lista 2:'))
b.append(valor2)

if lecker(a):
    print('Lecker')
    
else:
    print('Não')
    

if lecker(b):
    print('Lecker')
    
else:
    print('Não')
    
        