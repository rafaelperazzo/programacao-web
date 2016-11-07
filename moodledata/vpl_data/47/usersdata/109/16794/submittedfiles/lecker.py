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
            if i>lista[i-1] and i>lista[i+1]:
                cont=cont+1
    if cont==1:
        print 'S'
    if cont!=1:
        print 'N'
        
n=input('Digite o valor de n:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('Digite um valor para a lista 1'))
for i in range (0,n,1):
    b.append(input('Digite um valor para a lista 1'))   
r1=lecker(a)
r2=lecker(b)

print r1
print r2
            
        