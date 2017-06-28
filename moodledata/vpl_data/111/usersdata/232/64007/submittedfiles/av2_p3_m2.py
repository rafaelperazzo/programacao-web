# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite o número de linhas de colunas da matriz: '))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite os termos da matriz: '))

def SomaLinhas(a):
    l=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        l.append(soma)
    return(l)
    
def SomaColunas(a):
    c=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        c.append(soma)
    return(c)

l=SomaLinhas(a)
c=SomaColunas(a)

for i in range (0,len(l)-1,1):
    if l[i]!=l[i+1]:
        LE=i

for i in range (0,len(c)-1,1):
    if c[i]!=c[i+1]:
        if c[i]<c[i+1]:
            CE=i
        else:
            CE=(i+1)
        
        

print(LE)
print(CE)