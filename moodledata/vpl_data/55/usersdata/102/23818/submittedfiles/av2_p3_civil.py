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
print('%d'%peso(a,x,y))
    

n=input('digite o valor da dimensao da matriz':)
a=np.zeros((n,n))


    
    
    


