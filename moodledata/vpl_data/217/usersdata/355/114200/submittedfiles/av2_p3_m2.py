# -*- coding: utf-8 -*-
import numpy as np

n=int(input("Digite a dimensão da matriz: "))

matriz=np.zeros(n,n)
M0=M1=M2=0
for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i,j]=float(input("Digite os elementos da matriz: "))
        if j==0:
            M0=matriz[i,j]+M0
        if j==1:
            M1=matriz[i,j]+M1
        if j==2:
            M2=matriz[i,j]+M2
            
if M0==M1:
    m=M0
else:
    if M1==M2:
        m=M1
    else:
        m=M0


for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        soma=soma+matriz[i,j]
        if j=(matriz.shape[1]):
            if soma!=((i+1)*m):
                break
                x=i
                
for j in range(0,matriz.shape[1],1):
    for i in range(0,matriz.shape[0],1):
        soma1=soma1+matriz[i,j]
        if i==(matriz.shape[0],1):
            if soma1!=((j+1)*m):
                break
                y=j
for j in range(0,matriz.shape[1],1):
    soma2=soma2+matriz[x,j]
    
for i in range(0,matriz.shape[0],1):
    soma3=soma3+matriz[i,y]
    
if soma2<m:
    m-soma2=a
    a+matriz[x,y]=o
    print(o)
else:
    soma2-m=a
    matriz[x,y]-a=0
    print(o)

if soma3<m:
    m-soma3=b
    b+matriz[x,y]=o2
    print(o2)
else:
    soma3-m=b
    matriz[x,y]=o2
    print(o2)
        
    
        
        

