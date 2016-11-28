# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

    
    
def somadaslinhas(a):
    s=[]
    for i in range(0,a.shpe[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append (soma)
    return s
    
def somaadascolunas(a):
    s=[]
    for j in range(0,a.shpe[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append (soma)
    return s
    
def quadradom(a):
    sd=somad(a)
    sds=somad2(a)
    
    sl=somal(a)
    sc=somac(a)
    cont=0
    
    for i in range(0,len(sll),1):
        if sd==sds==sl[i]==sc[i]:
            cont=cont+1
    if cont==len(sl):
        
        
        return True
    else:
        return False
        
        
n=input('digite a dimensao da matriz:')

a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um valor:')
            
if quadradom(a):
    print('S')
else:
    print('N')
   
            
    