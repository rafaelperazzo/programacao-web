# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    
    if cont==1:
        return True
    else:
        return False
        
        
n=int(input('digite a quantidade de elementos:'))
a=[]
b=[]
for i in range(1,n+1,1):
    valor=int(input('digite um numero:'))
    a.append(valor)
for i in range(1,n+1,1):
    numero=int(input('digite um numero:'))
    b.append(numero)

if lecker(a):
    print('S')
else:
    print('N')

    

