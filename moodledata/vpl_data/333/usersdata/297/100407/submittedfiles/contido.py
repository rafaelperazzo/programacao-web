# -*- coding: utf-8 -*-
def contido(a,b,n,q):
    q = 0
    for i in range(0,n,1):
        if a[i] in b :
            q = q+1
    return print(q)
    
n=int(input('digite o numero de elementos que a lista n tera: '))
m=int(input('digite o numero de elementos que b lista m tera: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input('digite o elemento de a %d: '%(i+1))))
for i in range(0,m,1):
    b.append(int(input('digite o elemento de b %d: '%(i+1))))'''
contido(a,b,n,q)