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
            if (i+j) == (dimensao-1) :
                soma = soma + A[i,j]
        d.append(soma)
    return(d)
#ENTRADA
dimensao = int(input('Digite a dimensão da matriz: '))
a=np.zeros((dimensao,dimensao))

for i in range (0,dimensao,1) :
    for j in range (0,dimensao,1) :
        a[i,j] = int(input('Digite o elemento da matriz : '))
e = []
#PROCESSAMENTO
e.append(somalinha(a))
e.append(somacoluna(a))
e.append(dprincipal(a))
e.append(dsecundaria(a))
print(e)
cont = 0

for i in range (0,len(e),1):
    if e[0] != e[i]:
        print('N')
        break
    else:
        cont = cont + 1 
    
if cont == len (e):
    print('S')


    
        
        
            
            


