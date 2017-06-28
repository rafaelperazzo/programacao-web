# -*- coding: utf-8 -*-
import numpy as np
def somalinha(a):
    c=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        c.append(soma)
    for r in range(0,len(c),1):
        if c[0]!=c[i]:
            return False
        else:
            return (c[0])
def somacoluna(a):
    b=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i.j]
        b.append(soma)
    for k in range(0,len(b),1):
        if b[0]!=b[i]:
            return False
        else:
            return (b[0])
def somadiagonais(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return (soma)
def somadiag2(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[a.shape[0]-i-1,i]
    return soma
n=int(input('Digite a dimensão da matriz: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite os valores: '))
x=somalinha(a)
y=somacoluna(a)
w=somadiagonais(a)
z=somadiag2(a)
if x==False or y==False:
    print('N')
else:
    if x==y==z==w:
        print('S')
    else:
        print('N')
        
    
    
    
    

