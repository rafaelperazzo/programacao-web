# -*- coding: utf-8 -*-
from __future__ import division

def inter(listaa,listab):
    cont=0
    for i in range(0,len(listab)-1,1):
        if listab[i] in listaa:
            cont=cont+1
    return cont
        

#principal
n=input('Qtd de elementos de a:')
m=input('Qtd de elementos de b:')
a=[]
b=[]

for i in range (0,n,1):
    a.append('Digite um elemento para a:')

for i in range(0,m,1):
    b.append('Digite um elemento para b:')
    
resultado=inter(a,b)
print resultado
