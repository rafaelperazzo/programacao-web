# -*- coding: utf-8 -*-
from __future__ import division

def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x

def altura(l):
    maior=absoluto(l[0]-l[1])
    for i in range(0,len(l),1):
        if i==0:
            if absoluto(l[0]-l[1])>maior:
                maior=absoluto(l[0]-l[1])
        elif i==(len(l)-1):
            if absoluto(l[len(l)-2]-l[len(l)-1])>maior:
                maior=absoluto(l[len(l)-2]-l[len(l)-1])
        else:
            if absoluto(l[i]-l[i+1])>maior:
                maior=absoluto(l[i]-l[i+1])
    return maior
    
n=input('Digite o valor de n: ')

if n>=2:
    l=[]
    for i in range(0,n,1):
        l.append(input('Digite o elemento da lista: '))
    
    print(altura(l))
else:
    n=input('Digite o valor de n: ')
    

