# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np



def somal(a,x):
    
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[x,j]
        
       
    return soma
    
def somac(a,y):

    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,y]
        
    return soma

def peso(a,x,y):
    soma=0
    soma=somal+somac-2*a[x,y]
    return soma


n=input('digite o valor de n:')
a=np.zeros((n,n))
x=[]
y=[]
for i in range(0,n,1):
    x.append(input('digite o valor de x:'))
for i in range(0,n,1):
    y.append(input('digite o valor de y:'))
    
print('%d'%(peso(a,x,y)))
      
   
    


    
    
    


