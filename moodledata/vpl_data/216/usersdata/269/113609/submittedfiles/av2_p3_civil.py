# -*- coding: utf-8 -*-
import numpy as np
linhas=int(input('quantidade de linha: '))
colunas=linhas
a=np.zeros((linhas,colunas))

x=int(input('digite i: '))
y=int(input('digite j: '))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite elemento da matriz a: '))
somal1=0        
for i in range(y,a.shape[1],1):
    somal1=somal1+a[x,i+1]
somal2=0
for i in range(0,y,1):
    somal2=somal2+a[x,i]

somac1=0
for i in range(x,a.shape[0],1):
    somac1=somac1+a[i+1,y]
    
somac2=0
for i in range(0,x,1):
    somac2=somac2+a[i+1,y]
somatot=somal1+somal2+somac1+somac2 
print(a)
print(somatot)    

