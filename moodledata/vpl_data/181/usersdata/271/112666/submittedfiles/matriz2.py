# -*- coding: utf-8 -*-
import numpy as np
#FUNÇÕES
def somalinha (A) :
    a=[]
    soma = 0
    for i in range (0,A.shape[0],1) :
        soma = 0
        for j in range (0,A.shape[1],1) :
            soma = soma + A[i,j]
        a.append(soma)
    return(a)
def somacoluna (A) :
    b = []
    soma = 0
    for j in range (0,A.shape[1],1) :
        soma = 0
        for i in range (0,A.shape[0],1) :
            soma = soma + A[i,j]
        b.append(soma)
    return(b)
    
def dprincipal (A) :
    c = []
    soma = 0
    for i in range (0,A.shape[0],1) :
        for j in range (0,A.shape[1],1) :
            if (i==j) :
                soma = soma + A[i,j]
        c.append(soma)
    return(c)
        
def dsecundaria (A) :
    d = []
    soma = 0
    for i in range (0,A.shape[0],1) :
        for j in range (0,A.shape[1],1) :
            if (i+j) == (A.shape[0]-1) :
                soma = soma + A[i,j]
        d.append(soma)
    return(d)
#ENTRADA
dimensao = int(input('Digite a dimensão da matriz: '))
z=np.zeros((dimensao,dimensao))

for i in range (0,dimensao,1) :
    for j in range (0,dimensao,1) :
        z[i,j] = int(input('Digite o elemento da matriz : '))
e = []
#PROCESSAMENTO

a = somalinha(z)
b = somacoluna(z)
c = dprincipal(z)
d = dsecundaria(z)


cont = 0

for i in range (0,len(a),1):
    if a[0] != a[i]:
        print('N')
        break
    else:
        cont = cont + 1 
    
for i in range (0,len(b),1):
    if a[0] != b[i]:
        print('N')
        break
    else:
        cont = cont + 1
        
for i in range (0,len(c),1):
    if a[0] != c[i]:
        print('N')
        break
    else:
        cont = cont + 1   
        
for i in range (0,len(d),1):
    if a[0] != d[i]:
        print('N')
        break
    else:
        cont = cont + 1
        
if cont == (2*dimensao) + 2:
    print('S')


    
        
        
            
            


