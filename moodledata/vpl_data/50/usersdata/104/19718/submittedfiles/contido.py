# -*- coding: utf-8 -*-
from __future__ import division
def cont(x,y):
    cont=0
    if len(x)>len(y):
        for i in range(0,y,1):
            for j in range(0,x,1):
                if y[i]==x[j]:
                    cont=cont+1
    else:
        for i in range(0,x,1):
            for j in range(0,y,1):
                if x[i]==y[j]:
                    cont=cont+1
    return cont

n=input('Digite o n elementos para a:')
m=input('Digite o m elementos para b:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite um valor para a:'))
for i in range(0,m,1):
    b.append(input('Digite um valor para b:'))

total=cont(a,b)
print total

