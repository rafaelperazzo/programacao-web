# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 

k = input ('insira a dimensão da matriz:')

a = np.zeros ((k,k))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('insira um elemento para a matriz:') 
        
#Somatório das linhas 

cont2=0
m=0
for i in range (0,a.shape[0],1):
    cont=0
    for j in range (0,a.shape[1],1):
        cont=cont +a[i,j]
    if i==0:
        cont2=cont
    if cont!=cont2:
        m=m+1
        

#Somatório das linhas 

cont2=0
m=0
for i in range (0,a.shape[0],1):
    cont=0
    for j in range (0,a.shape[1],1):
        cont=cont +a[i,j]
    if i==0:
        cont2=cont
    if cont!=cont2:
        m=m+1
        
    
#Somatório das linhas 

cont2=0
m=0
for i in range (0,a.shape[0],1):
    cont=0
    for j in range (0,a.shape[1],1):
        cont=cont +a[i,j]
    if i==0:
        cont2=cont
    if cont!=cont2:
        m=m+1
        
    
#somatório das colunas:
cont4=0
n=0
for j in range (0,a.shape[1],1):
    cont3=0
    for i in range (0,a.shape[0],1):
        cont3=cont3+a[i,j]
    if j==0:
        cont4=cont3 
    if cont4!=cont3:
        n=n+1

#somatório das diagonais 

#Diagonal principal 

cont5=0
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if i==j:
            cont5=cont5+a[i,j]
        
#Diagonal secundária 

cont6=0
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if i+j==a.shape[0]-1:
            cont6=cont6+a[i,j]


#Saída 

if m==0 and n==0:
    if cont==cont3==cont5==cont6:
        print ('S')
    else: 
        print ('N')
else: 
    print ('N')
    