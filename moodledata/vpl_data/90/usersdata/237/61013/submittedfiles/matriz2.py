# -*- coding: utf-8 -*-
import numpy as np
a=int(input("Digite o número de linhas: "))
b=int(input("Digite o número de colunas: "))
m=np.zeros((a,b))
for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=float(input("Digite um termo: "))
c=0 
o=0
p=0
for i in range (0,m.shape[0],1):
    c=c+(m[0,i])
for i in range (0,m.shape[1],1):
    o=o+(m[i,0])
for i in range (0,m.shape[0],1):
    for j in range (1,m.shape[1],1):
        if i==j:
            p=p+(a[i,j])
if c==p==o:
    print("S")
else:
    print("N")