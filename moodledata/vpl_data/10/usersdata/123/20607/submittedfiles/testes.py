# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def sistema(a,x,b):
    cont=0
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+ (a[i,j]*x[j])
        if soma!= (b[i]):
            cont=cont+1
    if cont==0:
        return True 
    else:
        return False
        
n=input('Insira a dimensão:')
a=np.zeros((n,n))
b=[]
x=[]
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('Insira um valor para a matriz:')
for i in range(0,n,1):
    b.append(input('Insira um valor para b:'))
for i in range(0,n,1):
    x.append(input('Insira um valor para x:'))
if sistema(a,x,b):
    print('S')
else:
    print('N')