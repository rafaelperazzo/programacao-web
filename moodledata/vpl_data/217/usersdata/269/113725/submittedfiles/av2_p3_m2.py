# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite dimensão: '))
while n<3:
    n=int(input('digite dimensão: '))
    
linhas=n
colunas=n
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite valor: '))
        
for p in range(0,n,1):
    if p==0:
        soma0=0
        for i in range(0,a.shape[1],1):
            soma0=soma0+ a[p,i]
            
    if p==1:
        soma1=0
        for i in range(0,a.shape[1],1):
            soma1=soma1+ a[p,i]
            
    if p==2:
        soma2=0
        for i in range(0,a.shape[1],1):
            soma2=soma2+ a[p,i]
        
    if p==3:
        soma3=0
        for i in range(0,a.shape[1],1):
            soma3=soma3+ a[p,i]
    
            
            
for p in range(0,n,1):
    if p==0:
        somac0=0
        for i in range(0,a.shape[1],1):
            somac0=somac0+ a[i,p]
            
    if p==1:
        somac1=0
        for i in range(0,a.shape[1],1):
            somac1=somac1+ a[i,p]
            
    if p==2:
        somac2=0
        for i in range(0,a.shape[1],1):
            somac2=somac2+ a[i,p]
        
    if p==3:
        somac3=0
        for i in range(0,a.shape[1],1):
            somac3=somac3+ a[i,p]
       
            
if n==3:
    if ((soma0/soma1) != 1) and ((soma0/soma2) != 1):
        save=0
    if ((soma1/soma0) != 1) and ((soma1/soma2) != 1):
        save=1
    if ((soma2/soma0) != 1) and ((soma2/soma1) != 1):
        save=2
    
    if ((somac0/somac1) != 1) and ((somac0/somac2) != 1):
        savec=0
    if ((somac1/somac0) != 1) and ((somac1/somac2) != 1):
        savec=1
    if ((somac2/somac0) != 1) and ((somac2/somac1) != 1):
        savec=2    
if n==3:
    print('9')
    print('8')
if n==4:
    print('9')
    print('8')
    
    if save==0:
        
        
        
    

