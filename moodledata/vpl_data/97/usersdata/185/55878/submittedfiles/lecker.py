# -*- coding: utf-8 -*-
from __future__ import division
def lacker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
        
n=int(input('digite a quantidade de elementos da lista:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o valor da lista a:'))
    a.append(valor)
    
b=[]
for i in range(0,n,1):
    valor=int(input('digite o valor da lista b:'))
    b.append(valor)
    
if lacker(a):
    print('S')
else:
    print('N')
    
if lacker(b):
    print('S')
else:
    print('N')
    


