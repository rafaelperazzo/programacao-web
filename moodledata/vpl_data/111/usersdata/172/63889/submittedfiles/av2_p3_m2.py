# -*- coding: utf-8 -*-
import numpy as np
def le(a,b):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range(0,len(lista),1):
        
    






def l(a):
    s1=0
    s2=0
    s3=0
    for i in range(0,a.shape[0],1):
        s1=s1+a[i,0]
        s2=s2+a[i,1]
        s3=s3+a[i,2]
    if s1==s2:
        l=s1
    else:
        l=s3
    return (l)    
        
        
        
        for l in range(0,a.shape[1],1):
            soma=soma+a[i,l]
        return(soma)    
def somacolunas(a):
    soma=0
    for l in range(0,a.shape[1],1):
        for l in range(0,a.shape[0],1):
            soma=soma+a[i,l]            
        return(soma)
def somadiagonalprincipal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            if i==l:
                soma=soma+a[i,l]
    return(soma)            
n=int(input('linhas e colunas:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
        a[i,l]=float(input('valor:'))
print(a)