# -*- coding: utf-8 -*-
from __future__ import division

def elementos(x,y):
    cont=0
    for i in range(0,len(y)-1,1):
        j=0
        while j<len(x)-1:
            if y[i]==x[j]:
                cont=cont+1
                break
    return cont    
    
n=input('Digite o valor de n:')
m=input('Digite o valor de m:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite um elemnteo de a:'))
for i in range(0,m,1):
    b.append(input('Digite um elemento de b:'))
R=elementos(a,b)
print(R)